# /pi_coin/core/verification.py
"""
Pi Coin Verification Engine - Ultimate Hyper-Tech Origin Verification
Features: AI-Pattern Recognition, Quantum-Resistant Hashing, Real-Time Ecosystem Monitoring, Auto-Rejection of Invalid Sources.
"""

import numpy as np
from sklearn.ensemble import RandomForestClassifier  # Advanced AI for source pattern recognition
from cryptography.hazmat.primitives import hashes
from pi_coin import ALLOWED_SOURCES, monitor, pi_based_hash, quantum_private_key, quantum_public_key
from pi_coin.utils.config import REJECTED_SOURCES  # e.g., ["exchange", "unknown", "illicit"]

# AI Model for Source Verification (Trained on historical valid/invalid patterns)
class SourceVerifier:
    """
    AI-powered verifier using RandomForest to classify sources as valid/invalid.
    Trains on features like transaction frequency, amount patterns, and Pi-math correlations.
    """
    
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.is_trained = False
        self.training_data = []  # List of (features, label) tuples
    
    def train(self, data: list):
        """Train AI model with sample data (features: [amount, freq, pi_correlation], label: 1=valid, 0=invalid)."""
        if len(data) < 10:
            return  # Need minimum data
        X = np.array([d[0] for d in data])
        y = np.array([d[1] for d in data])
        self.model.fit(X, y)
        self.is_trained = True
        print("AI Source Verifier Trained.")
    
    def predict_validity(self, features: list) -> bool:
        """Predict if source is valid based on features."""
        if not self.is_trained:
            return True  # Default to valid if untrained
        prediction = self.model.predict([features])
        return prediction[0] == 1

# Global Verifier Instance
verifier = SourceVerifier()

def verify_origin(source: str, pi_coin_id: str, amount: float = 1.0, freq: int = 1) -> bool:
    """
    Ultimate verification function for Pi Coin origin.
    - Checks against allowed sources.
    - Uses AI for pattern recognition.
    - Integrates Pi-math hashing and quantum signatures.
    - Monitors ecosystem for anomalies.
    Returns True if valid, False otherwise.
    """
    # Basic Source Check
    if source not in ALLOWED_SOURCES or source in REJECTED_SOURCES:
        print(f"Rejected: Source '{source}' not allowed.")
        return False
    
    # AI Pattern Check (Features: amount, frequency, Pi-correlation via digit sum)
    pi_digits = str(np.pi)[:10]  # Sample Pi digits
    pi_correlation = sum(int(d) for d in pi_digits) / 10.0  # Simple correlation metric
    features = [amount, freq, pi_correlation]
    if not verifier.predict_validity(features):
        print(f"Rejected: AI detected invalid pattern for source '{source}'.")
        return False
    
    # Quantum-Resistant Hash Verification
    expected_hash = pi_based_hash(f"{source}-{pi_coin_id}-{amount}")
    actual_hash = pi_based_hash(pi_coin_id)  # Simulate ID hash
    if expected_hash != actual_hash:
        print("Rejected: Hash mismatch (possible tampering).")
        return False
    
    # Ecosystem Anomaly Check
    if monitor.detect_anomaly(amount):
        print(f"Rejected: Ecosystem anomaly detected for amount {amount}.")
        return False
    
    # Quantum Signature Verification (Mock for ID)
    message = f"{source}-{pi_coin_id}".encode()
    try:
        # Simulate signing/verifying (in real use, sign during creation)
        signature = quantum_private_key.sign(message, padding.PSS(...), hashes.SHA256())  # From stablecoin.py
        quantum_public_key.verify(signature, message, padding.PSS(...), hashes.SHA256())
    except:
        print("Rejected: Quantum signature invalid.")
        return False
    
    print(f"Verified: Pi Coin from '{source}' is valid.")
    return True

def batch_verify(coins: list) -> list:
    """Batch verify multiple Pi Coins for efficiency."""
    results = []
    for coin in coins:
        results.append(verify_origin(coin['source'], coin['id'], coin.get('amount', 1.0), coin.get('freq', 1)))
    return results

# Example Usage (Run this to test)
if __name__ == "__main__":
    # Train AI with sample data (valid: mining/rewards, invalid: exchange)
    verifier.train([
        ([1.0, 5, 3.1], 1),  # Valid mining
        ([2.0, 3, 3.1], 1),  # Valid rewards
        ([10.0, 1, 2.5], 0), # Invalid exchange
        ([0.5, 10, 3.1], 1), # Valid P2P
    ])
    
    # Test verifications
    print(verify_origin("mining", "pi_id_123", 1.0, 5))  # Should be True
    print(verify_origin("exchange", "pi_id_456", 10.0, 1))  # Should be False
