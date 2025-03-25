# 単一デバイスの駆動

ここでは, 一つのデバイスを駆動する方法について説明する.

## 依存プログラムのインストール

本チュートリアルでは[SOEM](https://github.com/OpenEtherCATsociety/SOEM)を利用する.
Windowsを使用する場合, [Npcap](https://npcap.com/)を「**WinPcap API-compatible Mode**」でインストールしておくこと.

なお, ファームウェアが古い場合, 正常な動作は保証されない.
本文章におけるファームウェアのバージョンはv11.0.0, または, v10.0.1[^1]が想定される.
ファームウェアのアップデートは[はじめに/ファームウェア](../getting_started/firmware.md)を参照されたい.

## サンプルコード

{{ #tabs }}
{{ #tab name=Rust }}
{{#include rust.md}}
{{ #endtab }}
{{ #tab name=C++ }}
{{#include cpp.md}}
{{ #endtab }}
{{ #tab name=C# }}
{{#include cs.md}}
{{ #endtab }}
{{ #tab name=Python }}
{{#include python.md}}
{{ #endtab }}
{{ #endtabs }}

[^1]: 一部機能は未サポート. 詳細は[Firmware v10 vs v11](./../firmware_v10_vs_v11.md)を参照.
