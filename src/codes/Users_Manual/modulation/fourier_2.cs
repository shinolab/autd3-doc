~using AUTD3Sharp;
~using AUTD3Sharp.Modulation;
~using static AUTD3Sharp.Units;
~using System;
var m = new Fourier([new Sine(100u * Hz), new Sine(150 * Hz).WithPhase(MathF.PI / 2.0f * rad)]);