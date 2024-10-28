~using System;
~using AUTD3Sharp;
~using AUTD3Sharp.Timer;
~using AUTD3Sharp.Utils;
~_ =
Controller.Builder([new AUTD3(Vector3.Zero)])
    .WithFallbackParallelThreshold(4)
    .WithFallbackTimeout(TimeSpan.FromMilliseconds(20))
    .WithSendInterval(TimeSpan.FromMilliseconds(1))
    .WithReceiveInterval(TimeSpan.FromMilliseconds(1))
    .WithTimerStrategy(AUTD3Sharp.Timer.TimerStrategy.Spin(new SpinSleeper()))
~;