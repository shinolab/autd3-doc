# ソフトウェア

基本的に各言語の標準的なパッケージマネージャーに対応している.

{{ #tabs }}
{{ #tab name=Rust }}
- [autd3](https://crates.io/crates/autd3)
- [autd3-gain-holo](https://crates.io/crates/autd3-gain-holo)
- [autd3-modulation-audio-file](https://crates.io/crates/autd3-modulation-audio-file)
- [autd3-link-twincat](https://crates.io/crates/autd3-link-twincat)
- [autd3-link-simulator](https://crates.io/crates/autd3-link-simulator)
- [autd3-link-soem](https://crates.io/crates/autd3-link-soem)
- [autd3-emulator](https://crates.io/crates/autd3-emulator)
{{ #endtab }}
{{ #tab name=C++ }}
CMakeのFetchContentを使用してインストールできる.

- autd3
    - Windows: [https://github.com/shinolab/autd3-cpp/releases/download/v32.1.1/autd3-v32.1.1-win-x64.zip](https://github.com/shinolab/autd3-cpp/releases/download/v32.1.1/autd3-v32.1.1-win-x64.zip)
    - macOS: [https://github.com/shinolab/autd3-cpp/releases/download/v32.1.1/autd3-v32.1.1-macos-aarch64.tar.gz](https://github.com/shinolab/autd3-cpp/releases/download/v32.1.1/autd3-v32.1.1-macos-aarch64.tar.gz)
    - Linux: [https://github.com/shinolab/autd3-cpp/releases/download/v32.1.1/autd3-v32.1.1-linux-x64.tar.gz](https://github.com/shinolab/autd3-cpp/releases/download/v32.1.1/autd3-v32.1.1-linux-x64.tar.gz)
- autd3-link-soem
    - Windows: [https://github.com/shinolab/autd3-cpp-link-soem/releases/download/v32.1.1/autd3-link-soem-v32.1.1-win-x64.zip](https://github.com/shinolab/autd3-cpp-link-soem/releases/download/v32.1.1/autd3-link-soem-v32.1.1-win-x64.zip)
    - macOS: [https://github.com/shinolab/autd3-cpp-link-soem/releases/download/v32.1.1/autd3-link-soem-v32.1.1-macos-aarch64.tar.gz](https://github.com/shinolab/autd3-cpp-link-soem/releases/download/v32.1.1/autd3-link-soem-v32.1.1-macos-aarch64.tar.gz)
    - Linux: [https://github.com/shinolab/autd3-cpp-link-soem/releases/download/v32.1.1/autd3-link-soem-v32.1.1-linux-x64.tar.gz](https://github.com/shinolab/autd3-cpp-link-soem/releases/download/v32.1.1/autd3-link-soem-v32.1.1-linux-x64.tar.gz)
{{ #endtab }}
{{ #tab name=C# }}
NuGetで公開している.

- [AUTD3Sharp](https://www.nuget.org/packages/AUTD3Sharp)
- [AUTD3Sharp.Link.SOEM](https://www.nuget.org/packages/AUTD3Sharp.Link.SOEM)
{{ #endtab }}
{{ #tab name=Unity }}
Unity Package Manager経由でインストール可能.
以下のリポジトリを追加する.
- AUTD3Sharp: [https://github.com/shinolab/AUTD3Sharp.git#upm/latest](https://github.com/shinolab/AUTD3Sharp.git#upm/latest)
- AUTD3Sharp.Link.SOEM: [https://github.com/shinolab/AUTD3Sharp.Link.SOEM.git#upm/latest](https://github.com/shinolab/AUTD3Sharp.Link.SOEM.git#upm/latest)
{{ #endtab }}
{{ #tab name=Python }}
PyPIで公開している.

- [pyautd3](https://pypi.org/project/pyautd3/)
- [pyautd3_link_soem](https://pypi.org/project/pyautd3_link_soem/)
- [pyautd3_emulator](https://pypi.org/project/pyautd3_emulator/)
{{ #endtab }}
{{ #endtabs }}
