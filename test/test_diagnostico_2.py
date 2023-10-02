import pytest
from src.diagnostico import Diagnostico, Sintoma

@pytest.fixture
def motor_diagnostico():
    motor = Diagnostico()
    motor.reset()
    return motor

def test_posible_faringitis(motor_diagnostico):
    sintomas = {
        'fiebre': 's',
        'dolor_de_garganta': 's',
        'dolor_de_cabeza': 'n',
        'congestion_nasal': 'n',
        'tos': 'n'
    }
    motor_diagnostico.declare(Sintoma(**sintomas))
    motor_diagnostico.run()
    assert "Posible faringitis" in motor_diagnostico.obtener_diagnostico()

def test_posible_gripe(motor_diagnostico):
    sintomas = {
        'fiebre': 's',
        'dolor_de_garganta': 'n',
        'dolor_de_cabeza': 's',
        'congestion_nasal': 'n',
        'tos': 'n'
    }
    motor_diagnostico.declare(Sintoma(**sintomas))
    motor_diagnostico.run()
    assert "Posible gripe" in motor_diagnostico.obtener_diagnostico()

def test_posible_resfriado_comun(motor_diagnostico):
    sintomas = {
        'fiebre': 'n',
        'dolor_de_garganta': 'n',
        'dolor_de_cabeza': 's',
        'congestion_nasal': 's',
        'tos': 'n'
    }
    motor_diagnostico.declare(Sintoma(**sintomas))
    motor_diagnostico.run()
    assert "Posible resfriado común" in motor_diagnostico.obtener_diagnostico()

def test_posible_bronquitis(motor_diagnostico):
    sintomas = {
        'fiebre': 'n',
        'dolor_de_garganta': 'n',
        'dolor_de_cabeza': 's',
        'congestion_nasal': 'n',
        'tos': 's'
    }
    motor_diagnostico.declare(Sintoma(**sintomas))
    motor_diagnostico.run()
    assert "Posible bronquitis" in motor_diagnostico.obtener_diagnostico()

def test_posible_sinusitis(motor_diagnostico):
    sintomas = {
        'fiebre': 'n',
        'dolor_de_garganta': 'n',
        'dolor_de_cabeza': 'n',
        'congestion_nasal': 's',
        'tos': 's'
    }
    motor_diagnostico.declare(Sintoma(**sintomas))
    motor_diagnostico.run()
    assert "Posible sinusitis" in motor_diagnostico.obtener_diagnostico()

def test_posible_alergia(motor_diagnostico):
    sintomas = {
        'fiebre': 'n',
        'dolor_de_garganta': 'n',
        'dolor_de_cabeza': 'n',
        'congestion_nasal': 's',
        'tos': 'n'
    }
    motor_diagnostico.declare(Sintoma(**sintomas))
    motor_diagnostico.run()
    assert "Posible alergia" in motor_diagnostico.obtener_diagnostico()

def test_sintomas_no_reconocidos(motor_diagnostico):
    sintomas = {
        'fiebre': 'n',
        'dolor_de_garganta': 'n',
        'dolor_de_cabeza': 'n',
        'congestion_nasal': 'n',
        'tos': 'n'
    }
    motor_diagnostico.declare(Sintoma(**sintomas))
    motor_diagnostico.run()
    assert  motor_diagnostico.obtener_diagnostico() 

def test_diagnostico_no_encontrado(motor_diagnostico):
    motor_diagnostico.run()
    assert "Síntomas no reconocidos" in motor_diagnostico.obtener_diagnostico()

