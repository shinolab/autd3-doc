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
var backend = new NalgebraBackend();
new LM(
    foci: [
             (new Point3(x1, y1, z1), 5e3f * Pa),
             (new Point3(x2, y2, z2), 5e3f * Pa)
    ],
    option: new LMOption
    {
        Eps1 = 1e-8f,
        Eps2 = 1e-8f,
        Tau = 1e-3f,
        KMax = 5,
        Initial = [],
        EmissionConstraint = EmissionConstraint.Clamp(EmitIntensity.Min, EmitIntensity.Max),
    },
    backend: backend
);