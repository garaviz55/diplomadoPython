monto = float(input("Ingrese el monto a prestar: "))
tiempo = int(input("Digite el tiempo del crédito: "))
opcionProducto = int(input("""Seleccionar el producto financiero a validar:
1. Crédito Hipotecario
2. Tarjeta Crédito
3. Crédito Libre Inversión
4. Compra de Cartera

"""))

def tipo_interes(producto):

  if producto == 1:
      interes = 0.4

  elif producto == 2:
      interes = 2.16

  elif producto == 3:
      interes = 1.5
      
  elif producto == 4:
      interes = 0.8

  else:
      print("Opción Invalida...")
      interes=0
  return interes


def monto_apagar(valor,duracion=12,tipoProducto=3):
  inter = tipo_interes(tipoProducto)
  val_inicial=valor

  if inter == 0:
    print('No se puede realizar el cálculo')
    
  else:
      for i in range(duracion):
        ValorPorIntereses = valor * (inter/100)
        valor = valor + ValorPorIntereses
      print("El interes compuesto es: {0:.2f}".format(valor-val_inicial), "y el valor total a pagar es: {0:.2f}".format(valor))


monto_apagar(monto,tiempo,opcionProducto)