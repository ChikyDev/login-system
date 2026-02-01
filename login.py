#LOGIN INTERACTIVO

"""
Login interactivo en Python
- Registro de usuario
- Inicio de sesión con intentos limitados
"""


import sys  #importamos libreria sys

print('\n === ⚪​ REGISTRO ⚪​ ===') #Hacemos el menu de registro
usuario_guardado = input('Nombre de usuario:') 
contraseña_guardada = input('Contraseña: ')


intentos = 3 #Aqui hacemos los intentos para que el usuario solo tenga 3 intentos de inicio de sesion

print('\n === 🔵​ INICIO DE SESION 🔵​ ===') #Aqui hacemos el menu de inicio de sesion

while intentos > 0:
    
	user = input('Introduce tu nombre de usuario: ') #Pedimos las credenciales al usuario tanto como el user y contraseña
	contraseña = input('Introduce tu contraseña: ')

	if user == usuario_guardado and contraseña == contraseña_guardada: #Indicamos que si las credenciales de registro son las mismas, se inicia sesion
		print('Inicio de sesion exitoso ✅​')
		break
	else:  #Esto indica que si el usuario no indica las mismas credenciales, no se inicia sesion y se resta 1 intento 
		intentos -= 1
		print(f'Te quean {intentos} intentos')
		print('Lo siento, vuelve a intentarlo ​🔄​')

	if intentos == 0: #Indica que si los intentos llegan a 0, indica salir del programa
		print('Vuelve a intentarlo dentro de 5 min')
		sys.exit()
