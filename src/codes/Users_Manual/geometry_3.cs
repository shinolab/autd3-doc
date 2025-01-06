~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;
~using var autd = Controller.Builder([new AUTD3(Point3.Origin)]).Open(Nop.Builder());
var numDevices = autd.NumDevices;
var numTransducers = autd.NumTransducers;
var center = autd.Center;