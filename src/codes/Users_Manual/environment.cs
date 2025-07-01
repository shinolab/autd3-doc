~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using var autd = Controller.Open([new AUTD3()], new Nop());
autd.Environment.SoundSpeed = 340e3f;
autd.Environment.SetSoundSpeedFromTemp(15);
var wavelength = autd.Environment.Wavelength();
var wavenumber = autd.Environment.Wavenumber();