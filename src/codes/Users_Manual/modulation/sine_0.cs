~using AUTD3Sharp;
~using AUTD3Sharp.Modulation;
~using static AUTD3Sharp.Units;
new Sine(
    freq: 150u * Hz,
    option: new SineOption
    {
        Intensity = 0xFF,
        Offset = 0x80,
        Phase = 0f * rad,
        Clamp = false,
        SamplingConfig = SamplingConfig.Freq4K
    }
);