~using AUTD3Sharp;
~using AUTD3Sharp.Modulation;
~using static AUTD3Sharp.Units;
new SamplingConfig(4000.0f * Hz).IntoNearest();
// or
new SamplingConfig(Duration.FromMicros(250)).IntoNearest();