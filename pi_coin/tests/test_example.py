import pytest
import asyncio
from pi_coin.examples.merchant_example import run_merchant_simulation

@pytest.mark.asyncio
async def test_merchant_simulation():
    # Mock run (in real test, capture outputs or use fixtures)
    await run_merchant_simulation()
    # Assert no exceptions (basic smoke test)
    assert True
