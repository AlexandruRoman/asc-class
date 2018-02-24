#
# Scrieti un program in care mai multe threaduri (numarul lor este dat ca
# argument in linia de comanda) aleg random un element dintr-o lista comuna si
# le adauga intr-o lista rezultat (tot comuna).
# a) in fiecare thread, afisati numele threadului si varianta din acel moment 
#    a listei rezultat
# b) in fiecare thread adunati elementul la o variabila globala. Protejati 
#    accesul la aceasta printr-un lock
# c) faceți thread-urile sa aștepte un număr random de secunde până să înceapă
#    execuția. Hint: modulul time
# !!! Verificati ca suma calculata in vareiabila globala este egala cu suma 
#    elementelor din lista rezultat. Rulati cu 1000 de threaduri.   
#
