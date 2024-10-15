~using System;
~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;
~_ =
Controller.Builder([new AUTD3(Vector3.Zero)])
    .WithParallelThreshold(4)
    .WithSendInterval(TimeSpan.FromMilliseconds(1))
    .WithReceiveInterval(TimeSpan.FromMilliseconds(1))
    .WithTimerResolution(1);