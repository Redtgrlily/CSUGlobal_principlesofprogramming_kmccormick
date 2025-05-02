transaction = {
    "id": 1001,
    "amount": 980.00,
    "signals": [0.8, 0.6, 0.9, 0.2]
}

risk_signals = transaction["signals"]

fraud_risk_score = sum(risk_signals) / len(risk_signals)

if fraud_risk_score > 0.7:
    decision = "FLAGGED FOR REVIEW"
elif fraud_risk_score > 0.4:
    decision = "REQUIRES 2ND LEVEL REVIEW"
else:
    decision = "APPROVED"
    
print(f"Transaction ID: {transaction['id']}")
print(f"Fraud Risk Score: {fraud_risk_score:.2f}")
print(f"Decision: {decision}")