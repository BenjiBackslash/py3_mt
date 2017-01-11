from socket import *
from fib import fib
from threading import Thread
import concurrent.futures
from test.libregrtest.save_env import multiprocessing

executor = concurrent.futures.ProcessPoolExecutor()


def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print("Connection", addr)
#         Thread(target=fib_handler, args=(client,), ).start()
        fib_handler(client)

        
def fib_handler(client):    
    while True:
        req = client.recv(100)
        if not req:
            break
        n = int(req)
#         print('fib_handler')
#         print('executor')
#         print(executor)
#         future = executor.submit(fib,n)
#         result =  future.result()
        result = fib(n)
        resp = str(result).encode('ascii') + b'\n'
        client.send(resp)
        
if __name__ == "__main__":
    multiprocessing.freeze_support()
    fib_server(('',25003))


        
    