import os

import numpy as np
from pyautd3 import AUTD3, Controller, Focus, Hz, Silencer, Sine
from pyautd3_link_soem import SOEM, Status


def err_handler(slave: int, status: Status) -> None:
    print(f"slave [{slave}]: {status}")
    if status == Status.Lost():
        # You can also wait for the link to recover, without exiting the process
        os._exit(-1)


if __name__ == "__main__":
    with Controller.builder([AUTD3([0.0, 0.0, 0.0])]).open(
        SOEM.builder().with_err_handler(err_handler),
    ) as autd:
        firmware_version = autd.firmware_version()
        print(
            "\n".join(
                [f"[{i}]: {firm}" for i, firm in enumerate(firmware_version)],
            ),
        )

        autd.send(Silencer())

        g = Focus(autd.center + np.array([0.0, 0.0, 150.0]))
        m = Sine(150 * Hz)
        autd.send((m, g))

        _ = input()

        autd.close()
