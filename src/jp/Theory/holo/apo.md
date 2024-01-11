# 音響パワー最適化法

Author: Shun Suzuki

Date: 2024-01-09

- - -

> NOTE: この手法は現在SDKでは実装されていない.

実際の応用上は, 音圧よりも音圧の二乗, すなわちパワーが重要である.
そこで, 長谷川らはこれを最適化する手法を提案した[^hasegawa2020volumetric].
すなわち, この方法では, 以下の最適化を考える.
$$\begin{aligned}
    \min \sum_{i} \left[|(G\bq)_i|^2 - |p_i|^2\right]^2
\end{aligned}$$
この場合は, 制御点の位相成分を最適化する必要はない.

さて, $(i,i)$成分のみ$1$であり, ほかは$0$である行列を$D_i$と表すと,
$$\begin{aligned}
    |(G\bq)_i|^2 = \bq\hermite G\hermite D_i G\bq
\end{aligned}$$
である. 論文 [^hasegawa2020volumetric]では, Tikhonov正則化を採用し, 以下の目的関数$J(\bq)$の最適化をBroyden--Fletcher--Goldfarb--Shanno (BFGS) 法[^fletcher2013practical]により行っている.
$$\begin{aligned}
    J(\bq) & = \sum_{i} \left[|\bq\hermite R_i\bq - |p_i|^2\right]^2 + \lambda (\bq\hermite\bq), \\
    R_i    & = G\hermite D_i G
\end{aligned}$$

なお, 論文 [^hasegawa2020volumetric]では初期値は, 
$$\begin{aligned}
    \bq_0 = (G\hermite G + \lambda \1)^{-1}G\hermite \bp
\end{aligned}$$ としている.
ただし, $\bp$の位相はすべて$0$である.

[^hasegawa2020volumetric]: Hasegawa, Keisuke, Hiroyuki Shinoda, and Takaaki Nara. "Volumetric acoustic holography and its application to self-positioning by single channel measurement." Journal of Applied Physics 127.24 (2020).

[^fletcher2013practical]: Fletcher, R. "Practical methods of optimization." (1987).

