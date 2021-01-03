import hashlib

#check if first 4 digit is 0
def proof_of_work(hash_val):
    return hash_val[0]==str(0) and hash_val[1]==str(0) and hash_val[2]==str(0) and hash_val[3]==str(0)

#generate a list of num from 0 to 100000000000000000000,
#if a 0000 hash val was found return it, else just return a the hash val of the original data

def hash_md5_with_PoW(data):
    for nonce in range(100000000000000000000): 
        if proof_of_work(hashlib.md5((data+str(nonce)).encode()).hexdigest()):
            hash_val = hashlib.md5((data+str(nonce)).encode()).hexdigest()
            return hash_val
    return hashlib.md5(data.encode()).hexdigest()

