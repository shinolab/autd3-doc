~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Gain;
~using static AUTD3Sharp.Units;
~using var autd = Controller.Builder([new AUTD3(Point3.Origin)]).Open(Nop.Builder());
var stm = new GainSTM((SamplingConfig)(1u * Hz), [new Null(), new Null()]);