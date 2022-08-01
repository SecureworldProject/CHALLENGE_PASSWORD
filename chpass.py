from math import log10, sqrt

import os
from pathlib import Path
import time
#para instalar el modulo easygui simplemente:
#pip3 install easygui
# o bien py -m pip install easygui
import easygui 

# variables globales
# ------------------
props_dict={} 
DEBUG_MODE=True

def init(props):
    global props_dict
    print("Python: Enter in init")
    
    #props es un diccionario
    props_dict= props
    res=executeChallenge()
    #check len retornada 
    if (res[1]>0):
        return 0
    else:
        #no se ha podido ejecutar
        return -1



def executeChallenge():
    print("Starting execute")
    
    
    #mecanismo de lock BEGIN, para garantizar una sola interaccion con user a la vez
    #-----------------------
    folder=os.environ['SECUREMIRROR_CAPTURES']
    while os.path.exists(folder+"/"+"lock"):
        time.sleep(1)
    Path(folder+"/"+"lock").touch()

    #pedimos password
    clave = easygui.enterbox("enter password", "chpass", "")

    #mecanismo lock
    os.remove(folder+"/"+"lock")
    
    #ahora comparamos con la correcta
    correcta=props_dict["param1"]

    #construccion de la respuesta
    mode= props_dict["mode"]

    if (mode=="parental"):
        for i in range (0,2): # 3 intentos        
            if (clave==correcta):
                cad="%d"%(0)
                break
            else:
                clave = easygui.enterbox("enter password", "chpass", "")
                
        if (clave!=correcta):
            cad="%d"%(1)
            
    else:#modo no parental
        cad=clave
    
    key = bytes(cad,'utf-8')
    key_size = len(key)

    result =(key, key_size)
    print ("result:",result)
    return result



    


if __name__ == "__main__":
    #mode "parental" o "normal"
    midict={"param1": "clavesecreta", "mode":"parental"}
    init(midict)
    #executeChallenge()

