@pytest.mark.asyncio
async def test_p2p_simulation():
    """Test P2P example simulation."""
    dashboard.transactions = []
    
    await run_p2p_simulation()
    
    analytics = dashboard.get_analytics()
    assert analytics["total_transactions"] >= 0
    assert "average_amount_pi" in analytics
