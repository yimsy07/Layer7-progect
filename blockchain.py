import hashlib
import json
from time import time  # time 모듈 임포트 수정

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []  # 변수명 수정
        self.create_block(previous_hash='1', proof=100)

    def create_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = []
        self.chain.append(block)
        return block

    def create_transaction(self, sender, recipient, amount):  # 함수명 수정
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    def hash(self, block):  # self 추가
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def last_block(self):  # self 추가
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    def valid_proof(self, last_proof, proof):  # 함수명 및 self 추가
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

# 코드에 있는 잘못된 부분을 수정한 후에 아래 부분은 들여쓰기가 잘못되어 있습니다.
# 아래 부분은 인스턴스를 생성하는 부분이므로 들여쓰기를 조정하였습니다.

blockchain = Blockchain()
blockchain.create_transaction('Layer7', 'Teamlog', 1)
blockchain.create_transaction('Teamlog', 'Unifox', 0.5)
proof = blockchain.proof_of_work(blockchain.last_block()['proof'])  # 함수 호출 수정
blockchain.create_transaction('Unifox', 'Layer7', 0.2)
block = blockchain.create_block(proof)

for block in blockchain.chain:
    print(block)



    import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, proof):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.proof = proof
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.proof}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(1, "0", time.time(), "Genesis Block", 0)

    def create_block(self, proof):
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = time.time()
        data = f"Block #{index}"
        return Block(index, previous_block.hash, timestamp, data, proof)

    def proof_of_work(self, previous_proof):
        proof = 0
        while self.valid_proof(previous_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(previous_proof, proof):
        guess = f"{previous_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

# 블록체인 초기화
blockchain = Blockchain()

# 작업 증명을 통한 블록 생성
previous_block = blockchain.chain[-1]
proof = blockchain.proof_of_work(previous_block.proof)
block = blockchain.create_block(proof)
blockchain.chain.append(block)

# 블록체인 출력
for block in blockchain.chain:
    print(f"Block #{block.index} | Hash: {block.hash} | Proof: {block.proof}")





    import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(previous_hash='1', proof=100)

    def create_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = []
        self.chain.append(block)
        return block

    def create_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

# 사용 예시
blockchain = Blockchain()
blockchain.create_transaction('Alice', 'Bob', 1)
blockchain.create_transaction('Bob', 'Charlie', 0.5)
proof = blockchain.proof_of_work(blockchain.last_block['proof'])
blockchain.create_transaction('Charlie', 'Alice', 0.2)
block = blockchain.create_block(proof)

# 더블 스펜딩 공격 시뮬레이션
# 같은 코인을 여러 번 사용하여 블록체인을 속인다고 가정
blockchain.create_transaction('Alice', 'Bob', 1)  # 동일한 거래를 다시 시도

# 블록체인 출력
for block in blockchain.chain:
    print(block)
