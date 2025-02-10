~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;
~using var autd = Controller.Open([new AUTD3()], new Nop());
var dev = autd[0];
var idx = dev.Idx;
dev.Enable = false;
dev.SoundSpeed = 340e3f;
dev.SetSoundSpeedFromTemp(15);
var t = new Vector3(1, 0, 0);
var r = new Quaternion(0, 0, 0, 1);
dev.Translate(t);
dev.Rotate(r);
dev.Affine(t, r);
var wavelength = dev.Wavelength;
var wavenumber = dev.Wavenumber;
var rotation = dev.Rotation;
var xDir = dev.XDirection;
var yDir = dev.YDirection;
var axialDir = dev.AxialDirection;