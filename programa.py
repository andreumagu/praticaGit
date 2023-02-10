print("Bienvenido al Módulo de validación de contraseñas en Python")
contraseña = input("Por favor, ingrese su contraseña: ")

if len(contraseña) < 8:
  print("Contraseña muy corta, debe tener más de 8 carácteres ")

else:
  minuscula = False
  for minus in contraseña:
    if minus.islower() == True:
      minuscula = True
  if not minuscula:
    print("La contraseña debe contener al menos una minúscula")
  mayusculas = False
  for mayus in contraseña:
    if mayus.isupper() == True:
      mayusculas == True
  if not mayusculas:
    print("La contraseña debe tener al menos una mayúscula")
num = False
for carac in contraseña:
  if carac.isdigit() == True:
    num = True
if not num:
  print("La contraseña debe tener al menos un numero")
if contraseña.count(" ") > 0:
  print("La contraseña no puede contener espacios en blanco")
else:
  print("Contraseña segura")
