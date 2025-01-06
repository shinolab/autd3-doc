~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;
Controller.Builder([
   new AUTD3(new Point3(-AUTD3.DeviceWidth, 0, 0)),
   new AUTD3(Point3.Origin)
])
~;