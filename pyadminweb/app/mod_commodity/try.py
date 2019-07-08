# 定义区块和区块链的方法
import time
from app.mod_commodity.blockchain_node import Block

from app.mod_commodity.blockchain_node import Blockchain

from app import chain_list

bc=Blockchain('123')
chain_list.append(bc)


block=Block('1','交易啊交易',time.time(),bc.last_block.hash)


# 将区块添加至链 参数  链名  区块  第几个区块
def addblock(Blockchain,block):
   proof_of_work=block.proof_of_work(block)
   Blockchain.add_block(block,proof_of_work)


addblock(bc,block)





