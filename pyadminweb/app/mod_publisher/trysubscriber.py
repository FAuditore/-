from app.mod_publisher.zmqsubscriber import subscriber
import zmq,json,threading,time

'''
zmqsb=subscriber('127.0.0.1',9000,'123')

context=zmq.Context()
zmqsb=context.socket(zmq.SUB)
zmqsb.connect("tcp://localhost:9000")
zmqsb.setsockopt(zmq.SUBSCRIBE,b'new_block')

while True:
    [address,contents]=zmqsb.recv_multipart()
    print("address:{},contents{}".format(address,contents))


zmqsb=subscriber('127.0.0.1',9000,'new_block')

zmqsb.sub_newblock()

zmqsb.write_newblock()

'''
'''
zmqsb=subscriber("127.0.0.1",9000,"new_block")

thread=threading.Thread(target=zmqsb.sub_newblock())

thread.start()

zmqsb2=subscriber("127.0.0.1",9001,"write_block")
thread2=threading.Thread(target=zmqsb2.write_newblock())

thread2.start()
'''
zmqsb3=subscriber("127.0.0.1",9003,"new_chain")
thread3=threading.Thread(target=zmqsb3.sub_newchain)
thread3.start()

zmqsb=subscriber("127.0.0.1",9000,"new_block")
thread=threading.Thread(target=zmqsb.sub_newblock)
thread.start()


zmqsb2=subscriber("127.0.0.1",9001,"write_block")

thread2=threading.Thread(target=zmqsb2.write_newblock)
thread2.start()