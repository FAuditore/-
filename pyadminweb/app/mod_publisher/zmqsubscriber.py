import zmq
import threading
import json
from hashlib import sha256
import os
import time
from app.mod_commodity.blockchain_node import Blockchain,writeBlock
from app.mod_commodity.blockchain_node import Block
from app import chain_list

_basepath = os.path.abspath(os.path.dirname(__file__))
conf = json.load(open(os.path.abspath(os.path.dirname(__file__))+"\\conf.json"))



class subscriber:
    def __init__(self, bindserver,port,pub_key):
        self.server = bindserver
        self.port = port
        self.key = pub_key

    def sub_newchain(self):
        context=zmq.Context()
        subscriber=context.socket(zmq.SUB)
        subscriber.connect("tcp://{}:{}".format(self.server,self.port))
        subscriber.setsockopt(zmq.SUBSCRIBE,bytes(self.key,'utf-8'))

        while True:
            time.sleep(1)
            [address, contents] = subscriber.recv_multipart()
            print("[%s] %s" % (address, contents))
            print(str(contents,encoding='utf-8'))
            bc=Blockchain(str(contents,encoding='utf-8'))
            chain_list.append(bc)

    #sub new block event
    def sub_newblock(self):
        # Prepare our context and subscriber
        context = zmq.Context()
        subscriber = context.socket(zmq.SUB)
        subscriber.connect("tcp://{}:{}".format(self.server,self.port))
        subscriber.setsockopt(zmq.SUBSCRIBE, bytes(self.key,'utf-8'))


        while True:
            time.sleep(1)
            # Read envelope with address
            [address, contents] = subscriber.recv_multipart()
            print("[%s] %s" % (address, contents))
            compute_hash(self,contents)

        subscriber.close()
        context.term()


    #sub write event
    def write_newblock(self):
        context = zmq.Context()
        subscriber = context.socket(zmq.SUB)
        subscriber.connect("tcp://{}:{}".format(self.server, self.port))
        subscriber.setsockopt(zmq.SUBSCRIBE, bytes(self.key, 'utf-8'))
        while True:
            time.sleep(1)
            # Read envelope with address
            [address, contents] = subscriber.recv_multipart()
            print("[%s] %s" % (address, contents))
            write_blockfile(contents)

        subscriber.close()
        context.term()


def compute_hash(self,data):
    """
    A function that return the hash of the block contents.
    """
    #block_string = self.transactions+str(self.nonce)
    block_object = json.loads(data)
    computed_hash = sha256(str(data,'utf-8').encode()).hexdigest()
    while not computed_hash.startswith('0' * 5):

        block_object['nonce'] +=1
        ee = json.dumps(block_object)
        computed_hash = sha256(ee.encode()).hexdigest()
       # print(computed_hash)
    print('最终结果是:{}, 随机数:{}'.format(computed_hash, block_object['nonce']))

    # send signal of status,FIFO
    # time.sleep(10)
    send_finish_status(self,block_object)

    return computed_hash


# send signal
def send_finish_status(self,block_object):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://{}:{}".format(self.server, 9002))
    print('fdsfffffffffffffff===',type(block_object),block_object)
    block_dict = {}
    block_dict['finished'] = block_object
    block_string = json.dumps(block_dict)
    print("已向服务器发送:{}".format(block_string))
    socket.send(bytes(block_string,'utf-8'))


def write_blockfile(data):
    obj_data = json.loads(data.decode(encoding="utf-8"))
   # print('the file ==================\n',obj_data," and index is ",json.dumps(obj_data,indent=2,ensure_ascii=False))
   #  with open(_basepath+'\\block'+str(obj_data['index'])+'.txt', 'w',encoding="utf-8") as f:
   #     f.write(json.dumps(obj_data,indent=2,ensure_ascii=False))
    for blockchain in chain_list:
        if blockchain.chainName ==obj_data['belongchain']:
            bl=Block(obj_data['index'],
                     obj_data['transactions'],
                     obj_data['timestamp'],
                     obj_data['previous_hash'],
                     obj_data['nonce'],
                     obj_data['belongchain'])
            writeBlock(blockchain.chainName,bl)
            break




# 发送新区块信息时调用 将新区块发给所有用户一起算
def send_new_node(self,block_object):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
  #  socket.connect("tcp:/{}:{}".format(self.server,self.port))
    socket.connect("tcp:/{}:{}".format(self.server,9002))
    block_dict = {}
    block_dict['new_block'] = block_object
    block_string = json.dumps(block_dict)
    socket.send(bytes(block_string,'utf-8'))

def send_new_chain(self,chain_object):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
  #  socket.connect("tcp:/{}:{}".format(self.server,self.port))
    socket.connect("tcp:/{}:{}".format(self.server,9002))
    chain_dict = {}
    chain_dict['new_chain'] = chain_object
    chain_string = json.dumps(chain_dict)
    socket.send(bytes(chain_string,'utf-8'))

'''
# 运用线程一个负责接收区块信息并计算反馈给服务器 一个负责接收确认有效的区块保存
print('消息服务器',conf["server"])
_newblock_sub = subscriber(conf["server"],conf["port"],"new_block")
# instead of s.sub_newblock(),we use thread fun,avoid locking
_newblock_thread = threading.Thread(target=_newblock_sub.sub_newblock)
_newblock_thread.start()


_writeblock_sub = subscriber(conf["server"],conf["write_port"],"write_block")
_writeblock_thread = threading.Thread(target=_writeblock_sub.write_newblock)
_writeblock_thread.start()
'''