# 単一デバイスの駆動

ここでは, 一つのデバイスを駆動する方法について説明する.

## 依存プログラムのインストール

本チュートリアルでは[SOEM](https://github.com/OpenEtherCATsociety/SOEM)を利用する.
Windowsを使用する場合, [Npcap](https://npcap.com/)を「**WinPcap API-compatible Mode**」でインストールしておくこと.

なお, ファームウェアが古い場合, 正常な動作は保証されない.
本文章におけるファームウェアのバージョンはv10.0.1が想定される.
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
