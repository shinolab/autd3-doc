~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;
~using var autd = Controller.Open([new AUTD3()], new Nop());
var numDevices = autd.NumDevices;
var numTransducers = autd.NumTransducers;
var center = autd.Center;