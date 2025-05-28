~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Modulation;
~using AUTD3Sharp.Utils;
~var x = 0.0f;
~var y = 0.0f;
~var z = 0.0f;
new AUTD3Sharp.Group(dev =>
    {
        return dev.Idx() switch
        {
            0 => "null",
            1 => "focus",
            _ => null
        };
    },
    new GroupDictionary {
        { "null", new Null() },
        { "focus", new Focus(pos: new Point3(x, y, z), option: new FocusOption()) }
    }
);