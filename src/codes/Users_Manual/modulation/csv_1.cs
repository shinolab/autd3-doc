~using AUTD3Sharp.Modulation;
~using AUTD3Sharp.Modulation.AudioFile;
~using static AUTD3Sharp.Units;
~var path = "path/to/foo.csv";
var m = new Csv(path, 2.0f * kHz, 4u * kHz, new SincInterpolation(new BlackMan(32)));