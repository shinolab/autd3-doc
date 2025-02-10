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

なお, ファームウェアが古い場合, 正常な動作は保証されない.
本文章におけるファームウェアのバージョンはv10.0.1が想定される.
ファームウェアのアップデートは[セットアップ/ファームウェア](./setup/firmware.md)を参照されたい.

## 各言語ごとのサンプルプログラム

- [Rust](./getting_started/rust.md)
- [C++](./getting_started/cpp.md)
- [C#](./getting_started/cs.md)
- [Python](./getting_started/python.md)
