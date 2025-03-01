~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
new DebugSettings(
    (dev, gpio) => gpio == GPIOOut.O0 ? DebugType.BaseSignal : DebugType.None
);