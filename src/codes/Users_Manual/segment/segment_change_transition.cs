~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;
~using var autd = Controller.Builder([new AUTD3(Point3.Origin)]).Open(Nop.Builder());
autd.Send(SwapSegment.Modulation(Segment.S1, TransitionMode.Immediate));