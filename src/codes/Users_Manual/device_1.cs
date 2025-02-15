~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;
~using var autd = Controller.Open([new AUTD3()], new Nop());
~{
var tr = autd[0][0];
~}
foreach (var tr in autd[0])
{
  // do something
}