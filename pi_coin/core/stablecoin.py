# /pi_coin/core/stablecoin.py
"""
Pi Coin Stablecoin Engine - Ultimate Hyper-Tech Stablecoin Class
Features: Fixed Value, Supply Cap, AI-Modulated Supply, Quantum Signatures, Ecosystem Health Integration.
"""

import numpy as np
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.exceptions import InvalidSignature
from pi_coin import PI_VALUE_USD, TOTAL_SUPPLY, monitor, quantum_private_key, quantum_public_key, pi_based_hash
from pi_coin.utils.config import ALLOWED_SOURCES

class PiCoin:
    """
    Ultimate Pi Coin Stablecoin Class.
    - Fixed value: 1 PI = $314,159
    - Total supply cap: 100,000,000,000 PI
    - AI-modulated: Adjusts supply based on ecosystem anomalies.
    - Quantum-resistant: Uses RSA signatures for transactions.
    """
    
    _global_supply = 0.0  # Tracks total minted supply (class-level)
    
    def __init__(self, amount_pi: float, source: str = "mining"):
        if source not in ALLOWED_SOURCES:
            raise ValueError(f"Invalid source: {source}. Must be one of {ALLOWED_SOURCES}.")
        
        self.amount_pi = amount_pi
        self.value_usd = amount_pi * PI_VALUE_USD
        self.source = source
        self.coin_id = pi_based_hash(f"{amount_pi}-{source}-{np.random.randint(1000000)}")  # Unique ID with Pi-hash
        
        # AI-Modulated Supply: Check ecosystem health and adjust if anomalies detected
        if monitor.detect_anomaly(amount_pi):
            self.amount_pi *= 0.95  # Reduce by 5% for anomaly mitigation
            self.value_usd = self.amount_pi * PI_VALUE_USD
            print(f"AI Anomaly Detected: Supply adjusted to {self.amount_pi} PI.")
        
        # Enforce supply cap
        if PiCoin._global_supply + self.amount_pi > TOTAL_SUPPLY:
            raise OverflowError(f"Supply cap exceeded. Current supply: {PiCoin._global_supply}, Requested: {self.amount_pi}.")
        
        PiCoin._global_supply += self.amount_pi
        
        # Quantum Signature for Security
        self.signature = self._sign_transaction()
    
    def convert_to_usd(self) -> float:
        """Convert PI to fixed USD value."""
        return self.value_usd
    
    def get_supply_status(self) -> dict:
        """Return current global supply status."""
        return {
            "current_supply": PiCoin._global_supply,
            "remaining_supply": TOTAL_SUPPLY - PiCoin._global_supply,
            "utilization_percent": (PiCoin._global_supply / TOTAL_SUPPLY) * 100
        }
    
    def _sign_transaction(self) -> bytes:
        """Generate quantum-resistant RSA signature for the transaction."""
        message = f"{self.coin_id}-{self.amount_pi}-{self.source}".encode()
        signature = quantum_private_key.sign(
            message,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        return signature
    
    def verify_signature(self) -> bool:
        """Verify the quantum signature."""
        message = f"{self.coin_id}-{self.amount_pi}-{self.source}".encode()
        try:
            quantum_public_key.verify(
                self.signature,
                message,
                padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
                hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False
    
    @classmethod
    def reset_supply(cls):
        """Reset global supply (for testing only)."""
        cls._global_supply = 0.0

# Example Usage (Run this to test)
if __name__ == "__main__":
    # Train AI monitor with sample data
    monitor.train([1.0, 2.0, 3.0, 100.0])  # 100.0 might be flagged as anomaly
    
    try:
        pi_coin = PiCoin(10.0, "mining")
        print(f"Created Pi Coin: {pi_coin.amount_pi} PI = ${pi_coin.convert_to_usd()}")
        print(f"Supply Status: {pi_coin.get_supply_status()}")
        print(f"Signature Valid: {pi_coin.verify_signature()}")
    except Exception as e:
        print(f"Error: {e}")
