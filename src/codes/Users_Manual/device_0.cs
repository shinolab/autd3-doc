~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;
~using var autd = Controller.Open([new AUTD3()], new Nop());
var dev = autd[0];
var idx = dev.Idx();
var rotation = dev.Rotation();
var xDir = dev.XDirection();
var yDir = dev.YDirection();
var axialDir = dev.AxialDirection();