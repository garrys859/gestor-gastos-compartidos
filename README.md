# Gestor de Gastos Compartidos

Aplicación de consola en Python para repartir gastos de un grupo (estilo Splitwise): se registran participantes y gastos, y el programa calcula quién debe dinero a quién.

Proyecto de prácticas de **Gestión de Proyectos (UBU)**, desarrollado con Scrum.

Solo usa la librería estándar de Python (`json`, `os`, `unittest`): no hay que instalar nada.

## Cómo ejecutarlo

```bash
cd gestor_gastos
python main.py
```

Tests:

```bash
cd gestor_gastos
python -m unittest test_proyecto.py
```

## Estructura y reparto

| Fichero | Responsable | Rama | Contenido |
|---|---|---|---|
| `main.py` | Dev 1 | `feature/main` | Menú principal e integración de módulos |
| `usuarios.py` | Dev 2 | `feature/usuarios` | Alta, listado y validación de participantes |
| `gastos.py` | Dev 3 | `feature/gastos` | Registro, listado y borrado de gastos |
| `balances.py` | Dev 4 | `feature/balances` | Saldos y pagos para liquidar deudas |
| `storage.py` | Dev 5 | `feature/storage` | Guardar/cargar `datos.json` y exportar resumen |
| `test_proyecto.py` | Dev 6 | `feature/tests` | Pruebas con `unittest` |

Formato de los datos (`datos.json`):

```json
{
    "participantes": ["Ana", "Luis", "Marta"],
    "gastos": [
        {"pagador": "Ana", "concepto": "Cena", "importe": 60.0}
    ]
}
```

## Product Backlog

**Sprint 1 (MVP)**

- HU1: Como usuario, quiero registrar participantes en el grupo.
- HU2: Como usuario, quiero añadir un gasto indicando quién pagó, el importe y el concepto.
- HU3: Como usuario, quiero ver el historial de gastos.
- HU4: Como usuario, quiero calcular el balance (quién debe dinero a quién).
- HU5: Como usuario, quiero que los datos se guarden en un fichero JSON al salir.

**Sprint 2**

- HU6: Dividir gastos de forma desigual (por porcentajes o importes exactos).
- HU7: Exportar el resumen de deudas a un fichero de texto.

## Forma de trabajo con Git

1. Cada historia de usuario tiene su Issue en GitHub.
2. Cada desarrollador trabaja en su rama `feature/...`, creada desde `main`.
3. Commits pequeños y con mensaje claro (`Añade validación de nombre vacío`).
4. Al terminar, se abre un Pull Request hacia `main` enlazando la Issue (`Closes #n`).
5. Otro compañero revisa el PR antes de hacer merge.

**Definition of Done:** el código está en `main` tras un PR aprobado y los tests pasan.
