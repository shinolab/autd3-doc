### Installing Dependencies

This tutorial uses [CMake](https://cmake.org/), so make sure it is installed.

### Creating an AUTD3 Client Program

First, open a terminal and prepare an appropriate directory.

```shell
mkdir autd3-sample
cd autd3-sample
```

Next, create `CMakeLists.txt` and `main.cpp` files under `autd3-sample`.

```shell,name=
└─autd3-sample
        CMakeLists.txt
        main.cpp
```

Next, edit `CMakeLists.txt` as follows.

```ignore,name=CMakeLists.txt
{{#include ../../../codes/Users_Manual/Tutorial/single/CMakeLists.txt}}
```

> NOTE: In the above example, the dependency library (Eigen3) is automatically downloaded.
> If Eigen3 is already installed, you can disable the automatic download by turning on `USE_SYSTEM_EIGEN` and use the installed one.

Also, edit `main.cpp` as follows. This is the source code for applying AM modulation of $\SI{150}{Hz}$ to a single focal point.

```cpp,name=main.cpp
{{#include ../../../codes/Users_Manual/Tutorial/single/main.cpp}}
```

Next, build with CMake.

```shell
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . --config Release
```

This will generate an executable file, so run it.

```shell,filename=Windows
.\Release\main.exe
```

```shell,filename=Linux/macOS
sudo ./main
```

### Troubleshooting

- There may be build errors if anaconda (miniconda) is activated.
  - In this case, delete the `build` directory, run `conda deactivate`, and then run `cmake` again.
