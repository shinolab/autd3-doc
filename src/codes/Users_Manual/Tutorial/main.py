import os

import numpy as np
from pyautd3 import (
    AUTD3,
    Controller,
    Focus,
    FocusOption,
    Hz,
    Silencer,
    Sine,
    SineOption,
)
from pyautd3_link_soem import SOEM, SOEMOption, Status


def err_handler(slave: int, status: Status) -> None:
    print(f"slave [{slave}]: {status}")
    if status == Status.Lost():
        # You can also wait for the link to recover, without exiting the process
        os._exit(-1)


if __name__ == "__main__":
    with Controller.open(
        [AUTD3(pos=[0.0, 0.0, 0.0], rot=[1, 0, 0, 0])],
        SOEM(err_handler=err_handler, option=SOEMOption()),
    ) as autd:
        firmware_version = autd.firmware_version()
        print(
            "\n".join(
                [f"[{i}]: {firm}" for i, firm in enumerate(firmware_version)],
            ),
        )

        autd.send(Silencer())

        g = Focus(pos=autd.center + np.array([0.0, 0.0, 150.0]), option=FocusOption())
        m = Sine(freq=150 * Hz, option=SineOption())
        autd.send((m, g))

        _ = input()

        autd.close()