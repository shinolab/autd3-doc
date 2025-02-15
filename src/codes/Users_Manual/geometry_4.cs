~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;
~using var autd = Controller.Open([new AUTD3()], new Nop());
~{
var dev = autd[0];
~}
foreach (var dev in autd)
{
  // do something
}