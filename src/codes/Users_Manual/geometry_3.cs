~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;
~using var autd = Controller.Builder([new AUTD3(Vector3.Zero)]).Open(Nop.Builder());
var numDevices = autd.Geometry.NumDevices;
var numTransducers = autd.Geometry.NumTransducers;
var center = autd.Geometry.Center;