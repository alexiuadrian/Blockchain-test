import hashlib

class Block:
    def __init__(self, previous_hash, transaction):
        self.transaction = transaction
        self.previous_hash = previous_hash
        transactions_string = "".join(transaction) + previous_hash
        self.block_hash = hashlib.sha256(transactions_string.encode()).hexdigest()