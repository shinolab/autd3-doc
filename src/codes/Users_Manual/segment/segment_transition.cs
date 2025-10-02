~using AUTD3Sharp;
~using AUTD3Sharp.TransitionMode;
~using AUTD3Sharp.Modulation;
new WithSegment(
    inner: new Static(),
    segment: Segment.S1,
    transitionMode: new Immediate()
);