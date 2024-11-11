~using AUTD3Sharp;
~using AUTD3Sharp.Modulation;
~using static AUTD3Sharp.Units;
~{
    var m = new Sine(150u * Hz).WithSamplingConfig(4000 * Hz);
    ~}
// or
~{
    var m = new Sine(150u * Hz).WithSamplingConfig(Duration.FromMicros(250));
    ~}