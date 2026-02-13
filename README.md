# Binance Futures Testnet Trading Bot

## Overview

This project is a Python CLI trading bot that places **Market** and **Limit** orders on **Binance Futures Testnet (USDT-M)**.  
It demonstrates clean code structure, logging, input validation, and error handling.

---

## Features

- Place **MARKET** orders
- Place **LIMIT** orders
- Support **BUY** and **SELL** sides
- Input validation via CLI (`argparse`)
- Structured logging of API requests, responses, and errors
- Exception handling:
  - Invalid input
  - API errors
  - Network failures
- Safe management of API keys using `.env` file (excluded from GitHub)

---

## Project Structure
trading_bot/
│
├── bot/
│ ├── client.py # Binance client wrapper
│ ├── orders.py # Order placement logic
│ ├── validators.py # CLI input validation
│ ├── logging_config.py # Logging configuration
│
├── cli.py # CLI entry point
├── requirements.txt
├── README.md
├── .gitignore
└── logs/ # Logs of API requests/responses

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/Jithin-UN/Binance-futures-trading-bot.git
cd trading_bot
python -m venv venv
#Activate:
venv\Scripts\activate
#Install Dependencies
pip install -r requirements.txt
#Configure API Keys
BINANCE_API_KEY=my_testnet_api_key
BINANCE_API_SECRET=my_testnet_secret

# Usage Examples
Place a MARKET order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.003
# Binance Futures requires minimum notional value of 100 USDT per order.
# How LIMIT Orders Work
# BUY LIMIT
# You must place it:
# At or below current price
# But not extremely far away
# SELL LIMIT
# You must place it:
# At or above current price
# But within allowed range
# Sample Output:

===== ORDER SUCCESS =====
Order ID: 123456789
Status: FILLED
Executed Qty: 0.003
Avg Price: 63210.45

# Place a LIMIT order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.003 --price 64000

# Sample Output:
===== ORDER SUCCESS =====
Order ID: 987654321
Status: NEW
Executed Qty: 0
Price: 64000

# Logging

All API requests, responses, and errors are logged to:

logs/trading_bot.log

# Assumptions & Notes
Minimum order notional: Binance Futures requires each order ≥ 100 USDT.

Limit orders must respect Binance price filters — too far from market price will be rejected.

Testnet account must have USDT balance.

Only USDT-M futures are supported.

Leverage configuration is not implemented in this version.

.env file stores API credentials and is never pushed to GitHub.

# Tech Stack

Python 3.x
python-binance library
argparse for CLI input
logging for structured logging

# Sample Logs Included

MARKET order log
LIMIT order log
All logs are located in the logs/ folder for review.

# Future Enhancements

Add Stop-Limit / OCO / TWAP / Grid order types
Enhanced CLI user experience with prompts and validation messages
Optional lightweight UI for order management
WebSocket integration for real-time price updates
Step 1 — Add or Update README

After creating or editing `README.md`:```bash
git add README.md
Step 2 — Commit Changes
git commit -m "Add detailed README with setup, usage, and assumptions"
Step 3 — Push to GitHub
git push
