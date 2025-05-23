### 依存プログラムのインストール

本チュートリアルでは[CMake](https://cmake.org/)を使用するので, インストールしておくこと.
また, 依存ライブラリのダウンロードに`git`を使用するので, これもインストールしておくこと.

### AUTD3クライアントプログラムの作成

まず, ターミナルを開き, 適当なディレクトリを用意する.

```shell
mkdir autd3-sample
cd autd3-sample
```

次に, `autd3-sample`以下に`CMakeLists.txt`, `main.cpp`ファイルを作成する.

```shell,name=
└─autd3-sample
        CMakeLists.txt
        main.cpp
```

次に, `CMakeLists.txt`を以下のようにする.

```cpp,name=CMakeLists.txt
{{#include ../../../codes/Users_Manual/Tutorial/single/CMakeLists.txt}}
```

> NOTE: 上記の例では, 依存ライブラリ (Eigen3) を自動的にダウンロードするようになっている.
> すでにEigen3がインストールされている場合, `USE_SYSTEM_EIGEN`をONにすると, 自動ダウンロードを無効化し, インストール済みのものを使用できる.

また, `main.cpp`を以下のようにする. これは単一焦点に$\SI{150}{Hz}$のAM変調をかける場合のソースコードである.

```cpp,name=main.cpp
{{#include ../../../codes/Users_Manual/Tutorial/single/main.cpp}}
```

次に, CMakeでビルドする.

```shell
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . --config Release
```

これで, 実行ファイルが生成されるので, これを実行する.

```shell,filename=Windows
.\Release\main.exe
```

```shell,filename=Linux/macOS
sudo ./main
```

### トラブルシューティング

- anaconda (miniconda) がactivateされている場合に, ビルドエラーになる可能性がある.
  - この場合, `build`ディレクトリを削除し, `conda deactivate`を実行したのち再び`cmake`を実行する.
