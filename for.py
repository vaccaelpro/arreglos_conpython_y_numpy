import time
import os
import os.sys

inicio=time.time()
for i in range(5):
    print(i)
fin=time.time()
print("Tiempo de ejecución:", fin-inicio)
if sys.platform == "win32":
    os.system('cls')
else:
    os.system('clear')
time.sleep(5)
os.system('cls')

inicio=time.time()
contador = 0
while contador<=10:
    print(contador)
    contador += 1
fin=time.time()
print("Tiempo de ejecución:", fin-inicio)

#liliana que haga silencio por favor