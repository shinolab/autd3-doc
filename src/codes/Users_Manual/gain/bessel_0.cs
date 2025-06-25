~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Gain;
~using static AUTD3Sharp.Units;
~var x = 0.0f;
~var y = 0.0f;
~var z = 0.0f;
~var nx = 0.0f;
~var ny = 0.0f;
~var nz = 1.0f;
~var theta = 0.0f;
new Bessel(
    pos: new Point3(x, y, z),
    dir: new Vector3(nx, ny, nz),
    theta: theta * rad,
    option: new BesselOption
    {
        Intensity = Intensity.Max,
        PhaseOffset = Phase.Zero
    }
);