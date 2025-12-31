import pytest
import os
from pi_coin.utils.config import config_manager, get_config, set_config

def test_config_loading():
    assert get_config("pi_value_usd") == 314159

def test_ai_adjustment():
    config_manager.ai_adjust_config({"anomaly_rate": 0.2})
    assert 314158 <= config_manager.config["pi_value_usd"] <= 314160

def test_set_config():
    set_config("test_key", "test_value")
    assert get_config("test_key") == "test_value"
    # Cleanup
    os.remove("pi_coin_config.json") if os.path.exists("pi_coin_config.json") else None
