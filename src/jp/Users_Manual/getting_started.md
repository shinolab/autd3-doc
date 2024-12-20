# チュートリアル

ここでは, 実際にAUTD3を動かす手順について述べる.

## 依存プログラムのインストール

本チュートリアルでは[SOEM](https://github.com/OpenEtherCATsociety/SOEM)を利用する.
Windowsを使用する場合, [Npcap](https://npcap.com/)を「**WinPcap API-compatible Mode**」でインストールしておくこと.

## デバイスのセットアップ

まず, デバイスをセットアップする.
ここでは一台のAUTD3のみを使うこととする.
PCのイーサネットポートとAUTD3デバイスのEtherCAT In ([Concept](concept.md)参照) をイーサネットケーブルで接続する.
次に, $\SI{24}{V}$直流電源を接続する.

### ファームウェアアップデート

ファームウェアが古い場合, 正常な動作は保証されない.
本文章におけるファームウェアのバージョンはv10.0.1が想定される.

ファームウェアのアップデートには[Vivado](https://www.xilinx.com/products/design-tools/vivado.html), 及び, [J-Link Software](https://www.segger.com/downloads/jlink/)をインストールしたWindows 10/11 64bit PCが必要である.
なお, Vivado 2024.1, 及び, J-Link Software v8.10での動作を確認している.

> NOTE: 古いJ-Linkを使用する場合, "**Install legacy USB Driver for J-Link (requires admin rights)**"にチェックを入れること.
> 例えば, J-Link Plusの場合, V10以前はlegacy USB Driverが必要になる. (バージョンはJ-Link Plusデバイスの背面に書かれている.)
> 詳しくは[Segger Wiki](https://wiki.segger.com/J-Link_Model_Overview)を参照されたい. 使用しているデバイスにWinUSB featureがあれば, legacy USB Driverは不要.

> NOTE: ファームウェアのアップデートだけが目的であれば, "Vivado Lab Edition"の使用を強く推奨する. 
> ML Edition はインストールに60 GB以上のディスク容量を要求する. Lab Edition は6 GB程度のディスク容量で済む. 

まず, AUTD3デバイスとPCを[XILINX Platform Cable](https://www.xilinx.com/products/boards-and-kits/hw-usb-ii-g.html), 及び, [J-Link 9-Pin Cortex-M Adapter](https://www.segger-pocjapan.com/j-link-9-pin-cortex-m-adapter)付きの[J-Link Plus](https://www.segger.com/products/debug-probes/j-link/models/j-link-plus/)で接続し, AUTD3の電源を入れる.
次に, [autd3-firmware](https://github.com/shinolab/autd3-firmware)内の`autd_firmware_writer.ps1`をpowershellから実行し, 指示に従えばよい. updateには数分の時間を要する.

<figure>
    <img src="../fig/Users_Manual/cable.jpg"/>
    <figcaption>ファームウェアアップデート用ケーブル接続先</figcaption>
</figure>

## 各言語ごとのサンプルプログラム

- [Rust](./getting_started/rust.md)
- [C++](./getting_started/cpp.md)
- [C#](./getting_started/cs.md)
    - [Unity](./getting_started/unity.md)
- [Python](./getting_started/python.md)
