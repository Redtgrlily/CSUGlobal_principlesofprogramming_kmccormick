from typing import List, Dict

sample_transactions: List[Dict] = [
    {'user_id': 'u1', 'amount':50.0},
    {'user_id': 'u1', 'amount':45.0},
    {'user_id': 'u1', 'amount':48.0},
    {'user_id': 'u1', 'amount':200.0}, #unusually large for u1
    {'user_id': 'u2', 'amount':100.0},
    {'user_id': 'u2', 'amount':95.0},
    {'user_id': 'u2', 'amount':110.0},
    {'user_id': 'u2', 'amount':500.0}, #unusually large for u2
    {'user_id': 'u3', 'amount':20.0},
    {'user_id': 'u3', 'amount':22.0},
    {'user_id': 'u3', 'amount':25.0},
    {'user_id': 'u3', 'amount':21.0}
]

def flag_large_transactions(transactions: List[Dict], threshold_multiplier: float = 1.8) -> List[Dict]:
    """
    Prep summary for DQ Prompt goal: 
    Flags transactions that are unusually large compared to the user's average transaction amount. 
    
    Params: 
        transactions (List[Dict]): List of transactions, each with 'amount' and 'user_id' keys. 
        threshold_multiplier (float): Multiplier for flagging large transactions.
        
    Return:
        List[Dict]: List of flagged transactions.
    """
    user_totals = {}
    user_counts = {}
    
    for tx in transactions:
        user_id = tx['user_id']
        amount = tx['amount']
        user_totals[user_id] = user_totals.get(user_id, 0) + amount
        user_counts[user_id] = user_counts.get(user_id, 0) + 1
        
    user_averages = {uid: user_totals[uid]/user_counts[uid] for uid in user_totals}
    
    flagged = [
        tx for tx in transactions
        if tx['amount'] > user_averages[tx['user_id']] * threshold_multiplier
    ]
    
    return flagged

flagged_transactions = flag_large_transactions(sample_transactions, threshold_multiplier=1.8)
print("Flagged transactions:")
for tx in flagged_transactions:
    print(tx)