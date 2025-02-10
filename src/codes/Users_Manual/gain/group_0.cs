~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Driver.Datagram;
~var x = 0.0f;
~var y = 0.0f;
~var z = 0.0f;
new Group(
    keyMap: dev => tr => tr.Idx() <= 100 ? "null" : "focus",
    gainMap: new Dictionary<object, IGain> {
        { "null", new Null() },
        { "focus", new Focus(pos: new Point3(x, y, z), option: new FocusOption()) }
    }
);