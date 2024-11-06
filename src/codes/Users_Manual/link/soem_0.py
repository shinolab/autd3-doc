~import os
~from datetime import timedelta
~
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
    .with_state_check_interval(timedelta(milliseconds=100))\
    .with_sync0_cycle(timedelta(milliseconds=1))\
    .with_send_cycle(timedelta(milliseconds=1))\
    .with_timer_strategy(TimerStrategy.SpinSleep)\
    .with_sync_tolerance(timedelta(microseconds=1))\
    .with_sync_timeout(timedelta(seconds=10))\
    .with_thread_priority(ThreadPriority.Max)\
    .with_process_priority(ProcessPriority.High)