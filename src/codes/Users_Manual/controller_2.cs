~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Modulation;
~using AUTD3Sharp.Utils;
~using var autd = Controller.Builder([new AUTD3(Point3.Origin)]).Open(Nop.Builder());
~var x = 0.0f;
~var y = 0.0f;
~var z = 0.0f;
autd.Group(dev =>
    {
        return dev.Idx switch
        {
            0 => "null",
            1 => "focus",
            _ => null
        };
    })
    .Set("null", new Null())
    .Set("focus", new Focus(new Point3(x, y, z)))
    .Send();