~using AUTD3Sharp;
var config = new Silencer(new FixedCompletionTime
{
    Intensity = TimeSpan.FromMicroseconds(250),
    Phase = TimeSpan.FromMicroseconds(250)
});