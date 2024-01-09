# 逆フーリエ変換

Author: Shun Suzuki

Date: 2024-01-09

- - -

ここでは, 逆フーリエ変換を用いた方法を示す.
これもSDKには実装されていないが[^3], 参考のために載せておく.

この手法では, フェーズドアレイが2次元平面グリッド上に配置されている場合を考える.
また, 焦点もこのアレイに水平な面内に配置されており, アレイ表面から十分離れているとする.

このとき, xy平面上の振動子を添字$u,v$で区別する.
すなわち,
$$\begin{aligned}
    \br_j & = (x_u, y_v, 0), \\
    \br_i & = (x, y, z),
\end{aligned}$$
とする.
また, $$\begin{aligned}
    |x_u|,|y_v| & \ll |z|,
\end{aligned}$$
を満たすと仮定する.

この時, $$\begin{aligned}
    \|\br_i - \br_j\| & = \sqrt{(x-x_u)^2 + (y-y_v)^2 + z^2}                                                                                                                    \\
                      & = z \left( \frac{(x-x_u)^2}{z^2} + \frac{(y-y_v)^2}{z^2} + 1\right)^\frac{1}{2}                                                                         \\
                      & \sim z \left( 1 + \frac{1}{2} \frac{(x-x_u)^2}{z^2} + \frac{1}{2}\frac{(y-y_v)^2}{z^2} \right) & (\because |x_u|,|y_v| \ll |z|) \\
                      & = z + \frac{x^2+y^2}{2z} - \frac{xx_u + yy_v}{z} +  \frac{x_u^2 + y_v^2}{2z}                                                                            \\
                      & \sim z + \frac{x^2+y^2}{2z} - \frac{xx_u + yy_v}{z},
\end{aligned}$$
となる. 
ここで, 最初の近似をFresnel近似, 最後の近似をFraunhofer近似という.
さらに,
$$\begin{aligned}
    \frac{1}{\|\br_i - \br_j\|} \sim \frac{1}{z},
\end{aligned}$$
と近似する.
これを近軸近似という.

これらの近似を用いると $$\begin{aligned}
    p(x,y,z) & \sim \sum_{u = 0}^{U-1}\sum_{v = 0}^{V-1} a_{uv}\rme^{-\im\phi_{uv}} \frac{1}{z}\exp\left[\im k\left(z + \frac{x^2+y^2}{2z} - \frac{xx_u + yy_v}{z}\right)\right]                                 \\
             & = \frac{1}{z} \exp\left[\im k\left(z + \frac{x^2+y^2}{2z}\right)\right] \sum_{u = 0}^{U-1}\sum_{v = 0}^{V-1} a_{uv}\rme^{-\im\phi_{uv}} \exp\left[\im k\left(\frac{xx_u + yy_v}{z}\right)\right],
\end{aligned}$$
となる.

最後の総和はフェーズドアレイ表面の振幅位相パターンの2次元離散フーリエ変換にほかならない.
したがって,
$$\begin{aligned}
    p(x,y,z) z \exp\left[-\im k\left(z + \frac{x^2+y^2}{2z}\right)\right] & \sim \mathcal{F}[a_{uv}\rme^{-\im\phi_{uv}}].
\end{aligned}$$
$$\begin{aligned}
    \therefore a_{uv}\rme^{-\im\phi_{uv}} \sim \mathcal{F}^{-1} \left[p(x,y,z) z \exp\left[-\im k\left(z + \frac{x^2+y^2}{2z}\right)\right]\right],
\end{aligned}$$
となる.

この場合の計算量は, アレイが$\sqrt{N}\times\sqrt{N}$の正方形だとすると,
2次元FFTを用いて$O(N\log_2 \sqrt{N})$になる.

[^3]: 基本的に, この手法で得られる音場が弱い, アレイと目標音場がそれぞれ平面的である必要がある, 目標音場の指定が面倒, といった問題点があり, 実装に見合った利得がないため.