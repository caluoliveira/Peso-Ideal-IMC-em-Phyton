#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal com base no IMC.
#IMC= Peso / Altura²

peso=float(input("Insira seu PESO ideal: \n"))
altura=float(input("Insira sua ALTURA:     \n"))
pesoideal=(peso/(altura*altura))
print("Seu peso ideal é de:", "%.2f" % pesoideal, "para atingi-lo você precisa perder", "%.2f" %(peso - pesoideal), "quilos.")