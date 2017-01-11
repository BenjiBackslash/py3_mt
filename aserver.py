from fib import fib
from collections import deque
from select import select

tasks = deque()
recv_wait = {}
send_wait = {}

def run():
    while any([tasks, recv_wait, send_wait]):
        while not tasks:
            # No active tasks to run
            # wait for I/O
            can_recv, can_send, [] = select(recv_wait, send_wait, [])
            for s
        task = tasks.popleft()
        try:
            why, what = next(task)
            if why  == 'recv':
                  

