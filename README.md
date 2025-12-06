# Medical Summary Bot

A Telegram bot + web backend for creating structured medical summaries.

## Structure
- bot.py  → Telegram bot
- backend.py → FastAPI backend
- templates/admin.html → Admin panel

## Deployment
Start command:
uvicorn backend:app --host 0.0.0.0 --port 10000
