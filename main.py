import json
from hashlib import sha256 as sha
# Class Block will contain information about the block
# index - index of the block in blockchain
# data - Data that is to be stored on blockchain
# Previous Hash - Previous hash of the block
# Nonce - key that makes block unique
class Block:
    ''' Class Block creats the object of block that is to added to blockchain. '''
    def __init__(self, index, data, timestamp, previous_hash, nonce=0):
        self.index = index
        self.data = data
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


B = Block(0,"Hello World","10:22","ASBASDKG",10)

print(B.__dict__)