~using System;
~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;
~using static AUTD3Sharp.Units;
~var link = new Nop();
Controller.Open([
   new AUTD3(pos: Point3.Origin, rot: Quaternion.Identity),
   new AUTD3(
      pos: new Point3(0, 0, AUTD3.DeviceWidth),
      rot: EulerAngles.Zyz(0 * rad, MathF.PI / 2 * rad, 0 * rad))
], link)
~;