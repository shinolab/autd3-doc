~using AUTD3Sharp;
~using AUTD3Sharp.Modulation;
new WithLoopBehavior(
    inner: new Static(),
    loopBehavior: LoopBehavior.Infinite,
    segment: Segment.S1,
    transitionMode: TransitionMode.Immediate
);

new WithLoopBehavior(
    inner: new Static(),
    loopBehavior: LoopBehavior.Finite(10),
    segment: Segment.S1,
    transitionMode: TransitionMode.SyncIdx
);