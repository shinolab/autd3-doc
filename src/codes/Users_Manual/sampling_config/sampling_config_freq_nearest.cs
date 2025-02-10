~using AUTD3Sharp;
~using AUTD3Sharp.Modulation;
~using static AUTD3Sharp.Units;
SamplingConfig.Nearest(4000.0f * Hz);
// or
SamplingConfig.Nearest(Duration.FromMicros(250));