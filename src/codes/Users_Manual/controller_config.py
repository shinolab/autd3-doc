~from datetime import timedelta
~from pyautd3 import Controller, AUTD3
Controller.builder([AUTD3([0.0, 0.0, 0.0])])\
    .with_parallel_threshold(4)\
    .with_send_interval(timedelta(milliseconds=1))\
    .with_receive_interval(timedelta(milliseconds=1))\
    .with_timer_resolution(1)