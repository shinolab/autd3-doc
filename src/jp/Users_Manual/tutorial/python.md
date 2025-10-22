### pyautd3ライブラリのインストール

```shell
pip install pyautd3
pip install pyautd3_link_ethercrab
```

次に, `main.py`を作成し, 以下のようにする.
これは単一焦点に$\SI{150}{Hz}$のAM変調をかける場合のソースコードである.

```python,name=main.py
{{#include ../../../codes/Users_Manual/Tutorial/single/main.py}}
```

そして, これを実行する.

```shell
python main.py
```

### Linux使用時の注意

Linuxでは, 管理者権限が必要になる場合がある.
その場合は, 
```shell
sudo setcap cap_net_raw,cap_net_admin=eip <your python path>
```
とした後, `main.py`を実行する.
```shell
python main.py
```

### macOS使用時の注意

macOSでは, 管理者権限が必要になる場合がある.
その場合は, 
```shell
sudo chmod +r /dev/bpf*
```
とした後, `main.py`を実行する.
```shell
python main.py
```
