~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Link;
~using static AUTD3Sharp.Units;
~using var autd = Controller.Open([new AUTD3(pos: Point3.Origin, rot: Quaternion.Identity)], new Nop());
var center = autd.Center() + new Vector3(0, 0, 150);
const int pointNum = 200;
const float radius = 30.0f;
new GainSTM(
    gains: Enumerable.Range(0, pointNum).Select(i =>
    {
        var theta = 2.0f * MathF.PI * i / pointNum;
        return new Focus(
            pos: center + radius * new Vector3(MathF.Cos(theta), MathF.Sin(theta), 0),
            option: new FocusOption()
        );
    }),
    config: 1.0f * Hz,
    option: new GainSTMOption
    {
        Mode = GainSTMMode.PhaseIntensityFull
    }
);