from threading import Lock, Thread
 
def inc(lista, lock, index, n):
    """ Incrementeaza elementul index din lista de n ori """
    for i in xrange(n):
        lock.acquire()
        lista[index] += 1
        lock.release()
 
 
def dec(lista, lock, index, n):
    """ Decrementeaza elementul index din lista de n ori """
    for i in xrange(n):
        lock.acquire()
        lista[index] -= 1
        lock.release()
 
# lista si lock-ul care o protejeaza
my_list = [0, 1]
my_lock = Lock()
 
# thread-urile care modifica elemente din lista
t1 = Thread(target = inc, args = (my_list, my_lock, 0, 100000))
t2 = Thread(target = dec, args = (my_list, my_lock, 1, 100000))
 
# lista inainte de modificari
print my_list
 
t1.start()
t2.start()
 
t1.join()
t2.join()
 
# lista dupa modificari
print my_list