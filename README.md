# Trade Opportunities API

This is a FastAPI-based backend service that analyzes market data and provides trade opportunity insights for different sectors in India.

## Features
- FastAPI backend
- Sector-based analysis
- Rate limiting
- Token authentication
- Markdown report generation

## Endpoint
GET /analyze/{sector}

## Example
/analyze/technology

## Header
token: mysecret

## Run locally
pip install -r requirements.txt
uvicorn main:app --reload
