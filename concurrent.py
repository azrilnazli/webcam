from time import sleep
from threading import Thread


def CAM001():
    print('CAM001 : Starting a task...')
    sleep(1)
    print('done')

def CAM002():
    print('CAM002 : Starting a task...')
    sleep(1)
    print('done')


# create two new threads
t1 = Thread(target=CAM001)
t2 = Thread(target=CAM002)

# start the threads
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()