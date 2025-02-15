using AUTD3Sharp.Modulation.AudioFile;

~using static AUTD3Sharp.Units;
new Csv(
    path: "path/to/foo.csv",
    samplingConfig: 4000 * Hz,
    option: new CsvOption
    {
        Delimiter = ',',
    }
);