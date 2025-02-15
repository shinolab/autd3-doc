using AUTD3Sharp.Modulation;

~using static AUTD3Sharp.Units;
new Fourier(
    components: [
        new Sine(freq: 100u * Hz, option: new SineOption()),
        new Sine(freq: 150u * Hz, option: new SineOption())
    ],
    option: new FourierOption
    {
        ScaleFactor = null,
        Clamp = false,
        Offset = 0x00
    }
);