~using AUTD3Sharp;
~using AUTD3Sharp.Modulation;
~using static AUTD3Sharp.Units;
new Square(
    freq: 150u * Hz,
    option: new SquareOption
    {
        Low = 0x00,
        High = 0xFF,
        Duty = 0.5f,
        SamplingConfig = SamplingConfig.Freq4K
    }
);