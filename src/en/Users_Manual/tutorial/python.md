### Installing the pyautd3 Library

First, install the `pyautd3` and `pyautd3_link_soem` libraries via pip.

```shell
pip install pyautd3
pip install pyautd3_link_soem
```

Next, create `main.py` and edit it as follows.
This is the source code for applying AM modulation of $\SI{150}{Hz}$ to a single focal point.

```python,name=main.py
{{#include ../../../codes/Users_Manual/Tutorial/single/main.py}}
```

Then, run it.

```shell
python main.py
```

### Notes for Linux Users

On Linux, administrator privileges are required to use SOEM.
In that case, run:
```shell
sudo setcap cap_net_raw,cap_net_admin=eip <your python path>
```
Then, run `main.py`.
```shell
python main.py
```

### Notes for macOS Users

On macOS, administrator privileges are required to use SOEM.
In that case, run:
```shell
sudo chmod +r /dev/bpf*
```
Then, run `main.py`.
```shell
python main.py
```
