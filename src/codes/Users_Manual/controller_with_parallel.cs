~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Modulation;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Driver.Datagram;
~using var autd = Controller.Builder([new AUTD3(Vector3.Zero)]).Open(Nop.Builder());
~var m = new Static();
~var g = new Null();
autd.Send((m, g).WithParallelThreshold(0));