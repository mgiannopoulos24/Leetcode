from typing import List

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # Parse the transactions into a list of dictionaries
        parsed_transactions = []
        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            parsed_transactions.append({
                'name': name,
                'time': int(time),
                'amount': int(amount),
                'city': city,
                'original': transaction
            })
        
        invalid = []
        
        # Check each transaction for invalidity
        for i, current in enumerate(parsed_transactions):
            if current['amount'] > 1000:
                invalid.append(current['original'])
                continue
            
            for j, other in enumerate(parsed_transactions):
                if i == j:
                    continue
                
                if (current['name'] == other['name'] and
                    current['city'] != other['city'] and
                    abs(current['time'] - other['time']) <= 60):
                    invalid.append(current['original'])
                    break
        
        return invalid