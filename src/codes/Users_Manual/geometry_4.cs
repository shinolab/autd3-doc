~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;
~using var autd = Controller.Builder([new AUTD3(Point3.Origin)]).Open(Nop.Builder());
~{
  var dev = autd[0];
  ~}
foreach (var dev in autd)
{
  // do something
}