~from pyautd3 import Hz, GainSTM, Null, SamplingConfig
stm = GainSTM(SamplingConfig(1 * Hz), [Null(), Null()])