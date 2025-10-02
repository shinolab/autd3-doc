~using AUTD3Sharp;
~using AUTD3Sharp.TransitionMode;
~using AUTD3Sharp.Modulation;
new WithFiniteLoop(
    inner: new Static(),
    loopCount: 1,
    segment: Segment.S1,
    transitionMode: new SyncIdx()
);