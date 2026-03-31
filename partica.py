#listas
frutas = ["manzana","banana","cereza"]
frutas.append("naranja")
print(frutas)
frutas[0] = "pera"
print(frutas)
frutas.remove(frutas[0])
print(frutas)

#tuplas
punto = (10,20)
print(punto)
tupla = punto + (30,40)
print(tupla)

#diccionarios
usuario = {"nombre": "david" ,"edad": 20, "ciudad":"barranquilla" }
print(usuario["edad"])
usuario["profesion"] = "programador"
print(usuario)
usuario["ciudad"] = "panama"
print(usuario)

#ejericico nivel pro
diccionarios = [{"nombre":"david", "hobbies": ("caminar","dormir")} , {"nombre":"juan", "hobbies": ("comer","correr")}, {"nombre":"mauricio", "hobbies": ("tomar","fumar")}]
print(diccionarios)