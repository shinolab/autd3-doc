~using AUTD3Sharp;
var config = new Silencer(config: new FixedUpdateRate
{
    Intensity = 1,
    Phase = 1
}, target: SilencerTarget.Intensity);