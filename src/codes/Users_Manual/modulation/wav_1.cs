~using AUTD3Sharp.Modulation;
~using AUTD3Sharp.Modulation.AudioFile;
~using static AUTD3Sharp.Units;
~var path = "path/to/foo.wav";
var m = new Wav(path, 4u * kHz, new SincInterpolation(new BlackMan(32)));