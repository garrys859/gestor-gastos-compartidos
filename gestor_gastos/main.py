# Menú principal e integración (Dev 1)
# Rama: feature/main
#
# Ejecutar desde la carpeta gestor_gastos:  python main.py

from storage import cargar_datos, guardar_datos
from usuarios import agregar_participante, listar_participantes
from gastos import registrar_gasto, listar_gastos
from balances import calcular_balances, calcular_liquidaciones


def mostrar_menu():
    """Muestra las opciones del menú."""
    pass


def opcion_participante(datos):
    """Pide un nombre y lo añade al grupo."""
    pass


def opcion_gasto(datos):
    """Pide pagador, concepto e importe y registra el gasto."""
    pass


def opcion_historial(datos):
    """Muestra todos los gastos registrados."""
    pass


def opcion_balances(datos):
    """Muestra el saldo de cada uno y quién paga a quién."""
    pass


def main():
    """Carga los datos, muestra el menú en bucle y guarda al salir."""
    pass


if __name__ == "__main__":
    main()
