import datetime as date
import proof_of_work as pw

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hashs = pw.hash_md5_with_PoW(data)
        
    def create_genesis_block():
        return Block(0, date.datetime.now(), "Genesis Block", "0")
    
    def gethash(self):
        return self.hashs
    
    def getIndex(self):
        return self.index
    
    def getdata(self):
        return self.data
    
    def getphash(self):
        return self.previous_hash
    
    def getTs(self):
        return self.timestamp.strftime("%m/%d/%Y, %H:%M:%S")
    
    def __str__(self):
        return [self.index, self.data, self.hashs, self.previous_hash, self.getTs()]