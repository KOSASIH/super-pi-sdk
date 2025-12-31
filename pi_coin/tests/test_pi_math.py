import pytest
from pi_coin.utils.pi_math import pi_math

def test_generate_pi_chudnovsky():
    pi_str = pi_math.generate_pi_chudnovsky(10)
    assert len(pi_str) >= 10
    assert pi_str.startswith("3.14159")

def test_benchmark():
    bench = pi_math.benchmark_pi_generation("leibniz", 100)
    assert bench["time_seconds"] > 0
    assert bench["accuracy_percent"] > 90
