import os

autos = []
tipos = []
patentes = []
marcas = []
precios = []
fechas_registro = []
nombres = []
apellidos = []
multas = []

def menu():
    print("Bienvenido a la automotora 'Auto Seguro'")
    print("-"*40)
    print("                ~ MENÚ ~")
    print("")
    print("[1] Grabar vehículo")
    print("[2] Buscar auto")
    print("[3] Imprimir certificados")
    print("[4] Salir")
    print("")
    print("-"*40)
    print("Escoja una opción")
    opc1 = int(input("Opción N°: "))
    return opc1

def grabar():
    while True:
      try:
        tipo = input("Ingrese el tipo de auto: ")
        if tipo != "" and tipo.isalnum():
          break
        else:
          print("Ingrese un tipo válido.")
      except:
         print("Error. Intente nuevamente.")

    tipos.append(tipo)
    
    while True:
      try:
        patente = input("Ingrese la patente: ").upper()
        if patente != "" and len(patente) == 6:
          break
        else:
          print("Ingrese una patente válida.")
      except:
         print("Error. Intente nuevamente.")

    patentes.append(patente)

    while True:
      try:
        marca = input("Ingrese la marca del auto: ")
        if marca != "" and len(marca) >= 2 and len(marca) <= 15:
          break
        else:
          print("Ingrese una marca válida. Va entre 2 a 15 caracteres.")
      except:
         print("Error. Intente nuevamente.")

    marcas.append(marca)
    
    while True:
      try:
        precio = input("Ingrese el precio del auto: ")
        if precio != "" and precio.isdigit() and int(precio) > 5000000:
          break
        else:
          print("Ingrese un precio válido. Debe ser mayor a $5.000.000")
      except:
         print("Error. Intente nuevamente.")

    precios.append(precio)

    print("Ingrese fecha de registro del vehículo. Sólo los dígitos, sin '-' o '/'")
    while True:
      try:
        fecha_regist = input("Fecha: ")
        if fecha_regist != "" and fecha_regist.isdigit() and len(fecha_regist) == 6:
           break
        else:
           print("Ingrese una fecha válida. Ej: 160822")
      except:
         print("Error. Intente nuevamente.")

    print(f"La fecha queda registrada como: {fecha_regist}")
    fechas_registro.append(fecha_regist)

    print("Ingrese el nombre del dueño del vehículo.")
    while True:
      try:
        nombre = input("Nombre: ")
        if nombre != "" and nombre.isalpha():
           break
        else:
           print("Ingrese un nombre válido.")
      except:
         print("Error. Intente nuevamente.")

    nombres.append(nombre)
    print("Ingrese el apellido del dueño del vehículo.")
    while True:
      try:
        apellido = input("Apellido: ")
        if apellido != "" and nombre.isalpha():
           break
        else:
           print("Ingrese un apellido válido.")
      except:
         print("Error. Intente nuevamente.")

    apellidos.append(apellido)
    autos.extend(patentes)
    autos.extend(marcas)
    autos.extend(precios)
    autos.extend(fechas_registro)
    autos.extend(nombres)
    autos.extend(apellidos)
    print(autos)
    os.system("cls")

def mostrar_multas():
  print("¿El auto tiene multas?")
  print("[1] Sí")
  print("[2] No")
  print("Escoja una opción")
  opc2 = int(input("Opción N°: "))
  return opc2

def multa():
  mult = []
  print("¿Cuántas multas tiene el vehículo? Ingrese el número.")
  num_multas = int(input("N° multas: "))
  os.system("cls")
  print(f"El vehículo tiene registrado {num_multas} multa(s) en total.")
  while num_multas > 0:
    print("Ingrese el monto y fecha de la multa")
    print("")
    print("~ MONTO DE LA MULTA ~")
    while True:
      try:
          monto = int(input("$ "))
          if monto != "" and monto >= 1500 and monto <= 3500:
           break
          else:
           print("Ingrese un monto válido. Debe estar entre los valores $1.500 y $3.500")
      except:
         print("Error. Intente nuevamente.")
      
    print(f"El monto queda registrado como: ${monto}")
    mult.append(monto)
    print("~ FECHA DE LA MULTA ~")
    print("Sólo los dígitos, sin '-' o '/'")
    while True:
      try:
        fecha_multa = input("Fecha: ")
        if fecha_multa != "" and fecha_multa.isdigit() and len(fecha_multa) == 6:
           break
        else:
           print("Ingrese una fecha válida. Ej: 160822")
      except:
         print("Error. Intente nuevamente.")

    print(f"La fecha queda registrada como: {fecha_multa}")
    mult.append(fecha_multa)
    multas.append(mult)
    num_multas -= 1
  
  print("Los datos del vehículo se guardaron.")

def buscar(display):
  patente_existe = False
  print("¿Qué auto está buscando?")
  print("Ingrese la patente del vehículo que desea buscar.")
  while True:
      try:
         buscar_patente = input("PATENTE: ")
         if buscar_patente != "" and len(buscar_patente) == 6:
            break
         else:
            print("Ingrese una patente válida.")
      except:
         print("Error. Intente nuevamente.")
  for p in range(len(patentes)):
        if buscar_patente.upper() == patentes[p]:
           print("Auto encontrado.")
           patente_existe = True   
           if display == True:
            print("   ~ INFORMACIÓN DEL VEHÍCULO ~")
            print("")
            print(f"Patente: {patentes[p]}")
            print(f"Tipo: {tipos[p]}")
            print(f"Marca: {marcas[p]}")
            print(f"Precio: ${precios[p]}")
            print(f"Fecha de registro: {fechas_registro[p]}")
            print(f"Marca: {marcas[p]}")
            print(f"Dueño: {nombres[p]} {apellidos[p]}")
            print(f"Multa(s): {multas[p]}")
           return p
  if patente_existe == False:
        print("Lo sentimos, pero el vehículo que busca no se encuentra en nuestro sistema.")        
  
def imprimir_certificados():
   ind = buscar(False)
   print("-"*40)
   print("CERTIFICADO DE EMISIONES CONTAMINANTES")
   print("-"*40)
   print(f"FECHA REVISIÓN: {fechas_registro[ind]}")
   print(f"PROPIETARIO   : {nombres[ind]} {apellidos[ind]}")
   print("-"*40)
   print(f"PLACA PATENTE : {patentes[ind]}")
   print(f"TIPO          : {tipos[ind]}")
   print(f"MARCA         : {marcas[ind]}")
   print("-"*40)
   print("ANOTACIONES VIGENTES")
   print("-"*40)
   print(multas[ind])
   print("")
   
def salir():
   print("¿Desea salir del menú? Elija un número")
   print("[1] Sí")
   print("[2] No")
   print("Escoja una opción")
   opc3 = int(input("Opción N°: "))
   return opc3

opcion1 = 0
while opcion1 != 4:
  opcion1 = menu()
  os.system("cls")
  match opcion1:
    case 1:
      grabar()
      opcion2 = mostrar_multas()
      os.system("cls")
      if opcion2 == 1:
         multa()
      else:
        print("Los datos del vehículo se guardaron.")
      os.system("cls")
      continue
    case 2:
      os.system("cls")
      buscar(True)
      continue
    case 3:
        os.system("cls")
        imprimir_certificados()
        continue
    case 4:
        opcion3 = salir()
        if opcion3 == 1:
          print("Macarena Paz Avendaño Ccopa")
          print("AutoSeguroFormaA V.1.0")     
          break
        else:
          opcion1 = 0
          continue
