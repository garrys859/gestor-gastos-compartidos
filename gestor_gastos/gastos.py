# Módulo de gastos (Dev 3)
# Rama: feature/gastos
#
# Cada gasto es un diccionario:
# {"pagador": "Ana", "concepto": "Cena", "importe": 60.0}


def registrar_gasto(datos, pagador, concepto, importe):
    """Añade un gasto a la lista.
    Devuelve False si el pagador no existe o el importe no es mayor que 0."""
    pass


def listar_gastos(datos):
    """Devuelve la lista de gastos registrados."""
    pass


def borrar_gasto(datos, posicion):
    """Borra el gasto que está en esa posición de la lista.
    Devuelve True si se ha borrado, False si la posición no existe."""
    pass


def total_gastado(datos):
    """Devuelve la suma de todos los importes."""
    pass
