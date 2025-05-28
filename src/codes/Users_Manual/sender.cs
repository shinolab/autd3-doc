~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Utils;
~using var autd = Controller.Open([new AUTD3()], new Nop());
var sender = autd.Sender(
    new SenderOption
    {
        SendInterval = Duration.FromMillis(1),
        ReceiveInterval = Duration.FromMillis(1),
        Timeout = null,
        Parallel = ParallelMode.Auto,
    },
    new SpinSleeper()
);
~var d = new Null();
sender.Send(d);