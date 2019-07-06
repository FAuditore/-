from app.mod_publisher.zmqsubscriber import subscriber
import zmq

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
