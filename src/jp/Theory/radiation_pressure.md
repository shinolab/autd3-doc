# 音響放射圧

Author: Shun Suzuki

Date: 2024-01-06

- - -

一般的に, 音波はそれが伝搬する媒質に置かれた物体に定常的な力を与える.
これを放射圧 (Radiation Pressure) と呼ぶ.
一般的に, 放射圧はRayleigh放射圧とLangevin放射圧に分類される.
前者はある容器内に閉じ込められた音波が壁にもたらす放射圧である. 
一方, 後者は自由空間に置かれた物体に作用する放射圧である.
例えば, 音響浮遊や触覚提示では後者の状況を考えるので, 本稿は後者の放射圧のみ扱うこととする.

音響放射圧の説明には, 平均エネルギー密度を用いたものがあるが, ここでは流体力学の観点から説明する.
平均エネルギー密度による説明は文献[^saneyoshi_ultrasound_1978]などに詳しい (なお, 平均エネルギー密度による説明は, 音場が平面波に分解できるときのみ成り立つことが指摘されている[^hasegawa1996_jp]).
本文章の議論は[^eckart1948vortices], [^awatani1955studies], [^hasegawa2000general]に基づく.
一部, 個人的な解釈を入れるので, 原論文と読み比べながら読むことを勧める.

圧力を$p$, 密度を$\rho$, 粒子速度を$\bv$とすると,
オイラー方程式[^2]は以下のように表される.
$$\begin{aligned}
    \nabla p = -\rho \left[ \pdiff{\bv}{t} + (\bv\cdot\nabla)\bv \right].
\end{aligned}$$
また, 連続方程式は
$$\begin{aligned}
    \pdiff{\rho}{t} + \nabla\cdot(\rho\bv) = 0,
\end{aligned}$$
と表される.
さらに, 音波の伝播は熱の伝搬より圧倒的に早く, 断熱的であると仮定する[^3].
したがって, 熱力学の結果より, 音圧は密度のみの関数となり[^4],
$$\begin{aligned}
    \nabla p = c^2\nabla \rho,
\end{aligned}$$
と表される.
ここで, $c$は速度の次元を持つ, $\rho$の関数である.
例えば, 理想気体の場合は断熱方程式 
$$\begin{aligned}
    \frac{p}{\rho^\gamma} = \text{const.}
\end{aligned}$$
から
$$\begin{aligned}
    p = p_0\left(\frac{\rho}{\rho_0}\right)^\gamma
\end{aligned}$$
となる.
ここで$\gamma$は比熱比であり, 添字${}_0$は平衡状態を表す.

一般的な流体の場合は, $\rho_0$の周りでテイラー展開を行い
$$\begin{aligned}
    p     & = p_0 + \left.\pdiff{p}{\rho}\right|_{\rho_0}(\rho-\rho_0) + \frac{1}{2} \left.\pdiffs{p}{\rho}\right|_{\rho_0}(\rho-\rho_0)^2 + O((\rho-\rho_0)^3) \\
          & = p_0 + A \frac{\rho-\rho_0}{\rho_0} + \frac{B}{2} \left(\frac{\rho-\rho_0}{\rho_0}\right)^2 + O((\rho-\rho_0)^3)                                   \\
    A     & = \rho_0\left.\pdiff{p}{\rho}\right|_{\rho_0} = \rho_0 c_0^2                                                                                        \\
    B     & = \rho_0^2\left.\pdiffs{p}{\rho}\right|_{\rho_0}                                                                                                    \\
    c_0^2 & = \left.\pdiff{p}{\rho}\right|_{\rho_0}
\end{aligned}$$
と表記する.

まず, 粒子速度の大きさ$\|\bv\|$と$c_0$との比を$\epsilon$とする,
$$\begin{aligned}
    \epsilon = \frac{\|\bv\|}{c_0}.
\end{aligned}$$ この$\epsilon$を音響マッハ数と呼ぶ.
$c_0$は速度の次元を持つので音響マッハ数の次元は無次元である.

ここで, 音響マッハ数が$\epsilon \ll 1$であると仮定し[^5],
$\epsilon$で$\rho$と$\bv$を摂動展開する. すなわち $$\begin{aligned}
    \rho & = \rho_0  + \epsilon\rho_1 + \epsilon^2\rho_2 + O(\epsilon^3), \\
    \bv  & = \epsilon\bv_1 + \epsilon^2\bv_2 + O(\epsilon^3),
\end{aligned}$$ と表す[^6]. この時, $p$は, $$\begin{aligned}
    p & = p_0 + \epsilon c_0^2\rho_1 + \epsilon^2\left(c_0^2\rho_2 + \frac{1}{2}\left.\pdiffs{p}{\rho}\right|_{\rho=\rho_0}\rho_1^2\right) + O(\epsilon^3).
\end{aligned}$$ でとなる.

これらを, オイラー方程式と連続方程式に代入すると, 
$$\begin{aligned}
     & \nabla p_0 + \epsilon\left[c_0^2\nabla\rho_1 + \rho_0\pdiff{\bv_1}{t}\right] \\
     & + \epsilon^2\left[c_0^2\nabla\rho_2 + \frac{1}{2}\left.\pdiffs{p}{\rho}\right|_{\rho=\rho_0}\nabla\rho_1^2 + \rho_0 \pdiff{\bv_2}{t} + \rho_1\pdiff{\bv_1}{t} +\rho_0(\bv_1\cdot\nabla)\bv_1 \right] + O(\epsilon^3) = 0,
\end{aligned}$$
及び,
$$\begin{aligned}
    \pdiff{\rho_0}{t} + \epsilon\left[\pdiff{\rho_1}{t} + \nabla\cdot (\rho_0\bv_1) \right] + \epsilon^2\left\lbrace\pdiff{\rho_2}{t} + \nabla\cdot\left[ (\rho_0\bv_2) + (\rho_1\bv_1)\right]\right\rbrace + O(\epsilon^3) = 0,
\end{aligned}$$
となる.

これより, まず0次の式として,
$$\begin{aligned}
    \nabla p_0        & = 0, \\
    \pdiff{\rho_0}{t} & = 0,
\end{aligned}$$
を得る.
ここで, 
$$\begin{aligned}
    \nabla \rho_0 = \frac{1}{c^2(\rho_0)}\nabla p_0,
\end{aligned}$$
なので$\rho_0$が定数であることがわかる. 
したがって, 必然$p_0$も定数になる.
これらは, $_0$を平衡状態とした仮定に矛盾しない.

次に一次の式として,
$$\begin{align}
    \tag{1}c_0^2\nabla\rho_1 +\rho_0\pdiff{\bv_1}{t}  & = 0,   \\
    \pdiff{\rho_1}{t} + \rho_0\nabla\cdot\bv_1 & = 0,
\end{align}$$
を得る.
上2式より,
$$\begin{aligned}
    \nabla^2 \bv_1 &= \frac{1}{c_0^2}\pdiffs{\bv_1}{t},\\
    \nabla^2 \rho_1 &= \frac{1}{c_0^2}\pdiffs{\rho_1}{t},
\end{aligned}$$
を得る.
これらは所謂波動方程式であり, $\bv_1, \rho_1$が線形の波動現象に従うことを意味する.

最後に, 2次の式として,
$$\begin{align}
    \tag{2}c_0^2\nabla\rho_2 + \frac{1}{2}\left.\pdiffs{p}{\rho}\right|_{\rho=\rho_0}\nabla\rho_1^2 + \rho_0 \pdiff{\bv_2}{t} + \rho_1\pdiff{\bv_1}{t} +\rho_0(\bv_1\cdot\nabla)\bv_1 & = 0,\\
    \pdiff{\rho_2}{t} + \rho_0\nabla\cdot\bv_2 + \nabla\cdot(\rho_1\bv_1) = 0,
\end{align}$$
を得る.

さて, 式(1), (2)を音圧の表示にすると,
$$\begin{align}
    \tag{3}\nabla p_1 & = -\rho_0\pdiff{\bv_1}{t},\\
    \tag{4}\nabla p_2 & = - \rho_0 \pdiff{\bv_2}{t} - \rho_1\pdiff{\bv_1}{t} - \rho_0(\bv_1\cdot\nabla)\bv_1,
\end{align}$$
となる.

ここで, 渦なしの場を仮定し, 次の速度ポテンシャルを導入する.
$$\begin{aligned}
    \bv_1 & = -\nabla\phi_1, \\
    \bv_2 & = -\nabla\phi_2.
\end{aligned}$$
すると, 式(3), (4)はそれぞれ 
$$\begin{aligned}
    \nabla p_1 & = \rho_0\nabla\pdiff{\phi_1}{t},    \\
    \nabla p_2 & = \rho_0\nabla\pdiff{\phi_2}{t} + \rho_1\nabla\pdiff{\phi_1}{t} - \rho_0(\bv_1\cdot\nabla)\bv_1\\
               & = \rho_0\nabla\pdiff{\phi_2}{t} + \frac{\rho_0}{c_0^2}\pdiff{\phi_1}{t}\nabla\pdiff{\phi_1}{t} - \rho_0(\bv_1\cdot\nabla)\bv_1 \\
               & = \rho_0\nabla\pdiff{\phi_2}{t} + \frac{\rho_0}{2c_0^2}\nabla\left(\pdiff{\phi_1}{t}\right)^2 - \frac{\rho_0}{2}\nabla(\nabla\phi_1\cdot\nabla\phi_1)
\end{aligned}$$
となり,
$$\begin{aligned}
    p_1 & = \rho_0\pdiff{\phi_1}{t},                                                                                                          \\
    p_2 & = \rho_0\pdiff{\phi_2}{t} + \frac{\rho_0}{2c_0^2}\left(\pdiff{\phi_1}{t}\right)^2 - \frac{\rho_0}{2}(\nabla\phi_1\cdot\nabla\phi_1) \\
        & = \rho_0\pdiff{\phi_2}{t} + \frac{p_1^2}{2c_0^2\rho_0} - \frac{\rho_0}{2}(\nabla\phi_1\cdot\nabla\phi_1)
\end{aligned}$$
を得る.

したがって, ある物体$V$にかかる音響放射力$F$ ($=$物体にかかる力の時間平均) は, 音圧と流入運動量の2次までの項を考えると,
$$\begin{aligned}
    F & = \left\langle\int_{\partial V}\mathrm{d}{\bS}\, p_1 + p_2\right\rangle + \left\langle\int_{\partial V}\bv_1\cdot\mathrm{d}{\bS}\,\rho_0\bv_1 \right\rangle                                 \\
      & = \left\langle\int_{\partial V}\mathrm{d}{\bS}\, \rho_0\pdiff{\phi_1}{t} + \rho_0\pdiff{\phi_2}{t} + \frac{p_1^2}{2c_0^2\rho_0} - \frac{\rho_0}{2}(\nabla\phi_1\cdot\nabla\phi_1)\right\rangle + \left\langle\int_{\partial V}\bv_1\cdot\mathrm{d}{\bS}\,\rho_0\bv_1 \right\rangle
\end{aligned}$$
となる[^7].

まず, 一次の項は, 線形の波動方程式に従うので, $\langle\pdiff{\phi_1}{t}\rangle = 0$となる.
また, 定常状態では, $\bv_2 = -\nabla \phi_2$が周期的であるので, $\langle\pdiff{\bv_2}{t}\rangle = \langle\nabla\pdiff{\phi_2}{t}\rangle = 0$となり, $\langle\pdiff{\phi_2}{t}\rangle = C$は定数となる.
閉じた領域で積分すれば, これも消滅し, 
$$\begin{aligned}
    F = \left\langle\int_{\partial V}\mathrm{d}{\bS}\,\frac{p_1^2}{2c_0^2\rho_0} - \frac{\rho_0}{2}(\nabla\phi_1\cdot\nabla\phi_1)\right\rangle + \left\langle\int_{\partial V}\bv_1\cdot\mathrm{d}{\bS}\,\rho_0\bv_1 \right\rangle
\end{aligned}$$
となる.

一般の場合, ある物体$V$にかかる音響放射力$F$は上記の式で与えられる.
しかし, これを計算するのは容易ではない.
まず, 物体表面$\partial V$が音響放射圧それ自体などにより変動する可能性がある.
また, 速度ポテンシャル$\phi_1, \phi_2$や (一次の) 音圧$p_1$などは反射波のそれを含む.
一般の場合にこれらを求めるのは難しい.

## 無限剛壁と平面波の場合

ここでは, $x=0$に置かれた無限剛壁に平面波が入射する場合を考えてみよう.

音響放射力の剛壁に垂直な方向の成分$F_x$は, $$\begin{aligned}
    F_x & = \left.\left\langle\int_{\partial V}\mathrm{d}{S}\, \frac{p_1^2}{2c_0^2\rho_0} - \frac{\rho_0}{2}(\nabla\phi_1\cdot\nabla\phi_1) + \rho_0 v_{1x}^2 \right\rangle\right|_{x=0} \\
        & =\int_{\partial V}\mathrm{d}{S}\,\left.\left\langle\frac{p_1^2}{2c_0^2\rho_0} - \frac{\rho_0}{2}(\nabla\phi_1\cdot\nabla\phi_1) + \rho_0 v_{1x}^2 \right\rangle\right|_{x=0}
\end{aligned}$$ となる. この被被積分項を音響放射圧$P$と呼ぶ[^8].

波が角度$\theta$で壁に入射するとし $$\begin{aligned}
    \phi_1   & = \phi_i + \phi_r,                            \\
    \phi_i   & = \phi_0\cos \tau_+,                          \\
    \phi_r   & = R\phi_0\cos (\tau_- + \delta),              \\
    \tau_\pm & = k(\pm x\cos\theta + y\sin\theta) - \omega t
\end{aligned}$$ とする. ここで, $R$は反射率で,
$\delta$は反射波の位相である.

この時, $$\begin{aligned}
    p_1   & = \rho_0 \pdiff{\phi_1}{t}                                                                                               \\
          & = -\rho_0\omega\phi_0\sin\tau_+ - R\rho_0\omega\phi_0\sin(\tau_- + \delta),                                              \\
    \bv_1 & = -\nabla \phi_1 = -k \phi_0\sin\tau_+(\cos\theta, \sin\theta) - Rk\phi_0\sin(\tau_- + \delta)(-\cos\theta, \sin\theta), \\
    c_0k  & = \omega,
\end{aligned}$$ より, $$\begin{aligned}
    P & = \rho_0k^2\phi_0^2 \cos^2\theta  \left.\left\langle \sin^2\tau_+ + R^2 \sin^2(\tau_- +\delta) \right\rangle\right|_{x=0} \\
      & = \frac{1}{2}(1+R^2)\rho_0k^2\phi_0^2 \cos^2\theta
\end{aligned}$$ となる.

なお, $$\begin{aligned}
    \left.\left\langle p_i^2 \right\rangle\right|_{x=0} = \frac{1}{2}\rho_0^2\omega^2\phi_0^2 =  \frac{1}{2}\rho_0^2c_0^2k^2\phi_0^2
\end{aligned}$$ なので, $$\begin{aligned}
    P & = (1+R^2)\frac{p^2}{\rho_0c_0^2}\cos^2\theta
\end{aligned}$$ と表すことができる. ここで,
$p^2 = \left.\left\langle p_i^2 \right\rangle\right|_{x=0}$は入射波の音圧の二乗平均である.

[^saneyoshi_ultrasound_1978]: 実吉純一, "超音波技術便覧", 日刊工業新聞社, 1978.

[^hasegawa1996_jp]: 長谷川高陽, "ランジュバン放射圧に関する統一理論", 日本音響学会誌, 1996.

[^eckart1948vortices]: Eckart, Carl. "Vortices and streams caused by sound waves." Physical review 73.1 (1948): 68.

[^awatani1955studies]: Awatani, Jobu. "Studies on acoustic radiation pressure. I.(General considerations)." The Journal of the Acoustical Society of America 27.2 (1955): 278-281.

[^hasegawa2000general]: Hasegawa, Takahi, et al. "A general theory of Rayleigh and Langevin radiation pressures." Acoustical Science and Technology 21.3 (2000): 145-152.

[^2]: 粘性なしのナビエ･ストークス方程式. また,
    ここでは外力場も考えていない.

[^3]: 別の言い方をすると等エントロピーを仮定する.

[^4]: このような流体をバロトロピー流体 (barotropic fluid) と呼ぶ.

[^5]: この仮定の妥当性は後に示される.

[^6]: $|\bv| = O(\epsilon)$なので, $\bv_0$は存在しない.

[^7]: $p_0$は大気圧にあたり, これによる力は音響放射力とは呼ばない. なお, 定数なのでそもそも閉じた領域で積分すれば消滅する.

[^8]: 方向によるので正確には圧力ではない.
