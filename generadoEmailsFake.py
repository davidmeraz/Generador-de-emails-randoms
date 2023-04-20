
# Generador de emails

import random

dominios = ["@gmail.com", "@hotmail.com"]
nombres = ["estrada", "meza", "jorge", "mendez","murillo","alfonso"]

def generadorNumero(cuantosNumerosQuieres):
   
    numerosRandoms = ""
    numeroRandom = ""

    for i in range(cuantosNumerosQuieres):
        numeroRandom = random.randint(0,9)
        numerosRandoms += str(numeroRandom)
    
    return numerosRandoms

def generadoremailsFakes(dominio):
    email = ""

    for i in range(0, 3):
        numeroA = random.randint(0,3)
        email += str(nombres[numeroA])
    pass

    email += str(generadorNumero(3))

    if dominio == "1":
        email += str(dominios[0])
    if dominio == "2":
        email += str(dominios[1])
    
    print(email)

def generarEmails(numerosEmails):

    dominio = input("Que domonio quieres 1:@gmail, 2:@hotmail: ")
    print(dominio)

    for i in range(0, numerosEmails):
        generadoremailsFakes(dominio)

generarEmails(10)