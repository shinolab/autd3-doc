~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
new GPIOOutputs(
    (dev, gpio) => gpio == GPIOOut.O0 ? GPIOOutputType.BaseSignal : GPIOOutputType.None
);