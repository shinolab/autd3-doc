~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Gain;
~var nx = 0.0f;
~var ny = 0.0f;
~var nz = 1.0f;
new Plane(
    dir: new Vector3(nx, ny, nz),
    option: new PlaneOption
    {
        Intensity = Intensity.Max,
        PhaseOffset = Phase.Zero
    }
);