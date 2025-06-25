# 開発環境構築

FPGAの開発にはVivado 2025.1を使用している.
ML Editionは無料 (要登録) なので各自インストールされたい.
インストール時にDesign Toolsの"Vivado"とDeviceの"Artix-7", 及び, Cable Drivesをインストールすること.
Vitisは必要ない.

Vivadoのプロジェクトを生成するには, 以下のようにする.
```ignore
git clone https://github.com/shinolab/autd3-firmware.git
cd autd3-firmware/src/fpga
cargo make build
```
これで, `autd3-fpga.xpr`ファイルが生成されるはずなので, これをVivadoで開けば良い.

VivadoのGUI操作でビットストリームファイルを作成できる.
ビットストリームファイル (.bit) からコンフィグレーションファイル (.mcs) を生成し, FPGAに書き込むには, 「Tools」→「Run Tcl Script...」で`configuration.tcl`を実行すれば良い.

> `vivado`コマンドやtclコマンドの使い方はXilinxのUser's Guide ([UG835](https://docs.amd.com/r/en-US/ug835-vivado-tcl-commands), [UG910](https://docs.amd.com/r/en-US/ug910-vivado-getting-started)) を参照されたい.
