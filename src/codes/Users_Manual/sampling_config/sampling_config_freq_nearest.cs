~using AUTD3Sharp;
~using AUTD3Sharp.Modulation;
~using static AUTD3Sharp.Units;
~var s =
SamplingConfig.Nearest(4000.0f * Hz)
~;
// or
~var sp =
SamplingConfig.Nearest(TimeSpan.FromMicroseconds(250))
~;