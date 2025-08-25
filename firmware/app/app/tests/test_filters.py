import numpy as np
from app.preprocessing.filters import hpf_lpf

def test_hpf_lpf_shapes():
    x = np.random.randn(1000)
    y = hpf_lpf(x, fs=250.0)
    assert y.shape == x.shape
app/tests/test_rpeaks.py
import numpy as np
from app.preprocessing.rpeaks import detect_rpeaks

def test_rpeaks_basic():
    # signal synthétique : pics toutes 1s à fs=250
    fs=250; T=5
    x = np.zeros(fs*T)
    x[::fs] = 5.0
    idx = detect_rpeaks(x, fs)
    assert len(idx) >= 4
