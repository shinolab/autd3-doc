# FAQ

<details><summary><code class="hljs">STATUS_DLL_NOT_FOUND</code>または<code class="hljs">FileNotFoundError: autd3capi_link_soem.dll (or one of its dependencies)</code>というエラーがでる</summary>

- [npcap](https://nmap.org/npcap/)を「**WinPcap API compatible mode**」でインストールする

</details>

<details><summary><code class="hljs">TcAdsDll not found</code>というエラーがでる</summary>

- TwinCAT 3 Build 4026以降をインストールする

</details>

<details><summary><code class="hljs">No AUTD3 devices found</code>と表示される</summary>

- macOS, linuxで`SOEM`リンクを使用する場合, root権限が必要

   - linuxの場合, `setcap`コマンドで以下の権限を設定することで回避することもできる
   
      ```shell
      sudo setcap cap_net_raw,cap_net_admin=eip <your executable file>
      ```

   - macOSの場合, `/dev/bpf*`ファイルに読み取り権限を追加することで回避することもできる
   
      ```shell
      sudo chmod +r /dev/bpf*
      ```

- (Windows) 最新のnpcapを使用する

- WSL等の仮想マシンは対応していない
   - VirtualBoxなどで動く場合があるが, 挙動は不安定になる

</details>

<details><summary><code class="hljs">One ore more slaves are not responding</code>, または, <code class="hljs">Slow network was detected</code>と表示される</summary>

- デバイスドライバを更新する

- (Windows) 最新のnpcapを使用する

- `send_cycle`と`sync0_cycle`の値を増やす

- (Windows) デバイスマネージャーの当該ネットワークアダプタのプロパティから, 「電源の管理」タブで「電力の節約のために、コンピューターでこのデバイスの電源をオフにできるようにする」のチェックを外す

</details>

<details><summary><code class="hljs">Not supported tag</code>というエラーがでる</summary>

- [ファームウェアがサポートされていない](../release_notes.md)

</details>

<details><summary><code class="hljs">Failed to confirm the response from the device</code>というエラーがでる</summary>

- [デフォルトより長いTimeoutを指定する](../API/controller.md#sender)

</details>

<details><summary><code class="hljs">Failed to synchronize devices. Maximum system time difference exceeded the tolerance</code>というエラーがでる</summary>

- [`sync_timeout`か`sync_tolerance`](../API/link/soem.md#apis)の値を増やす. ただし, 後者の変更は推奨されない.

</details>

<details><summary><code class="hljs">SOEM</code>リンク使用時に送信が頻繁に失敗する</summary>

- この問題は
   * `sync_mode`を`DC`にしている

   かつ,

   * オンボードのethernetインターフェースを使用している

  かつ, 以下のいずれかの状況で発生することが確認されている

   * RealSense, Azure Kinect, Webカメラ等を使用する
      * 基本的にカメラをアクティブにした時点で発生
   * 動画や音声を再生する
      * または, インターネットブラウザで動画サイト (Youtube等) を開く
   * Unityを使用する
      * 起動するだけで発生
   * Blenderでアニメーションを再生する
      * その他の操作 (モデリング等) は問題ない

- この問題の回避策としては, 以下のいずれかを試されたい
  1. `TwinCAT`, `RemoteTwinCAT`, または, `RemoteSOEM`リンクを使用する
  1. `sync_mode`を`FreeRun`にする
  1. Linuxやmacを使用する.
     - ただし, 仮想マシンはNG
  1. USB to Ethernetアダプターを使用する
     - 少なくとも「ASIX AX88179」のチップを採用しているもので正常に動作することが確認されている
     - なお, オンボードではなくとも, PCIe接続のethernetアダプターでも同様の問題が発生する

- 上記以外の状況でも発生した, 或いは, 上記状況でも発生しなかった等の報告があれば, GitHubのIssueに積極的に報告していただけると幸いである.

</details>

<details><summary>リンクが頻繁に切れる</summary>

- 超音波の出力時にこれが頻発する場合は, 電力が足りているかを確認すること
   - デバイス一台で最大50W消費する

</details>

<details><summary>TwinCAT 3上で<code class="hljs">abnormal state change</code>, <code class="hljs">Synchronization error</code>のようなエラーがでる</summary>

- `Sync0 cycle`と`Send task cycle`の値を増やし, TwinCAT 3を再起動する

</details>

<details><summary><code class="hljs">RemoteTwinCAT</code>リンク使用時にエラーが出る</summary>

- ファイアウォールでブロックされている可能性があるため, ファイアウォールを切るか, TCP/UDPの48898番ポートを開ける.
- クライアントPCのサーバー以外とのLANをすべて切断する.

</details>


<details><summary><code class="hljs">Silencer cannot complete phase/intensity interpolation in the specified sampling period</code>というエラーがでる</summary>

- [`Silencer`のこの条件](../API/silencer.md#fixed-completion-time-modeの注意点)を満たしていない. 以下のいずれかの方法で修正できる. (おすすめは上から順に)
  1. AM変調/STMのサンプリングレートをおとす
  1. [`Silencer`を無効化する](../API/silencer.md#silencerの設定)
  1. [Fixed update rateモード](../API/silencer.md#fixed-update-rate-mode)を使用する
  1. [strict_mode](../API/silencer.md#fixed-completion-time-modeの設定)を`false`にする

</details>

<details><summary>振動子の位相/振幅データにアクセスするには?</summary>

1. 自分で所望の`Gain`を作成する. [Gainの自作](../advanced/custom_gain.md)を参照.

</details>

<details><summary>AM変調データにアクセスするには?</summary>

1. 自分で所望の`Modulation`を作成する. [Modulationの自作](../advanced/custom_modulation.md)を参照.

</details>

## その他

- 質問やバグ報告は[GithubのIssue](https://github.com/shinolab/autd3/issues)へお気軽にどうぞ
