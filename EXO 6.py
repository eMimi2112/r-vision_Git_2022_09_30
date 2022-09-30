#Créez une liste contenant 10 nombres de 1 à 5.
# Affichez la liste.
numbers = [-5, -4, -3, -2, -1, 0, 1, 5]
print(numbers)

# Demandez à l'utilisateur d'entrer un nombre au clavier.
#Retirez le nombre entré de la liste.
# Affichez la liste finale.

number = int(input("Entrez un nombre svp"))
numbers.remove(number)
print(numbers)


# Note: Que se passe-t-il quand vous essayez de retirer un 
# nombre qui n'est pas dans la liste
# ==> le nombre n'est pas dans la liste