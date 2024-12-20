# 多焦点音場再構成

Author: Shun Suzuki

Date: 2024-01-09

- - -

本節では, Holo Gainの実装, すなわち, フェーズドアレーを用いた多焦点の音像の再構成手法について述べる.

なお, 本文章では,

1.  各振動子の特性は同一
1.  非線形項は無視できる, すなわち, 音場は個々の振動子が放出したものの重ね合わせになる

という事を仮定する.

## 定式化

問題の定義は以下となる.

「$M$点の焦点$\br_i$における音圧の振幅$|p_i|, i = 0,1,...,M-1$が与えられたとき,
これを出力するような$N$個の振動子の振幅と位相, すなわち,
$$\begin{aligned}
  |p_i| & = |(G\bq)_i|,                   \\
  \bq   & = [q_0,..., q_{N-1}]\trans, q_j = a_j\rme^{-\im \phi_j}, \\
  G     & \in \mathbb{C}^{M\times N},
\end{aligned}$$
を満たす$\bq$を求めたい.
ただし, 振動子の出力$a_j$には上限があり, $|a_j| \le a = \mathrm{const.}, \forall j$を満たす.」

ここで, $G$は伝達行列であり, 例えば,
障害物のない状態の球面波を仮定すると, $$\begin{aligned}
  G_{ij} = \frac{1}{4\pi\|\br_i - \br_j\|}\rme^{\im k\|\br_i - \br_j\|},
\end{aligned}$$ である. また, $k$は波数, $\br_j$は振動子の位置である.
なお,
振動項$\rme^{-\im\omega t}$はすべての振動子で同一と仮定したので無視する.

Sさらに指向性$D(\theta)$と空気による吸収項$\rme^{\alpha \|\br_i - \br_j\|}$を考慮して
$$\begin{aligned}
  G_{ij} = \frac{D(\theta)}{4\pi\|\br_i - \br_j\|}\rme^{\alpha \|\br_i - \br_j\|}\rme^{\im k\|\br_i - \br_j\|},
\end{aligned}$$
とするモデル化もあるが, 本章の議論は本質的に$G$の要素の表記に依らない.

### 複素数への拡張: 焦点の位相の導入

焦点$\br_i$における複素音圧の位相を$\psi_i$とすると, 上式はまとめて
$$\begin{aligned}
  \bp & = G\bq,                              \\
  \bp & = [p_0,..., p_{M-1}]\trans, p_i = |p_i|\rme^{-\im \psi_i},
\end{aligned}$$
と書ける.

一般的に, 超音波フェーズドアレーによる触覚提示や音響浮遊において, この位相$\psi_i$は重要でない.
例えば, $\SI{40}{kHz}$の超音波で考えると, 2つの焦点が同位相で振動していたとしても, 逆位相 (すなわち, $\SI{12.5}{us}$のずれ)で振動していたとしても, ヒトの触覚は区別できない.
したがって, $\bq$に加えて, 焦点の位相$\psi_i$にも自由度がある.

以下に, この問題の解法をいくつかの分類に分けて論じていく. 
なお, この分類は筆者の恣意的なものである.

- [空間分割スキーム](./partitioning.md)
- [逆フーリエ変換](./fourier.md)
- [半正定値緩和法](./sdp.md)
- [固有値問題と行列方程式](./evp.md)
- [逆伝搬法](./back_prop.md)
- [非線形最小二乗法](./nlsp.md)
- [音響パワー最適化法](./apo.md)
- [貪欲法](./greedy.md)
