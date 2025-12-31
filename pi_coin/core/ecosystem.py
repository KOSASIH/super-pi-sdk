# /pi_coin/core/ecosystem.py
"""
Pi Coin Ecosystem Engine - Ultimate Hyper-Tech Ecosystem Integrator
Features: AI-Driven Pricing, Real-Time Standardization, Decentralized Oracle Simulations, Analytics Dashboard.
"""

import asyncio
import numpy as np
from sklearn.linear_model import LinearRegression  # AI for pricing predictions
from pi_coin import PI_VALUE_USD, monitor
from pi_coin.core.stablecoin import PiCoin
from pi_coin.core.transaction import Transaction

class Merchant:
    """
    Merchant class for Pi ecosystem integration.
    - Sets prices in PI, converts to USD.
    - AI adjusts prices based on ecosystem health.
    """
    
    def __init__(self, name: str):
        self.name = name
        self.products = {}  # {product: price_pi}
        self.ai_model = LinearRegression()  # AI for price prediction based on demand
    
    def set_price(self, product: str, base_price_pi: float):
        """Set product price with AI adjustment."""
        # AI Predict adjustment (mock training on historical data)
        if len(self.products) > 5:  # Train if enough data
            X = np.array(list(range(len(self.products)))).reshape(-1, 1)
            y = np.array(list(self.products.values()))
            self.ai_model.fit(X, y)
            adjustment = self.ai_model.predict([[len(self.products)]])[0] * 0.1  # 10% AI tweak
        else:
            adjustment = 0.0
        
        adjusted_price = base_price_pi + adjustment
        self.products[product] = adjusted_price
        print(f"{self.name}: {product} priced at {adjusted_price} PI (${adjusted_price * PI_VALUE_USD})")
    
    def get_price_usd(self, product: str) -> float:
        """Get price in USD."""
        return self.products.get(product, 0) * PI_VALUE_USD

class ServiceProvider:
    """
    Service provider for wages/upah in PI.
    - Calculates service value with ecosystem standardization.
    """
    
    def __init__(self, name: str):
        self.name = name
        self.services = {}  # {service: rate_pi_per_hour}
    
    def set_rate(self, service: str, rate_pi: float):
        """Set service rate, standardized to PI."""
        self.services[service] = rate_pi
        print(f"{self.name}: {service} rate {rate_pi} PI/hour (${rate_pi * PI_VALUE_USD})")
    
    def calculate_payment(self, service: str, hours: float) -> float:
        """Calculate total payment in PI."""
        rate = self.services.get(service, 0)
        return rate * hours

class EcosystemOracle:
    """
    Decentralized oracle for external data (e.g., market trends).
    - Simulates real-time data feeds for ecosystem adjustments.
    """
    
    def __init__(self):
        self.data_feeds = {"market_trend": 1.0}  # Mock: Trend multiplier
    
    async def fetch_data(self, feed: str) -> float:
        """Async fetch simulated external data."""
        await asyncio.sleep(0.2)  # Simulate network delay
        return self.data_feeds.get(feed, 1.0) * np.random.uniform(0.9, 1.1)  # Random variation

class EcosystemDashboard:
    """
    Analytics dashboard for ecosystem overview.
    - Tracks transactions, supply, anomalies.
    """
    
    def __init__(self):
        self.transactions = []
        self.supply_status = PiCoin(0).get_supply_status()  # Initial
    
    def log_transaction(self, tx: Transaction):
        """Log a transaction for analytics."""
        self.transactions.append({
            "id": tx.tx_id,
            "amount": tx.amount_pi,
            "status": tx.status,
            "timestamp": tx.timestamp
        })
    
    def get_analytics(self) -> dict:
        """Generate ecosystem analytics."""
        total_tx = len(self.transactions)
        avg_amount = np.mean([t["amount"] for t in self.transactions]) if self.transactions else 0
        anomalies = sum(1 for t in self.transactions if monitor.detect_anomaly(t["amount"]))
        return {
            "total_transactions": total_tx,
            "average_amount_pi": avg_amount,
            "anomalies_detected": anomalies,
            "supply_utilization": self.supply_status["utilization_percent"]
        }

# Global Instances
oracle = EcosystemOracle()
dashboard = EcosystemDashboard()

async def standardize_value(value_usd: float) -> float:
    """Standardize external USD value to PI using oracle."""
    trend = await oracle.fetch_data("market_trend")
    pi_equivalent = (value_usd / PI_VALUE_USD) * trend
    return pi_equivalent

# Example Usage (Run this to test)
if __name__ == "__main__":
    # Merchant example
    merchant = Merchant("PiShop")
    merchant.set_price("Widget", 0.01)
    print(f"USD Price: ${merchant.get_price_usd('Widget')}")
    
    # Service example
    service = ServiceProvider("PiDev")
    service.set_rate("Coding", 0.05)
    print(f"Payment for 10 hours: {service.calculate_payment('Coding', 10)} PI")
    
    # Oracle and standardization
    asyncio.run(standardize_value(3141.59))  # ~1 PI
    
    # Dashboard
    tx = Transaction("buyer", "seller", 0.01)
    dashboard.log_transaction(tx)
    print(f"Analytics: {dashboard.get_analytics()}")
