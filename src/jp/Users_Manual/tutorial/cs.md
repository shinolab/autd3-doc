まず, ターミナルを開き, 適当なプロジェクトを作成し, AUTD3Sharpライブラリを追加する.

```shell
dotnet new console --name autd3-sample
cd autd3-sample
dotnet add package AUTD3Sharp
dotnet add package AUTD3Sharp.Link.SOEM
```

次に, `Program.cs`を以下のようにする.
これは単一焦点に$\SI{150}{Hz}$のAM変調をかける場合のソースコードである.

```csharp,name=Program.cs
{{#include ../../../codes/Users_Manual/Tutorial/single/Program.cs}}
```

そして, これを実行する.

```shell
dotnet run -c:Release
```

### Linux,macOS使用時の注意

Linux, macOSでは, SOEMを使用するのに管理者権限が必要な場合がある.
その場合は, 
```shell
sudo dotnet run -c:Release
```
とすること.
