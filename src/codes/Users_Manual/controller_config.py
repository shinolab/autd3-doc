~from datetime import timedelta
~from pyautd3 import Controller, AUTD3
~from pyautd3.controller.timer import TimerStrategy, SpinSleeper
Controller.builder([AUTD3([0.0, 0.0, 0.0])])\
    .with_fallback_parallel_threshold(4)\
    .with_fallback_timeout(timedelta(milliseconds=20))\
    .with_send_interval(timedelta(milliseconds=1))\
    .with_receive_interval(timedelta(milliseconds=1))\
    .with_timer_strategy(TimerStrategy.Spin(SpinSleeper()))