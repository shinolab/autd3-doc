~using AUTD3Sharp;
~using static AUTD3Sharp.Units;
new SamplingConfig(10);
// or
new SamplingConfig(4000 * Hz);
// or
new SamplingConfig(Duration.FromMicros(250));