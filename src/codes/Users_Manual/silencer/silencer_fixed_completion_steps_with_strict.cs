~using AUTD3Sharp;
ushort stepsIntensity = 10;
ushort stepsPhase = 10;
var config = Silencer.FromCompletionSteps(stepsIntensity, stepsPhase).WithStrictMode(false);