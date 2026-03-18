from fastapi import FastAPI, Header, HTTPException
from datetime import datetime

app = FastAPI()

# In-memory storage (rate limiting)
request_count = {}

# 🔐 Authentication
def verify_token(token: str = Header(...)):
    if token != "mysecret":
        raise HTTPException(status_code=401, detail="Unauthorized")

# 🚫 Rate Limiting
def check_rate_limit(user: str):
    if user not in request_count:
        request_count[user] = 1
    else:
        request_count[user] += 1

    if request_count[user] > 5:
        raise HTTPException(status_code=429, detail="Too many requests")

# 🌐 Dummy Data Collection
def get_market_data(sector: str):
    return f"Latest updates show growth in {sector} sector in India."

# 🤖 AI Analysis (dummy)
def analyze_with_ai(data: str, sector: str):
    return f"""
## 📊 {sector.capitalize()} Sector Market Analysis (India)

### 📝 Summary
The {sector} sector in India is experiencing steady growth.

### 📈 Opportunities
- Increasing demand
- Government support
- Investment growth

### ⚠️ Risks
- Market competition
- Economic changes
- Policy risks

### 🗓 Generated On
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""

# 🎯 Main Endpoint
@app.get("/analyze/{sector}")
def analyze_sector(sector: str, token: str = Header(...)):
    verify_token(token)
    check_rate_limit(token)

    data = get_market_data(sector)
    report = analyze_with_ai(data, sector)

    return {
        "sector": sector,
        "report_markdown": report
    }

# Home
@app.get("/")
def home():
    return {"message": "Trade Opportunities API Running"}