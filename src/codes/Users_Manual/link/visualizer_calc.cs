var autd = Controller.Builder().AddDevice(new AUTD3(Vector3d.zero)).Open(Visualizer.Builder());

var center = autd.Geometry.Center + new Vector3d(0, 0, 150);
var g = new Focus(center);
autd.Send(g);

var points = new List<Vector3d> { center };
var p = autd.Link.CalcField(points, autd.Geometry, Segment.S0, 0);
Console.WriteLine($"Acoustic pressure at ({center.x}, {center.y}, {center.z}) = ({p[0]})");