frase = input("Danos una frase: ")
print("Tu frase tiene ", frase.count(" ")+1, " palabras")   #count() cuenta la cantidad de veces que aparece el texto entre paréntesis en el String
print("Tu frase tiene ", len(frase), " carácteres") #len() cuenta los caracteres de un String
print("Tu frase tiene ", len(frase) - frase.count(" "), " letras")