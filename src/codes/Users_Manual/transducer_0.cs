~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;
~using var autd = Controller.Open([new AUTD3()], new Nop());
var tr = autd[0][0];
var trIdx = tr.Idx();
var devIdx = tr.DevIdx();
var position = tr.Position();