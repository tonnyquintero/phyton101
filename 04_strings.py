name = "Anthony"
last_name = "Quintero"

full_name = name + " " + last_name
print(full_name)

#format
template = "Hola mi nombre es " + name + " y mi apellido es " + last_name
print("v1 ", template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name,last_name)
print("v2 ", template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print("v3 ", template)