~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;
~using var autd = Controller.Builder([new AUTD3(Vector3.Zero)]).Open(Nop.Builder());
~{
var tr = autd[0][0];
  ~}
foreach (var tr in autd[0])
{
  // do something
}