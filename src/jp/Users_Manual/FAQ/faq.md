# FAQ

<details><summary><code class="hljs">STATUS_DLL_NOT_FOUND</code>または<code class="hljs">FileNotFoundError: (or one of its dependencies)</code>というエラーがでる</summary>

- [npcap](https://nmap.org/npcap/)を「**WinPcap API compatible mode**」でインストールする

</details>

<details><summary><code class="hljs">Not supported tag</code>というエラーがでる</summary>

- [ファームウェアがサポートされていない](../release_notes.md)

</details>

<details><summary><code class="hljs">Failed to confirm the response from the device</code>というエラーがでる</summary>

- [デフォルトより長いTimeoutを指定する](../API/controller.md#sender)

</details>

<details><summary><code class="hljs">Failed to synchronize devices. Maximum system time difference exceeded the tolerance</code>というエラーがでる</summary>

- `sync_timeout`か`sync_tolerance`の値を増やす. ただし, 後者の変更は推奨されない.

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
  1. 上記条件を満たすように[`Silencer`を弱める](../API/silencer.md#fixed-completion-time-mode), または, [`Silencer`を無効化する](../API/silencer.md#silencerの設定)
  1. [Fixed update rateモード](../API/silencer.md#fixed-update-rate-mode)を使用する
  1. [strict](../API/silencer.md#fixed-completion-time-modeの設定)を`false`にする

</details>

<details><summary>振動子の位相/振幅データにアクセスするには?</summary>

1. [`Controller::inspect`](../API/controller.md#inspect-rustのみ)を使用する.
1. 自分で所望の`Gain`を作成する. [Gainの自作](../advanced/custom_gain.md)を参照.

</details>

<details><summary>AM変調データにアクセスするには?</summary>

1. [`Controller::inspect`](../API/controller.md#inspect-rustのみ)を使用する.
1. 自分で所望の`Modulation`を作成する. [Modulationの自作](../advanced/custom_modulation.md)を参照.

</details>

## その他

- 質問やバグ報告は[GithubのIssue](https://github.com/shinolab/autd3/issues)へお気軽にどうぞ
