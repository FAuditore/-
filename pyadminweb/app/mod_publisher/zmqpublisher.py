import time
import zmq
import json
import os
import threading

_basepath = os.path.abspath(os.path.dirname(__file__))
conf = json.load(open(os.path.abspath(os.path.dirname(__file__))+"\\conf.json"))

class publisher:
    def __init__(self, bindserver,port,pub_key,pub_data=''):
        self.server = bindserver
        self.port = port
        #self.timestamp = mestamp
        self.key = pub_key
        self.data = pub_data

    def publish_newblock(self,block):
        context = zmq.Context()
        publisher = context.socket(zmq.PUB)
        publisher.bind("tcp://{}:{}".format(conf["server"],conf["port"]))

       # block_string = json.dumps(block['data'].__dict__, sort_keys=True)
        block_string = json.dumps(block.__dict__, sort_keys=True)
        print(block_string)
        i = 0
        while True:
         publisher.send_multipart([b'new_block', bytes(block_string,'utf-8')])
         time.sleep(1)
         print('正在进行第{}次发送'.format(i+1))
         i+=1
         if i==2:
            break

        publisher.close()
        context.term()
        print('新区块信息发送完毕')

    def publish_new_blockchain(self,blockchain):
        context=zmq.Context()
        publisher=context.socket(zmq.PUB)
        publisher.bind("tcp://{}:{}".format(conf["server"],conf["chain_port"]))
        chain_string=blockchain
        print("发布新链:{}".format(chain_string))
        i = 0
        while True:
            publisher.send_multipart([b'new_chain',bytes(chain_string,'utf-8')])
            time.sleep(1)
            i+=1
            if i==2:
                break
        publisher.close()
        context.term()

    def publish_write_newblock(self,block):
        context = zmq.Context()
        publisher = context.socket(zmq.PUB)
        publisher.bind("tcp://{}:{}".format(conf["server"],conf["write_port"]))

        block_string = json.dumps(block, sort_keys=True)
        print("让用户写:{}".format(block_string))
        i = 0
        while True:
            publisher.send_multipart([b'write_block', bytes(block_string,'utf-8')])
            time.sleep(1)
            print(i)
            i+=1
            if i==2:
                break

        publisher.close()
        context.term()

    def req_rep(self):
        while True:
            context = zmq.Context()
            socket = context.socket(zmq.REP)
            socket.bind("tcp://{}:{}".format(conf["server"], conf["signal_port"]))
            #  Wait for next request from client
            time.sleep(1)
            data = socket.recv()
            data_str = data.decode(encoding="utf-8")
            print("接收到客户消息:{}".format(data_str))
            if  'finished' in data_str:
                #time.sleep(10)
                data_obc = json.loads(data_str)

                pub_write = publisher(conf["server"],conf["write_port"],'')

                pub_write.publish_write_newblock(data_obc['finished'])
                socket.close()
                context.term()

            elif 'new_block' in data_str:
                # time.sleep(10)
                data_obc = json.loads(data_str)

              #  pub_write = publisher(conf["private_server"], conf["write_port"], '')

              # pub_write.publish_write_newblock(data_obc['finished'])
                pub_write=publisher(conf["server"],conf["port"],'')

                pub_write.publish_newblock(data_obc)

                socket.close()
                context.term()
            elif 'new_chain' in data_str:
                data_obc=json.loads(data_str)

                pub_write=publisher(conf["server"],conf["chain_port"])

                pub_write.publish_new_blockchain(data_obc)

                socket.close()
                context.term()

# 发送新区块时调用
'''
zmqnew=publisher(conf["server"],conf["port"])
zmqnew.publish_newblock(block)
'''
# 接收用户计算返回哈希值时调用  接收用户发送新区快产生时调用
'''
zmqrep=publisher(conf["server"],conf["signal_port"])
zmqrep.req_rep()
'''

#确认一位用户发来的哈希值有效后发布新区块时调用 req_rep会自动调用
'''
zmqpub=publisher(conf["server"],conf["write_port"])
zmqpub.publish_write_newblock(block)
'''
#死循环线程接收用户请求和响应以及发布新区快消息的线程
'''
_req_rep_pub=publisher(conf["server"],conf["port"])
_req_rep_thread=threading.Thread(target=_req_rep_pub.req_rep())
_req_rep_thread.start()
'''
