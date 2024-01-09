# 貪欲法

Author: Shun Suzuki

Date: 2024-01-09

- - -

ここまでの手法は, 振動子の振幅・位相を連続量としていた.
しかし, 実際には, フェーズドアレイの駆動は離散量で指定する.
しかも, かなり低い量子化深度($\sim\SI{4}{bit}$)で十分である ([位相, 及び, 振幅の必要分解能](../resolution.md)参照).

したがって, 位相を離散化することで, 組合せ最適化問題として解く方法が考えられる.

## 貪欲法 (Greedy)

組み合わせ最適化問題として解く方法の1つに,貪欲法と全探索を用いた方法がある[^suzuki2021radiation].

以下にそのアルゴリズムを示す.
振動子の振幅と位相が$a_j\in\{a_i^k\}_{k=0,1,...,K-1}, \phi_j\in\{\phi_i^l\}_{l=0,1,...,L-1}$のように離散化されていると, このアルゴリズムは

1. $\bq = \bzero$で初期化
1. $j=0, ..., N-1$まで以下を繰り返す
    1. $k=0, ..., K-1$まで以下を繰り返す
        - $l=0, ..., L-1$まで以下を繰り返す
            - $E_j^{kl} = E(q_0, ...,q_{j-1}, a_j^k\rme^{-\im\phi_{j}^l})$を計算する.
    1. $q_j \leftarrow a_j^{k^*}\rme^{-\im\phi_{j}^{l^*}}$としてセットする. ここで, $l^*$は$E_j^{k^*l^*} = \min{\{E_j^{kl}\}}$を満たす.

である. 
このアルゴリズムでは, まず, 1つの振動子を駆動する.
そして, 全ての可能な振幅位相を探索した後, 最適なものを選ぶ.
次に, この振動子の出力は固定して, 新たな振動子を追加し, この新たな振動子に対して全ての可能な振幅位相を探索した後, 最適なものを選んで固定する.
これを全ての振動子に対して繰り返していく.
なお, 振動子の選択はランダムに行うべきである[^suzuki2021radiation].

ここで評価関数$E(q_0, ...,q_j)$は$0$番目から$j$番目までの振動子を駆動した際の, 目標音圧と実際に生成される音圧との二乗誤差であり
$$\begin{aligned}
  E(q_0, ...,q_j) = \sum_i^{M-1}\left| |p(\br_i)| - \left|\sum_{k=0}^{j}G_{ik}q_k\right|\right|^2,
\end{aligned}$$
である.
なお,
$$\begin{aligned}
  \sum_{k=0}^{j}G_{ik}q_k = \sum_{k=0}^{j-1}G_{ik}q_k + G_{ij}q_j
\end{aligned}$$
であるため, $\sum_{k=0}^{j}G_{ik}q_k$をキャッシュ化しておくことで, 評価関数の計算は$O(M)$で行える.
したがって, このアルゴリズムは明らかに$O(KLMN)$で実行できる.

この手法のメリットは, 焦点の位相を最適化する必要がないことである.
また, 計算速度的にも有利である.

### 焦点位相に対する貪欲法 (LSSGreedy)

上記のアルゴリズムでは振動子の振幅/位相を離散化したが, 焦点の位相を離散化し, 単一焦点の重ね合わせ解において最適な焦点の位相を貪欲法と全探索で求める方法もある[^chen2022sound].
なお, 現状このアルゴリズムを使用するメリットは特になく, Greedyのほうが基本的に性能は良いのでSDKには実装されていない.

[^suzuki2021radiation]: Suzuki, Shun, et al. "Radiation pressure field reconstruction for ultrasound midair haptics by Greedy algorithm with brute-force search." IEEE Transactions on Haptics 14.4 (2021): 914-921.

[^chen2022sound]: Chen, Jianyu, et al. "Sound Pressure Field Reconstruction for Ultrasound Phased Array by Linear Synthesis Scheme Optimization." International Conference on Human Haptic Sensing and Touch Enabled Computer Applications. Cham: Springer International Publishing, 2022.
