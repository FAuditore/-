from app.mod_publisher.zmqpublisher import publisher
from app.mod_commodity.blockchain_node import Block

from app.mod_commodity.blockchain_node import Blockchain
import time,zmq,threading
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

zmqpb=publisher('127.0.0.1',9000,'new_block')

zmqpb.publish_newblock(block)

zmqpb.req_rep()

'''

block=Block('1','交易啊交易',time.time(),'0',0,'haha')


zmqpb=publisher("127.0.0.1",9000,'')

zmqpb.publish_new_blockchain('haha')


thread=threading.Thread(target=zmqpb.publish_newblock(block))
thread.start()

thread2=threading.Thread(target=zmqpb.req_rep)
thread2.start()


