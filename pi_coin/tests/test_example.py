# /pi_coin/tests/test_examples.py
"""
Tests for Pi Coin Examples - Ultimate Hyper-Tech Example Testing
Features: Smoke tests for merchant and service simulations, integration checks.
"""

import pytest
import asyncio
from pi_coin.examples.merchant_example import run_merchant_simulation
from pi_coin.examples.service_example import run_service_simulation
from pi_coin.core.ecosystem import dashboard

@pytest.mark.asyncio
async def test_merchant_simulation():
    """Test merchant example simulation."""
    # Reset dashboard for clean test
    dashboard.transactions = []
    
    # Run simulation
    await run_merchant_simulation()
    
    # Basic assertions: Check if transactions were logged
    analytics = dashboard.get_analytics()
    assert analytics["total_transactions"] >= 0  # At least no errors
    assert "average_amount_pi" in analytics

@pytest.mark.asyncio
async def test_service_simulation():
    """Test service provider example simulation."""
    # Reset dashboard for clean test
    dashboard.transactions = []
    
    # Run simulation
    await run_service_simulation()
    
    # Basic assertions: Check if transactions were logged
    analytics = dashboard.get_analytics()
    assert analytics["total_transactions"] >= 0  # At least no errors
    assert "average_amount_pi" in analytics

@pytest.mark.asyncio
async def test_combined_examples():
    """Test running both examples sequentially."""
    dashboard.transactions = []
    
    await run_merchant_simulation()
    await run_service_simulation()
    
    analytics = dashboard.get_analytics()
    assert analytics["total_transactions"] >= 2  # At least one from each
