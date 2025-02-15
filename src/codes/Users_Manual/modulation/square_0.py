~from pyautd3 import Hz, SamplingConfig, Square, SquareOption
Square(
    freq=150 * Hz,
    option=SquareOption(
        low=0x00,
        high=0xFF,
        duty=0.5,
        sampling_config=SamplingConfig.FREQ_4K,
    ),
)