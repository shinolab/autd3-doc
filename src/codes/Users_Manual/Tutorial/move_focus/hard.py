~import numpy as np
~from pyautd3 import AUTD3, Controller, Hz, Sine, SineOption, FociSTM
~from pyautd3.link.nop import Nop
~autd = Controller.open([AUTD3(pos=[0.0, 0.0, 0.0], rot=[1, 0, 0, 0])], Nop())
autd.send(
    Sine(
        freq=150 * Hz,
        option=SineOption(),
    )
)

center = autd.center() + np.array([0.0, 0.0, 150.0])
autd.send(
    FociSTM(
        foci=[
            center + np.array([20.0, 0.0, 0.0]),
            center - np.array([20.0, 0.0, 0.0]),
        ],
        config=0.5 * Hz,
        # config=Duration.from_secs(2),
        # config=SamplingConfig(1.0 * Hz),
        # config=SamplingConfig(Duration.from_secs(1)),
    )
)