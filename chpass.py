from math import log10, sqrt

import os
from pathlib import Path
import time
#para instalar el modulo easygui simplemente:
#pip3 install easygui
# o bien py -m pip install easygui
import easygui 
import lock


# variables globales
# ------------------
props_dict={} 
DEBUG_MODE=True

def init(props):
    global props_dict
    print("Python: Enter in init")
    
    #props es un diccionario
    props_dict= props

    return 0
    """
    res=executeChallenge()
    #check len retornada 
    if (res[1]>0):
        return 0
    else:
        #no se ha podido ejecutar
        return -1
    """


def executeChallenge():
    print("Starting execute")
    
    
    #mecanismo de lock BEGIN, para garantizar una sola interaccion con user a la vez
    #-----------------------
    lock.lockIN("chpass")
    """
    folder=os.environ['SECUREMIRROR_CAPTURES']
    while os.path.exists(folder+"/"+"lock"):
        time.sleep(1)
    Path(folder+"/"+"lock").touch()
    """
    #pedimos password
    clave = easygui.enterbox("enter password", "chpass", "")

    #mecanismo lock out
    lock.lockOUT("chpass")
    """
    if os.path.exists(folder+"/"+"lock"):
        os.remove(folder+"/"+"lock")
    """
    #ahora comparamos con la correcta
    correcta=props_dict["clave"]

    #construccion de la respuesta
    mode= props_dict["mode"]

    if (mode=="parental"):
        for i in range (0,2): # 3 intentos        
            if (clave==correcta):
                cad="\0" #bytearray(0) #"%d"%(0)
                break
            else:
                clave = easygui.enterbox("enter password", "chpass", "")
                
        if (clave!=correcta):
            cad="\1" #"%d"%(1)
        else :
            cad="\0" #"%d"%(0)
            
    else:#modo no parental
        cad=clave
    
    key = bytes(cad,'utf-8')
    key_size = len(key)

    result =(key, key_size)
    print ("result:",result)
    return result



    


if __name__ == "__main__":
    #mode "parental" o "normal"
    midict={"clave": "clavesecreta", "mode":"parental"}
    init(midict)
    executeChallenge()

