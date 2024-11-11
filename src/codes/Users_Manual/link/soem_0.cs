~using AUTD3Sharp;
using AUTD3Sharp.Link;

~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Modulation;
~using AUTD3Sharp.Utils;
~var autd = Controller.Builder([new AUTD3(Vector3.Zero)]).Open(
SOEM.Builder()
    .WithIfname("")
    .WithBufSize(32)
    .WithErrHandler((slave, status) =>
    {
        Console.Error.WriteLine($"slave [{slave}]: {status}");
        if (status == Status.Lost)
        {
            // You can also wait for the link to recover, without exiting the process
            Environment.Exit(-1);
        }
    })
    .WithStateCheckInterval(Duration.FromMillis(100))
    .WithSync0Cycle(Duration.FromMillis(1))
    .WithSendCycle(Duration.FromMillis(1))
    .WithTimerStrategy(TimerStrategy.SpinSleep)
    .WithSyncTolerance(Duration.FromMicros(1))
    .WithSyncTimeout(Duration.FromSecs(10))
    .WithThreadPriority(AUTD3Sharp.Link.ThreadPriority.Max)
    .WithProcessPriority(ProcessPriority.High)
~);