using AUTD3Sharp.Modulation.AudioFile;

~using static AUTD3Sharp.Units;
var path = "path/to/foo.csv";
var m = new Csv(
    path: path,
    samplingConfig: 4000 * Hz,
    option: new CsvOption
    {
        Delimiter = ',',
    }
);