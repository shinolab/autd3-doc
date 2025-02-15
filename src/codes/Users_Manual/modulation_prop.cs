~using AUTD3Sharp;
~using AUTD3Sharp.Modulation;
~using static AUTD3Sharp.Units;
var m = new Sine(freq: 150u * Hz, option: new SineOption());
Console.WriteLine(m.SamplingConfig().Freq()); // -> 150Hz