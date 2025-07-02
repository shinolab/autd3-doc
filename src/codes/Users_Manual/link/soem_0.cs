~using AUTD3Sharp;
using AUTD3Sharp.Link;

~using AUTD3Sharp.Utils;
new SOEM(
    errHandler: (slave, status) =>
    {
        Console.Error.WriteLine($"slave [{slave}]: {status}");
        if (status == Status.Lost)
            Environment.Exit(-1);
    },
    option: new SOEMOption
    {
        BufSize = 16,
        Ifname = "",
        StateCheckInterval = Duration.FromMillis(100),
        Sync0Cycle = Duration.FromMillis(1),
        SendCycle = Duration.FromMillis(1),
        ThreadPriority = AUTD3Sharp.Link.ThreadPriority.Max,
        ProcessPriority = ProcessPriority.High,
        SyncTolerance = Duration.FromMicros(1),
        SyncTimeout = Duration.FromSecs(10),
        Affinity = null,
    }
);