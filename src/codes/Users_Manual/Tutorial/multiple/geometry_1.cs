~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;
~var link = new Nop();
Controller.Open([
   new AUTD3(pos: new Point3(-AUTD3.DeviceWidth, 0, 0), rot: Quaternion.Identity),
   new AUTD3(pos: Point3.Origin, rot: Quaternion.Identity)
], link)
~;