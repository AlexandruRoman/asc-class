"""
    Create and run more than 1000 threads that work together. They share a list,
    input_list, and an integer variable.
    When they run, they each select one random item from the input list, that
    was not previously selected, and add it to that variable.
    When they finish, all elements in the list should have been selected.
    Make the critical section(s) as short as possible.

    Requirements:
        * the length of the input list is equal to the number of threads
        * the threads have a random delay when running (see time.sleep), before
            accessing the input_list, in the order of 10-100ms
        * before starting the threads compute the sum of the input list
        * after the threads stopped, the shared variable should be identical to
            the sum of the input list

    Hint:
        * In CPython some operations on data structures are atomic, some are
            not. Use locks when the operations are not thread-safe.
        * Useful links:
        https://docs.python.org/2/faq/library.html#what-kinds-of-global-value-mutation-are-thread-safe
"""

import random
from threading import Lock, Thread

global shared_var
shared_var = 0

def add(lista, lock, num_threads):
    global shared_var
    while 1:
        x = random.randint(0, num_threads-1)
        if lista[x][1] == False:
            lock.acquire()
            lista[x] = (lista[x][0], True)
            shared_var += lista[x][0]
            lock.release()
            break;

if __name__ == "__main__":

    #TODO provide the number of threads from the command line
    num_threads = 10
    initial_sum = 0
    my_lock = Lock()

    input_list = [(random.randint(0, 500), False) for i in range(num_threads)]
    for (x,_) in input_list:
        initial_sum = initial_sum + x
    print " ".join([str(x[0]) for x in input_list])


    # stocam obiectele Thread pentru a putea face join
    thread_list = []
    
    
    # pornim thread-urile
    for i in xrange(10):
        thread = Thread(target = add, args = (input_list, my_lock, num_threads))
        thread.start()
        thread_list.append(thread)
    
    # asteptam terminarea thread-urilor
    for i in xrange(len(thread_list)):
        thread_list[i].join()

    print initial_sum
    print shared_var