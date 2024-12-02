None
diccionario={"MELO":"bacano",
            "AGUACATE":"policia",
            "CUCHA":"vieja",
            "VOS":"tu",
           }
for i in range(5):
    word = input("ESCRIBE PALABRAS QUE NO ENTIENDAS(¡CON MAYUSCULA!):")


    if word in diccionario.keys():
        print(diccionario[word])

    else:
        print("¿Que palabra quiers averiguar?")
