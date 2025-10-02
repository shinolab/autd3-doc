First, open a terminal, create an appropriate project, and add the AUTD3Sharp library.

```shell
dotnet new console --name autd3-sample
cd autd3-sample
dotnet add package AUTD3Sharp
```

Next, edit `Program.cs` as follows.
This is the source code for applying AM modulation of $\SI{150}{Hz}$ to a single focal point.

```csharp,name=Program.cs
{{#include ../../../codes/Users_Manual/Tutorial/single/Program.cs}}
```

Then, run it.

```shell
dotnet run -c:Release
```

### Notes for Linux and macOS Users

On Linux and macOS, administrator privileges may be required.
In that case, run:
```shell
sudo dotnet run -c:Release
```
