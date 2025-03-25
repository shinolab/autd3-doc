~using AUTD3Sharp;
new PulseWidthEncoder(_dev => i => PulseWidth.FromDuty((float)i.Item1 / 510.0f));