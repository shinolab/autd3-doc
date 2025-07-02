~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Modulation;
~using static AUTD3Sharp.Units;
~using var autd = Controller.Open([new AUTD3(pos: Point3.Origin, rot: Quaternion.Identity)], new Nop());
autd.Send(new Sine(
    freq: 150u * Hz,
    option: new SineOption()
));

var center = autd.Center() + new Vector3(0.0f, 0.0f, 150.0f);
while (true)
{
    autd.Send(new Focus(
        pos: center + new Vector3(20.0f, 0.0f, 0.0f),
        option: new FocusOption()
    ));

    Thread.Sleep(1000);

    autd.Send(new Focus(
        pos: center - new Vector3(20.0f, 0.0f, 0.0f),
        option: new FocusOption()
    ));

    Thread.Sleep(1000);
}