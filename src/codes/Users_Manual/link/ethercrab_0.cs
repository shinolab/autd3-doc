~using AUTD3Sharp;
using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;

new EtherCrab(
    errHandler: (idx, status) =>
    {
        Console.Error.WriteLine($"Device[{idx}]: {status}");
    },
    option: new EtherCrabOption
    {
        Ifname = null,
        StateCheckPeriod = Duration.FromMillis(100),
        Sync0Period = Duration.FromMillis(2),
        SyncTolerance = Duration.FromMicros(1),
        SyncTimeout = Duration.FromSecs(10),
    }
);