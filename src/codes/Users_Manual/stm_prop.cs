~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Link;
~using static AUTD3Sharp.Units;
~using var autd = Controller.Builder([new AUTD3(Point3.Origin)]).Open(Nop.Builder());
var stm = new FociSTM(1.0f * Hz, [Point3.Origin, Point3.Origin]);
var f = stm.Freq;                 // -> 1 Hz
var p = stm.Period;               // -> 1 s
var fs = stm.SamplingConfig.Freq; // -> 2 Hz