# コンセプト

SDKを構成する主なコンポーネントは以下の通りである.

* `Controller` - AUTD3デバイスに対する全ての操作はこれを介して行う.
* `Geometry` - `Device`のコンテナ.
  * `Device` - AUTD3デバイスに対応する. デバイスが現実世界でどのように配置されているかを管理する. `Transducer`のコンテナ.
  * `Transducer` - 振動子に対応する. 振動子が現実世界でどこにあるかを管理する.
* `Link` - デバイスとのインターフェース.
* `Gain` - 各振動子の位相/振幅を管理する.
* `STM` - Spatio-Temporal Modulation (STM, 時空間変調) 機能を提供する. 各振動子の位相/振幅データの時間列を管理する.
* `Modulation` - AM変調機能を提供するする. 変調データの時間列を管理する.
* `Silencer` - 静音化処理を管理する.

ソフトウェアの使用方法は以下の通りである.

まず, 現実世界のAUTD3デバイスの配置を指定し, どの`Link`を使用するかを決め, `Controller`を開く.
次に, `Controller`を介して, `Gain` (または`STM`), `Modulation`, `Silencer`データをデバイスに送信する.

送信されたデータに基づいたPWM信号が振動子に印加される.
信号が生成されるまでの流れは以下の図の通りである.

<figure>
  <a href="../../fig/Users_Manual/concept.svg" data-lightbox="image"><img src="../../fig/Users_Manual/concept.svg"/></a>
  <figcaption>信号が生成されるまでの概念図</figcaption>
</figure>

`Gain`/`STM`で指定された振幅データは, `Modulation`で指定された変調データと順次掛け合わされた後, `Silencer`に渡される.
`Gain`/`STM`で指定された位相データは, そのまま`Silencer`に渡される.
`Silencer`は, これらのデータを静音化処理[^silencer]する.
最後に, `Silencer`で処理された振幅/位相データに基づきPWM信号が生成され, 振動子に印加される. 

なお, 振幅/位相データ, 及び, 変調データはすべて$\SI{8}{bit}$である.

[^silencer]: 詳細は[Silencer](./API/silencer.md)を参照.
