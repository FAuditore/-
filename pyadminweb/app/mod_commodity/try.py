# 定义区块和区块链的方法
import time
from app.mod_commodity.blockchain_node import Block

from app.mod_commodity.blockchain_node import Blockchain


bc=Blockchain('123')
block=Block('4','交易啊交易',time.time(),bc.last_block.hash)
# 将区块添加至链 参数  链名  区块  第几个区块
def addBlock(Blockchain,block):
 proof_of_work=block.proof_of_work(block)
 Blockchain.add_block(block,proof_of_work)

addBlock(bc,block)

'''
 from app.mod_publisher.zmqpublisher import publisher

print(b"B",bytes(json.dumps(bl),'utf-8'))

zmqpb=publisher('*','9000','123',pub_data=bl.transactions)

zmqpb.publish_newblock()

zmqpb.publish_write_newblock(bl)

zmqpb.req_rep()
'''

