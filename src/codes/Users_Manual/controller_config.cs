~using System;
~using AUTD3Sharp;
~using AUTD3Sharp.Timer;
~using AUTD3Sharp.Utils;
~_ =
Controller.Builder([new AUTD3(Vector3.Zero)])
    .WithDefaultParallelThreshold(4)
    .WithDefaultTimeout(Duration.FromMillis(20))
    .WithSendInterval(Duration.FromMillis(1))
    .WithReceiveInterval(Duration.FromMillis(1))
    .WithTimerStrategy(AUTD3Sharp.Timer.TimerStrategy.Spin(new SpinSleeper()))
~;