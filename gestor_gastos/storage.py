# Módulo de persistencia (Dev 5)
# Rama: feature/storage

ARCHIVO_DATOS = "datos.json"
ARCHIVO_RESUMEN = "resumen.txt"


def datos_vacios():
    """Devuelve la estructura inicial cuando aún no hay datos."""
    return {"participantes": [], "gastos": []}


def cargar_datos():
    """Lee datos.json. Si no existe, devuelve datos_vacios()."""
    pass


def guardar_datos(datos):
    """Guarda los datos en datos.json."""
    pass


def exportar_resumen(balances, liquidaciones):
    """Escribe en resumen.txt los saldos y los pagos pendientes. (Sprint 2, HU7)"""
    pass
