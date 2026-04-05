# Adaptive Firewall Prototype(DEMO)

This project is a prototype of a hybrid adaptive firewall that combines:
- rule-based threat detection
- anomaly detection
- explainable decisions
- secure temporary override simulation

## Features
- Reads traffic events from CSV
- Calculates rule-based risk score
- Uses AI anomaly detection
- Makes ALLOW / WARN / VERIFY / BLOCK decisions
- Explains why a decision was made
- Simulates temporary override for verified users

## Files
- `app.py` - main program
- `rules.py` - rule-based scoring
- `detector.py` - anomaly detection
- `decision.py` - decision logic
- `explain.py` - explanation generator
- `override.py` - temporary override logic

## Run
```bash
python aprfrwal.py
