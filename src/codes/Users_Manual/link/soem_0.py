~import os
~from pyautd3 import Duration
from pyautd3_link_soem import (
    SOEM,
    ProcessPriority,
    Status,
    ThreadPriority,
    TimerStrategy,
)


def err_handler(slave: int, status: Status) -> None:
    print(f"slave [{slave}]: {status}")
    if status == Status.Lost():
        # You can also wait for the link to recover, without exiting the process
        os._exit(-1)


SOEM.builder()\
    .with_ifname("")\
    .with_buf_size(32)\
    .with_err_handler(err_handler)\
    .with_state_check_interval(Duration.from_millis(100))\
    .with_sync0_cycle(Duration.from_millis(1))\
    .with_send_cycle(Duration.from_millis(1))\
    .with_timer_strategy(TimerStrategy.SpinSleep)\
    .with_sync_tolerance(Duration.from_micros(1))\
    .with_sync_timeout(Duration.from_secs(10))\
    .with_thread_priority(ThreadPriority.Max)\
    .with_process_priority(ProcessPriority.High)