from pyautd3 import Duration
from pyautd3.link.ethercrab import (
    EtherCrab,
    EtherCrabOption,
    Status,
)


def err_handler(idx: int, status: Status) -> None:
    print(f"Device[{idx}]: {status}")


EtherCrab(
    err_handler=err_handler,
    option=EtherCrabOption(
        ifname=None,
        state_check_period=Duration.from_millis(100),
        sync0_period=Duration.from_millis(2),
        sync_tolerance=Duration.from_micros(1),
        sync_timeout=Duration.from_secs(10),
    ),
)
