array = [[4, 7, 3], [8, 4, 5], [7, 6, 9]]
total = 0
for alumno in array:
    for nota in alumno:
        total = total + nota
    
print (total)
media = total / (len(array)*len(array[0]))
print(media)