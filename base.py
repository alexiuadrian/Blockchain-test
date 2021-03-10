from block import Block

blockchain = []

genesis_block = Block("But it ain’t how hard you hit; it’s about how hard you can get hit, and keep moving forward. How much you can take, and keep moving forward. That’s how winning is done.", ["Elon Musk sent 1 TEST to Satoshi"])

second_block = Block(genesis_block.block_hash, ["Adi sent 5 TEST to Elon Musk"])

third_block = Block(second_block.block_hash, ["Emperor Palpatin sent 0.5 TEST to Anakin"])

print("Genesis block hash: " + genesis_block.block_hash)
print("Second block hash: " + second_block.block_hash)
print("Third block hash: " + third_block.block_hash)