~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Modulation;
~using static AUTD3Sharp.Units;
~using var autd = Controller.Open([new AUTD3(pos: Point3.Origin, rot: Quaternion.Identity)], new Nop());
autd.Send(new Silencer());

var center = autd.Center() + new Vector3(0.0f, 0.0f, 150.0f);
const int pointNum = 40;
const float radius = 30.0f;
new FociSTM(
    foci: Enumerable.Range(0, pointNum).Select(i =>
    {
        var theta = 2.0f * MathF.PI * i / pointNum;
        return center + radius * new Vector3(MathF.Cos(theta), MathF.Sin(theta), 0);
    }),
    config: 50.0f * Hz
);