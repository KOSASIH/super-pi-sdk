import pytest
import asyncio
from pi_coin.core.ecosystem import Merchant, ServiceProvider, standardize_value, dashboard

def test_merchant_pricing():
    merchant = Merchant("TestShop")
    merchant.set_price("Item", 0.1)
    assert merchant.get_price_usd("Item") == 0.1 * 314159

def test_service_payment():
    service = ServiceProvider("TestService")
    service.set_rate("Work", 0.05)
    assert service.calculate_payment("Work", 2) == 0.1

@pytest.mark.asyncio
async def test_standardize_value():
    pi_val = await standardize_value(314159)
    assert 0.9 <= pi_val <= 1.1  # Approximate due to trend
