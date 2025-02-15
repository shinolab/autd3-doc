~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;
~using var autd = Controller.Open([new AUTD3()], new Nop());
autd.Send(new DebugSettings(
    (dev, gpio) => gpio == GPIOOut.O0 ? DebugType.BaseSignal : DebugType.None
));