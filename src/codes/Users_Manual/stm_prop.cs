~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using static AUTD3Sharp.Units;
var stm = new FociSTM(foci: [Point3.Origin, Point3.Origin], config: 1.0f * Hz);
Console.WriteLine(stm.SamplingConfig().Freq()); // -> 2 Hz