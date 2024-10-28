using AUTD3Sharp;
using AUTD3Sharp.Utils;
using AUTD3Sharp.Link;
using AUTD3Sharp.Gain;
using AUTD3Sharp.Modulation;
using static AUTD3Sharp.Units;

using var autd = Controller.Builder([new AUTD3(Vector3.Zero)])
        .Open(SOEM.Builder().WithErrHandler((slave, status) =>
        {
            Console.Error.WriteLine($"slave [{slave}]: {status}");
            if (status == Status.Lost)
                Environment.Exit(-1);
        }));

var firmList = autd.FirmwareVersion();
foreach (var firm in firmList)
    Console.WriteLine(firm);

autd.Send(new Silencer());

var g = new Focus(autd.Center + new Vector3(0, 0, 150));
var m = new Sine(150u * Hz);
autd.Send((m, g));

Console.ReadKey(true);

autd.Close();