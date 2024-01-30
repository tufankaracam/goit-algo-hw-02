from queue import Queue
from uuid import uuid4
import os

client_order = Queue()


def clear_screen():
    os_name = os.name
    if os_name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def generate_request():
    new_order_id = uuid4()
    client_order.put(new_order_id)
    input(f'Request created with id : {new_order_id}.')


def process_request():
    if not client_order.empty():
        request = client_order.get()
        input(f'{request} is completed!')
    else:
        input('Queue is empty!')


clear_screen()
while True:
    print(f'1) Generate Request')
    print(f'2) Process Request')
    print(f'3) Quit')
    cmd = input()
    if cmd == '1':
        generate_request()
    elif cmd == '2':
        process_request()
    elif cmd == '3':
        quit()
    clear_screen()
