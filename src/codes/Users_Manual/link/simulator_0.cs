~using AUTD3Sharp;
~using System.Net;
using AUTD3Sharp.Link;

~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Modulation;
~using AUTD3Sharp.Utils;
~var autd = Controller.Builder([new AUTD3(Point3.Origin)]).Open(
Simulator.Builder(new IPEndPoint(IPAddress.Parse("127.0.0.1"), 8080))
~);