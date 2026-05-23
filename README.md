# Telegram Image Generation Bot

A Telegram bot that generates images from text prompts using AI.

## Setup

1. **Clone the repo**
```bash
git clone https://github.com/oxforddev/telegram-image-gen-bot.git
cd telegram-image-gen-bot
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment**
```bash
cp .env.example .env
# Edit .env and add your BOT_TOKEN
```

4. **Get a Bot Token**
- Open @BotFather on Telegram
- Use /newbot command
- Copy the token and add it to .env

5. **Run the bot**
```bash
python main.py
```

## Usage

- Send `/start` to begin
- Send any text prompt to generate an image
- Example: "a futuristic city with flying cars"

## Deploying

### Option 1: Render (Free)
1. Push to GitHub
2. Connect to Render
3. Set start command: `python main.py`
4. Add BOT_TOKEN in env vars

### Option 2: Railway
1. Connect GitHub repo
2. Add BOT_TOKEN env var
3. Deploy

### Option 3: VPS/DigitalOcean
```bash
apt update && apt install python3 python3-pip git
git clone <your-repo>
cd telegram-image-gen-bot
pip install -r requirements.txt
nohup python main.py &
```

## License
MIT