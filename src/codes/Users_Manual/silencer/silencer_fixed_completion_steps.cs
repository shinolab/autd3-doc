~using AUTD3Sharp;
var config = new Silencer(new FixedCompletionTime
{
    Intensity = Duration.FromMicros(250),
    Phase = Duration.FromMicros(250)
});