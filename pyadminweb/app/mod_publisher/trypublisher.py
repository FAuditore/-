from app.mod_publisher.zmqpublisher import publisher
from app.mod_commodity.blockchain_node import Block

from app.mod_commodity.blockchain_node import Blockchain
import time,zmq
'''
zmqpb=publisher('*','9000','123',pub_data='hahahah')
context=zmq.Context()

zmqpb=context.socket(zmq.PUB)
zmqpb.bind("tcp://*:9000")
i=0
while True:
 zmqpb.send_multipart([b'new_block',b"nihao"])
 time.sleep(2)
 print(i)
 i+=1

'''

'''
bc=Blockchain('123')

block=Block('1','交易啊交易',time.time(),'0')

zmqpb=publisher('127.0.0.1',9000,'new_block',pub_data='123')

zmqpb.publish_newblock(block)

zmqpb.req_rep()

zmqpb.publish_write_newblock(bc)

'''
