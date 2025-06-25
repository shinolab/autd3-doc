~import os
from pyautd3 import Duration
from pyautd3_link_soem import (
    SOEM,
    ProcessPriority,
    SOEMOption,
    Status,
    ThreadPriority,
)


def err_handler(slave: int, status: Status) -> None:
    print(f"slave [{slave}]: {status}")
    if status == Status.Lost():
        os._exit(-1)


SOEM(
    err_handler=err_handler,
    option=SOEMOption(
        buf_size=32,
        ifname="",
        state_check_interval=Duration.from_millis(100),
        sync0_cycle=Duration.from_millis(1),
        send_cycle=Duration.from_millis(1),
        thread_priority=ThreadPriority.Max,
        process_priority=ProcessPriority.High,  # only available on Windows
        sync_tolerance=Duration.from_micros(1),
        sync_timeout=Duration.from_secs(10),
    ),
)