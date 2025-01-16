~using System;
~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using static AUTD3Sharp.Units;
Controller.Builder([
   new AUTD3(Point3.Origin),
   new AUTD3(new Point3(AUTD3.DeviceWidth, 0, 0))
         .WithRotation(EulerAngles.Zyz(0 * rad, MathF.PI / 2 * rad, 0 * rad))
])
~;