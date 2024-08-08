~using AUTD3Sharp;
var timeIntensity = TimeSpan.FromMicroseconds(250);
var timePhase = TimeSpan.FromMicroseconds(250);
var config = Silencer.FromCompletionTime(timeIntensity, timePhase);