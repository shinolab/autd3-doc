~from pyautd3 import Controller, AUTD3, Duration
from pyautd3.controller.timer import TimerStrategy, SpinSleeper

Controller.builder([AUTD3([0.0, 0.0, 0.0])])\
    .with_default_parallel_threshold(4)\
    .with_default_timeout(Duration.from_millis(20))\
    .with_send_interval(Duration.from_millis(1))\
    .with_receive_interval(Duration.from_millis(1))\
    .with_timer_strategy(TimerStrategy.Spin(SpinSleeper()))