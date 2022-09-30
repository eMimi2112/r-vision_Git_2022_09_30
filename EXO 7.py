# EXO 125: Créez une liste contenant 5 nombres de 1 à 5.
# Affichez la liste.
 

numbers = [5, 4, 3, 2, 1,]
print(numbers)

#Tant que la liste n'est pas vide (ex: tant que sa longueur est > 0):
# Retirez le premier élément de la liste
# Affichez l'élément retiré de la liste
# Affichez la liste


while len(numbers) > 0 :
    removed = numbers.pop(0)
    print(removed)
    print(numbers)


# Ici, pour exprimer une fct de longueur, nous parlons de "len"
# attention aux variables, le print finale d'affichage de liste
# doit etre inclus dans la boucle