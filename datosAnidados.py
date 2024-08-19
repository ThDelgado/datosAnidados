#lista de estudiantes
estudiantes = [
    {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]}, 
    {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]}, 
    {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]}, 
    {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]}, 
    {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]}, 
]

# evaluando los estudiantes mayores de 18 años y con promedio mayor que 85
print ("los estudiantes mayores de 18 años y con promedio mayor que 85 son: ")
for estudiante in estudiantes: 
    if (estudiante["edad"] > 18) and (sum(estudiante["calificaciones"]) / len(estudiante["calificaciones"])) > 85:
        print (estudiante)

# evaluando a los estudiantes mayores de 18 años y numero primo de edad
print()
print ("los estudiantes mayores de 18 años y numero primo de edad son: ")
for estudiante in estudiantes: 
    if (estudiante["edad"] > 18) and ( estudiante["edad"] %  estudiante["edad"] == 0 and  estudiante["edad"] % 1  == int and estudiante["edad"] % 2 == int and estudiante["edad"] % 3 == int):        
         print (estudiante)
    else:
        print ("no hay estudiantes mayores de 18 con edad numero primo")
        break

    
 

