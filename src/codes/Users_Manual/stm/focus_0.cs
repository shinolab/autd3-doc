~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Link;
~using static AUTD3Sharp.Units;
var center = new Point3(0, 0, 150);
const int pointNum = 200;
const float radius = 30.0f;
new FociSTM(
    foci: Enumerable.Range(0, pointNum).Select(i =>
    {
        var theta = 2.0f * MathF.PI * i / pointNum;
        return center + radius * new Vector3(MathF.Cos(theta), MathF.Sin(theta), 0);
    }),
    config: 1.0f * Hz
);