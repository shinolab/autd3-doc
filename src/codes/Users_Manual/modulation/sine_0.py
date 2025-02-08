~from pyautd3 import Hz, SamplingConfig, Sine, SineOption, rad
Sine(
    freq=150 * Hz,
    option=SineOption(
        intensity=0xFF,
        offset=0x80,
        phase=0.0 * rad,
        clamp=False,
        sampling_config=SamplingConfig.FREQ_4K,
    ),
)