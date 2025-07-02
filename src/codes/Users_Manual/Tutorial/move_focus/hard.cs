~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Modulation;
~using static AUTD3Sharp.Units;
~using var autd = Controller.Open([new AUTD3(pos: Point3.Origin, rot: Quaternion.Identity)], new Nop());
autd.Send(new Sine(
    freq: 150u * Hz,
    option: new SineOption()
));

var center = autd.Center() + new Vector3(0.0f, 0.0f, 150.0f);
autd.Send(new FociSTM(
    foci: [
        center + new Vector3(20.0f, 0.0f, 0.0f),
        center - new Vector3(20.0f, 0.0f, 0.0f),
    ],
    config: 0.5f * Hz
    // config: Duration.FromSecs(2)
    // config: new SamplingConfig(1.0f * Hz)
    // config: new SamplingConfig(Duration.FromSecs(1))
));