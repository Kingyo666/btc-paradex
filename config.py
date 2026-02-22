# Paradex BTC 秒开关配置

import os
from dotenv import load_dotenv

load_dotenv()

# ==================== API 配置 ====================
# Paradex 环境
PARADEX_ENV = "MAINNET"  # MAINNET 或 TESTNET

# L2 认证 - 从 .env 文件读取
L2_ADDRESS = os.getenv("L2_ADDRESS", "")
L2_PRIVATE_KEY = os.getenv("L2_PRIVATE_KEY", "")

# Paradex API URLs
API_BASE_URL = "https://api.prod.paradex.trade"
WS_URL = "wss://ws.api.prod.paradex.trade/v1"

# ==================== 交易配置 ====================
MARKET = "BTC-USD-PERP"

# 每单大小 (BTC)
ORDER_SIZE_BTC = 0.001

# 价差阈值 (百分比)
# 当价差 <= 此值时触发开仓
MAX_SPREAD_PERCENT = 0.0008  # 0.0008%

# 最大循环次数 (一开一关为一个循环)
# 每循环下2单，500循环 = 1000单 = Retail 24h 上限
MAX_CYCLES = 500

# 循环间隔 (秒)
# 考虑到 500ms speed bump，实际每单延迟约 1.5s
CYCLE_INTERVAL_SEC = 1.0

# ==================== 日志配置 ====================
LOG_FILE = "scalper.log"
LOG_LEVEL = "INFO"

# ==================== 安全配置 ====================
# 最大连续失败次数 (超过则暂停)
MAX_CONSECUTIVE_FAILURES = 5

# 紧急停止文件 (存在此文件则停止运行)
EMERGENCY_STOP_FILE = "STOP"
