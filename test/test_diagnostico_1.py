import unittest
from src.diagnostico import Diagnostico, Sintoma, EstadoDiagnostico

class TestDiagnostico(unittest.TestCase):

    def setUp(self):
        print("\nIniciando una nueva prueba")
        self.motor_diagnostico = Diagnostico()

    def tearDown(self):
        print(f"Diagnóstico obtenido: {self.diagnostico}")
        print("Finalizando la prueba\n")

    def run_diagnostico(self, sintomas):
        self.motor_diagnostico.reset()
        self.motor_diagnostico.declare(Sintoma(**sintomas))
        self.motor_diagnostico.run()
        self.diagnostico = self.motor_diagnostico.obtener_diagnostico()

    def test_faringitis(self):
        print("Prueba para verificar el diagnóstico de faringitis")
        self.run_diagnostico({'fiebre': 's', 'dolor_de_garganta': 's'})
        self.assertEqual(self.diagnostico, "Posible faringitis")

    def test_gripe(self):
        print("Prueba para verificar el diagnóstico de gripe")
        self.run_diagnostico({'fiebre': 's', 'dolor_de_garganta': 'n', 'dolor_de_cabeza': 's'})
        self.assertEqual(self.diagnostico, "Posible gripe")

    def test_resfriado_comun(self):
        print("Prueba para verificar el diagnóstico de resfriado común")
        self.run_diagnostico({'fiebre': 'n', 'dolor_de_cabeza': 's', 'congestion_nasal': 's'})
        self.assertEqual(self.diagnostico, "Posible resfriado común")

    def test_bronquitis(self):
        print("Prueba para verificar el diagnóstico de bronquitis")
        self.run_diagnostico({'fiebre': 'n', 'dolor_de_cabeza': 's', 'congestion_nasal': 'n', 'tos': 's'})
        self.assertEqual(self.diagnostico, "Posible bronquitis")

    def test_sinusitis(self):
        print("Prueba para verificar el diagnóstico de sinusitis")
        self.run_diagnostico({'fiebre': 'n', 'dolor_de_cabeza': 'n', 'congestion_nasal': 's', 'tos': 's'})
        self.assertEqual(self.diagnostico, "Posible sinusitis")

    def test_alergia(self):
        print("Prueba para verificar el diagnóstico de alergia")
        self.run_diagnostico({'fiebre': 'n', 'dolor_de_cabeza': 'n', 'congestion_nasal': 's', 'tos': 'n'})
        self.assertEqual(self.diagnostico, "Posible alergia")

    def test_sintomas_no_reconocidos(self):
        print("Prueba para verificar el diagnóstico de síntomas no reconocidos")
        self.run_diagnostico({'fiebre': 'n', 'dolor_de_garganta': 'n', 'dolor_de_cabeza': 'n', 'congestion_nasal': 'n', 'tos': 'n'})
        self.assertEqual(self.diagnostico, "Síntomas no reconocidos")

if __name__ == "__main__":
    unittest.main()
