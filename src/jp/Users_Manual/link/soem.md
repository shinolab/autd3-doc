# SOEM

[SOEM](https://github.com/OpenEtherCATsociety/SOEM)は有志が開発しているオープンソースのEherCAT Masterライブラリである.
TwinCATとは異なり通常のWindows上で動作するためリアルタイム性は保証されない.
そのため, 基本的にTwinCATを使用することを推奨する.
SOEMを使用するのはやむを得ない理由があるか, 開発時のみに限定するべきである.
一方, SOEMはクロスプラットフォームで動作し, インストールも単純という利点がある.

Windowsの場合は, [npcap](https://nmap.org/npcap/)を「**WinPcap API compatible mode**」でインストールしておくこと.
Linux/macOSの場合は, 特に準備は必要ない.

[[_TOC_]]

## SOEMリンクのAPI

SOEMリンクで指定できるオプションは以下の通りである.

```rust,should_panic,edition2021
{{#include ../../../codes/Users_Manual/link/soem_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/link/soem_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/link/soem_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/link/soem_0.py}}
```

- `ifname`: ネットワークインタフェース名. デフォルトでは空白であり, 空白の場合はAUTD3デバイスが接続されているネットワークインタフェースを自動的に選択する.
- `buf_size`: 送信キューバッファサイズ. 通常は変更する必要はない.
- `err_handler`: 何らかのエラーが発生したときのコールバック. コールバック関数はエラーが発生したデバイスインデックス, エラーの種類を引数に取る.
- `state_check_interval`: エラーが出ているかどうかを確認する間隔. デフォルトは$\SI{100}{ms}$.
- `sync0_cycle`: 同期信号の周期. デフォルトは2 (単位は$\SI{500}{us}$).
- `send_cycle`: 送信サイクル. デフォルトは2 (単位は$\SI{500}{us}$).
    - `SOEM`も大量のデバイスを接続すると挙動が不安定になる場合がある[^fn_soem]. このときは, `sync0_cycle`と`send_cycle`の値を増やす. これら値はエラーが出ない中で, 可能な限り小さな値が望ましい. デフォルトは2であり, どの程度の値にすべきかは接続している台数に依存する. 例えば, 9台の場合は3, 4程度の値にしておけば動作するはずである.
- `timer_strategy`: タイマーの戦略. デフォルトは`Sleep`である.
    - `Sleep`       : 標準ライブラリのsleepを用いる
    - `BusyWait`    : ビジーウェイトを用いる. 高解像度だが, CPU負荷が高い.
- `sync_tolerance`: 同期許容レベル. 初期化時, 各デバイスのシステム時間差がこの値以下になるまで待機する. 以下のタイムアウト時間が経過しても同期が完了しない場合はエラーとなる. デフォルトは$\SI{1}{us}$であり, 変えることは推奨されない.
- `sync_timeout`: 同期タイムアウト. 上記のシステム時間差測定のタイムアウト時間. デフォルトは$\SI{10}{s}$.
- `thread_priority`: スレッドの優先度. デフォルトは`ThreadPriority::MAX`である.
- `process_priority`: (Windowsのみ) プロセスの優先度. デフォルトは`ProcessPriority::High`である.

# RemoteSOEM

このLinkは`SOEM`を動かすサーバーPCとユーザプログラムを動かすクライアントPCを分離するためのものである.

`RemoteSOEM`を使用する場合はPCを2台用意する必要がある.
この時, 片方のPCは`SOEM` linkが使えるである必要がある.
このPCをここでは"サーバ"と呼ぶ.
一方, 開発側のPC, 即ちSDKを使用する側は特に制約はなく, サーバと同じLANに繋がっていれば良い, こちらをここでは"クライアント"と呼ぶ.

まず, サーバとAUTDデバイスを接続する.
また, サーバとクライアントを別のLANで繋ぐ[^fn_remote_soem].
そして, サーバとクライアント間のLANのIPを確認しておく.
ここでは例えば, サーバ側が`172.16.99.104`, クライアント側が`172.16.99.62`だったとする.

## AUTD Server

`RemoteSOEM`を使用する場合, サーバに`AUTD Server`をインストールする必要がある.
[GitHub Releases](https://github.com/shinolab/autd3-server/releases)にてインストーラを配布しているので, これをダウンロードし, 指示に従ってインストールする.

`AUTD Server`を実行すると, 以下のような画面になるので, `SOEM`タブを開く.

<figure>
  <img src="../../fig/Users_Manual/autdserver_remotesoem.jpg"/>
</figure>

ポートに適当なポート番号を指定し, `Run`ボタンを押す.

AUTD3デバイスが見つかり, クライアントとの接続待ちである旨のメッセージが表示されれば成功である.

なお, `AUTD Server`では`SOEM`と同等のオプションを指定できる.

## RemoteSOEMリンクのAPI

`RemoteSOEM`のコンストラクタでは, <サーバのIP:ポート>を指定する.

```rust,should_panic,edition2021
{{#include ../../../codes/Users_Manual/link/remote_soem_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/link/remote_soem_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/link/remote_soem_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/link/remote_soem_0.py}}
```

## ファイアウォール

TCP関係のエラーが出る場合は, ファイアウォールでブロックされている可能性がある.
その場合は, ファイアウォールの設定でTCP/UDPの指定したポートの接続を許可する.

[^fn_soem]: TwinCATよりは緩く, 普通に動くこともある.

[^fn_remote_soem]: 無線LANでも可
