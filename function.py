#US-001/create_registrer

user = []

def user_register():
    id =  int(input("Agregue su id"))
    user.append(id)
    name = input("Agregue su nombre")
    user.append(name)
    last_name =  input("Agregue su apellido")
    user.append(last_name)
    email = input("Agregue su email")
    user.append(email)
    password = input("cree una contraseña de 8 caracteres entren numrs")
    print("Usuario creado")
    print (user)


def user_login():
    print("login")
