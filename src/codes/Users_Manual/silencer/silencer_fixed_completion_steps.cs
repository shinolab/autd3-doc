~using AUTD3Sharp;
new Silencer(
    config: new FixedCompletionTime
    {
        Intensity = Duration.FromMicros(250),
        Phase = Duration.FromMicros(250),
        StrictMode = true
    }
);