# Pruebas automáticas (Dev 6)
# Rama: feature/tests
#
# Ejecutar desde la carpeta gestor_gastos:  python -m unittest test_proyecto.py

import unittest


class TestUsuarios(unittest.TestCase):

    def test_agregar_participante(self):
        self.skipTest("Pendiente de implementar")

    def test_no_permite_nombre_vacio_ni_repetido(self):
        self.skipTest("Pendiente de implementar")


class TestGastos(unittest.TestCase):

    def test_registrar_gasto(self):
        self.skipTest("Pendiente de implementar")

    def test_no_permite_importe_negativo_ni_pagador_inexistente(self):
        self.skipTest("Pendiente de implementar")


class TestBalances(unittest.TestCase):

    def test_calcular_balances(self):
        self.skipTest("Pendiente de implementar")

    def test_calcular_liquidaciones(self):
        self.skipTest("Pendiente de implementar")


class TestStorage(unittest.TestCase):

    def test_guardar_y_cargar(self):
        self.skipTest("Pendiente de implementar")


if __name__ == "__main__":
    unittest.main()
