import pytest
from pi_coin.core.verification import verify_origin, verifier

def test_verify_valid_source():
    verifier.train([([1.0, 5, 3.1], 1)])  # Train minimally
    assert verify_origin("mining", "test_id", 1.0, 5) == True

def test_verify_invalid_source():
    assert verify_origin("exchange", "test_id", 10.0, 1) == False

def test_batch_verify():
    coins = [{"source": "mining", "id": "id1"}, {"source": "exchange", "id": "id2"}]
    results = batch_verify(coins)
    assert results == [True, False]
