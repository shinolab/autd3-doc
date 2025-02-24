~from pyautd3 import Hz, Sine, SineOption, kHz, SamplingConfig
from pyautd3.modulation import Fir

Fir(
    target=Sine(
        freq=150 * Hz,
        option=SineOption(
            sampling_config=SamplingConfig(20.0 * kHz),
        ),
    ),
    coef=[
        -0.000009, -0.000013, -0.000016, -0.000021, -0.000025, -0.000030, -0.000036,
        -0.000042, -0.000049, -0.000056, -0.000064, -0.000072, -0.000080, -0.000088,
        -0.000096, -0.000105, -0.000113, -0.000120, -0.000128, -0.000134, -0.000139,
        -0.000143, -0.000146, -0.000146, -0.000145, -0.000141, -0.000135, -0.000124,
        -0.000111, -0.000093, -0.000071, -0.000044, -0.000012, 0.000026, 0.000071,
        0.000122, 0.000180, 0.000247, 0.000321, 0.000405, 0.000497, 0.000599, 0.000712,
        0.000835, 0.000968, 0.001113, 0.001270, 0.001439, 0.001619, 0.001812, 0.002018,
        0.002236, 0.002467, 0.002711, 0.002968, 0.003237, 0.003518, 0.003812, 0.004118,
        0.004435, 0.004764, 0.005103, 0.005452, 0.005811, 0.006178, 0.006554, 0.006937,
        0.007326, 0.007720, 0.008119, 0.008521, 0.008925, 0.009331, 0.009737, 0.010141,
        0.010543, 0.010941, 0.011335, 0.011722, 0.012101, 0.012472, 0.012833, 0.013183,
        0.013520, 0.013843, 0.014152, 0.014445, 0.014720, 0.014978, 0.015217, 0.015435,
        0.015633, 0.015810, 0.015964, 0.016096, 0.016204, 0.016289, 0.016350, 0.016386,
        0.016399, 0.016386, 0.016350, 0.016289, 0.016204, 0.016096, 0.015964, 0.015810,
        0.015633, 0.015435, 0.015217, 0.014978, 0.014720, 0.014445, 0.014152, 0.013843,
        0.013520, 0.013183, 0.012833, 0.012472, 0.012101, 0.011722, 0.011335, 0.010941,
        0.010543, 0.010141, 0.009737, 0.009331, 0.008925, 0.008521, 0.008119, 0.007720,
        0.007326, 0.006937, 0.006554, 0.006178, 0.005811, 0.005452, 0.005103, 0.004764,
        0.004435, 0.004118, 0.003812, 0.003518, 0.003237, 0.002968, 0.002711, 0.002467,
        0.002236, 0.002018, 0.001812, 0.001619, 0.001439, 0.001270, 0.001113, 0.000968,
        0.000835, 0.000712, 0.000599, 0.000497, 0.000405, 0.000321, 0.000247, 0.000180,
        0.000122, 0.000071, 0.000026, -0.000012, -0.000044, -0.000071, -0.000093,
        -0.000111, -0.000124, -0.000135, -0.000141, -0.000145, -0.000146, -0.000146,
        -0.000143, -0.000139, -0.000134, -0.000128, -0.000120, -0.000113, -0.000105,
        -0.000096, -0.000088, -0.000080, -0.000072, -0.000064, -0.000056, -0.000049,
        -0.000042, -0.000036, -0.000030, -0.000025, -0.000021, -0.000016, -0.000013,
        -0.000009,
    ],
)