#src/main.py 

import os

# obtener entrada
valor= os.version.get("Input_Value")

# mostrar resultado en consola
if "GITHUB_OUTPUT" in os.environ: 
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        print("{0}=Hola {1}".format('result', valor), file=f) 
print("hola")
print("chao")