~from pyautd3 import Hz, GainSTM, GainSTMMode, Null
stm = GainSTM(1.0 * Hz, [Null(), Null()]).with_mode(GainSTMMode.PhaseFull)