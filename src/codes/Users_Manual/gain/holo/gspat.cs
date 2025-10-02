using AUTD3Sharp.Gain.Holo;

~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using static AUTD3Sharp.Units;
~var x1 = 0.0f;
~var y1 = 0.0f;
~var z1 = 0.0f;
~var x2 = 0.0f;
~var y2 = 0.0f;
~var z2 = 0.0f;
new GSPAT(
    foci: [
             (new Point3(x1, y1, z1), 5e3f * Pa),
             (new Point3(x2, y2, z2), 5e3f * Pa)
    ],
    option: new GSPATOption
    {
        Repeat = 100,
        EmissionConstraint = EmissionConstraint.Clamp(Intensity.Min, Intensity.Max),
    }
);