~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Gain;
~var x = 0.0f;
~var y = 0.0f;
~var z = 0.0f;
var g = new Focus(new Point3(x, y, z))
            .WithIntensity(0xFF)
            .WithPhaseOffset(0x00);