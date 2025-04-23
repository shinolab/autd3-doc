# TwinCAT

TwinCATはPCでEherCATを使用する際の唯一の公式の方法である.
TwinCATはWindowsのみをサポートする非常に特殊なソフトウェアであり, Windowsを半ば強引にリアルタイム化する.

また, 特定のネットワークコントローラが求められるため,
[対応するネットワークコントローラの一覧](https://infosys.beckhoff.com/english.php?content=../content/1033/tc3_overview/9309844363.html&id=)を確認すること.

> Note: 或いは, TwinCATのインストール後に, `C:/TwinCAT/3.1/Driver/System/TcI8254x.inf`に対応するデバイスのVendor IDとDevice IDが書かれているので,「デバイスマネージャー」→「イーサネットアダプタ」→「プロパティ」→「詳細」→「ハードウェアID」と照らし合わせることでも確認できる.

上記以外のネットワークコントローラでも動作する場合があるが, その場合, 正常な動作とリアルタイム性は保証されない.

[[_TOC_]]

## 事前準備

前提として, TwinCATはHyper-VやVirtual Machine Platformと共存できない.
そのため, これらの機能を無効にする必要がある.
これには, 例えば, PowerShellを管理者権限で起動し,

```PowerShell
Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Hypervisor
Disable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
```

と打ち込めば良い.

また, Windows 11の場合, 仮想化ベースのセキュリティ機能もオフにする必要がある.
「Windows セキュリティ」→ 「デバイス セキュリティ」→「コア分離」→「メモリ整合性」をオフにする.
Windows 11 24H2から, レジストリで`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceGuard\EnableVirtualizationBasedSecurity`の値を0にする必要もあるかもしれない.

### TwinCATのインストール

[公式サイト](https://infosys.beckhoff.com/content/1033/tc3_installation/15698617995.html?id=7523796010185393366)を参照し, TwinCAT 3.1 Build 4026をインストールする.
(インストールにはmyBeckhoffアカウントの登録 (無料) が必要になる.)
TwinCAT Xae Shellは64bit版をインストールすること.
Visual Studio Integrationは不要.

Package Managerのインストール後, Package Managerで「TwinCAT Standard」のインストールを行えば良い.

### AUTD3 Serverのインストール

TwinCATのLinkを使うには, まず, `AUTD3 Server`をインストールする必要がある.
[GitHub](https://github.com/shinolab/autd3-server)にてインストーラを配布しているので, これをダウンロードし, 指示に従ってインストールする.

> NOTE: 必ず, 使用するソフトウェアのバージョンに合わせた`AUTD Server`を使用すること.

> NOTE: [CLI版](https://github.com/shinolab/TwinCATAUTDServer/releases)もある.

`AUTD3 Server`を実行すると, 以下のような画面になるので, `TwinCAT`タブを開く.

<figure>
  <img src="../../../fig/Users_Manual/autdserver_twincat.jpg"/>
</figure>

### 初回の追加作業

初回のみ, 以下の作業が必要になる.

まず, `AUTD3 Server`を管理者として開き, `TwinCAT`タブから「Copy AUTD.xml」ボタンを押す.
ここで, 「AUTD.xml is successfully copied」のようなメッセージが出れば成功である.

次に, 「Open XAE Shell」ボタンを押し, XAE Shellを開く.
TwinCAT XAE Shell上部メニューから「TwinCAT」→「Show Realtime Ethernet Compatible Devices」を開き「Compatible devices」の中の対応デバイスを選択し, Installをクリックする.
「Installed and ready to use devices (realtime capable)」にインストールされたアダプタが表示されていれば成功である.

なお,「Compatible devices」に何も表示されていない場合はそのPCのイーサネットデバイスはTwinCATに対応していない.
「Incompatible devices」の中のドライバもインストール自体は可能で, インストールすると「Installed and ready to use devices (for demo use only)」と表示される.
この場合, 使用できるが動作保証はない.

### AUTD Serverの実行

AUTD3とPCを接続し, AUTD3の電源が入った状態で, 「Run」ボタンを押す.
このとき, 「Client IP address」の欄は空白にしておくこと.

下の画面のように, AUTD3デバイスが見つかった旨のメッセージが出れば成功である.

<figure>
  <img src="../../../fig/Users_Manual/autdserver_twincat_run.jpg"/>
</figure>

なお, TwinCATはPCの電源を切る, スリープモードに入る等で接続が途切れるので, その都度実行し直すこと.

### ライセンス

初回はライセンス関係のエラーが出るので, XAE Shellで「Solution Explorer」→「SYSTEM」→「License」を開き, 「7 Days Trial License ...」をクリックし, 画面に表示される文字を入力する.
なお, ライセンスは7日間限定のトライアルライセンスだが, 切れたら再び同じ作業を行うことで再発行できる.
ライセンスを発行し終わったら, "TwinCAT XAE Shell"を閉じて, 再び実行する.

## TwinCATリンク

### Install

{{ #tabs }}
{{ #tab name=Rust }}
```shell
cargo add autd3-link-twincat
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp,name=CMakeLists.txt
target_link_libraries(<TARGET> PRIVATE autd3::link::twincat)
```
{{ #endtab }}
{{ #tab name=C# }}
メインライブラリに含まれている.
{{ #endtab }}
{{ #tab name=Unity }}
メインライブラリに含まれている.
{{ #endtab }}
{{ #tab name=Python }}
メインライブラリに含まれている.
{{ #endtab }}
{{ #endtabs }}

### APIs

{{ #tabs }}
{{ #tab name=Rust }}
```rust
{{#include ../../../../codes/Users_Manual/link/twincat_0.rs}}
```
{{ #endtab }}
{{ #tab name=C++ }}
```cpp
{{#include ../../../../codes/Users_Manual/link/twincat_0.cpp}}
```
{{ #endtab }}
{{ #tab name=C# }}
```cs
{{#include ../../../../codes/Users_Manual/link/twincat_0.cs}}
```
{{ #endtab }}
{{ #tab name=Python }}
```python
{{#include ../../../../codes/Users_Manual/link/twincat_0.py}}
```
{{ #endtab }}
{{ #endtabs }}

### トラブルシューティング

大量のデバイスを使用しようとすると, 下の図のようなエラーが発生することがある.

<figure>
  <img src="../../../fig/Users_Manual/tcerror.jpg"/>
  <figcaption>9台のAUTD3デバイスを使用した際のTwinCATエラー</figcaption>
</figure>

この場合は, `AUTD3 Server`の`Sync0 cycle time`と`Send task cycle time`の値を増やし, AUTD Serverを再び実行する.
これらのオプションの値はデフォルトでそれぞれ$\SI{1}{ms}$になっている.

どの程度の値にすればいいかは接続する台数による.
エラーが出ない中で可能な限り小さな値が望ましい.
例えば, 9台の場合は$1.5$--$\SI{2}{ms}$程度の値にしておけば動作するはずである.
