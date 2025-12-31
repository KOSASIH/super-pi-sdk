import pytest
from pi_coin.utils.hashing import pi_based_hash, hash_engine

def test_pi_based_hash():
    hash_val = pi_based_hash("test")
    assert len(hash_val) in [64, 128]  # SHA256 or SHA3 length

def test_ai_select_hash():
    assert hash_engine.ai_select_hash("short") in ["SHA256", "SHA3_512"]

def test_quantum_sign_verify():
    data = "test data"
    signature = hash_engine.quantum_sign_hash(data)
    public_key = rsa.generate_private_key(public_exponent=65537, key_size=4096).public_key()
    assert hash_engine.verify_quantum_signature(data, signature, public_key) == True
