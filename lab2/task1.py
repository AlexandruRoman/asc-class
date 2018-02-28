#a) Folosind clasa Thread, creati 10 threaduri care afiseaza un mesaj de forma:
#    Hello, I'm thread id_thread

#b) Modificati codul anterior astfel incat thread-urile sa primeasca un 
#   index si un mesaj date ca parametru sub forma de dictionar
#   *hint: exemplu in lab1 http://cs.curs.pub.ro/wiki/asc/asc:lab1:index#functii

#c) Modificati codul anterior astfel incat thread-urile sa afiseze si numele
#   thread-ului (campul 'name' din clasa Thread)

#d) Modificati codul anterior astfel incat thread-urile sa primeasca index-ul
#   drept nume al thread-ului, afisati-l ca la punctul b)
#   * hint: folositi campul 'name' al constructorului clasei Thread

from threading import *


def afiseaza(dict):
    # print "hello, i'm thread ", dict['index'] , " ", dict['mesaj']
    print current_thread().getName()

thread_list = []

# pornim thread-urile
for i in xrange(10):
    thread = Thread(target = afiseaza, name="efe", args = ({"index": i, "mesaj":"random message"}, ))
    thread.start()
    thread_list.append(thread)
 
# asteptam terminarea thread-urilor
for i in xrange(len(thread_list)):
    thread_list[i].join()