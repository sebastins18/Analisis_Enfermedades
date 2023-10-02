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
    assert motor_diagnostico.obtener_diagnostico() == "Posible faringitis"

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
    assert motor_diagnostico.obtener_diagnostico() == "Posible gripe"

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
    assert motor_diagnostico.obtener_diagnostico() == "Posible resfriado común"

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
    assert motor_diagnostico.obtener_diagnostico() == "Posible bronquitis"

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
    assert motor_diagnostico.obtener_diagnostico() == "Posible sinusitis"

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
    assert motor_diagnostico.obtener_diagnostico() == "Posible alergia"

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
    assert motor_diagnostico.obtener_diagnostico() == "Síntomas no reconocidos"

def test_diagnostico_no_encontrado(motor_diagnostico):
    motor_diagnostico.run()
    assert motor_diagnostico.obtener_diagnostico() == "Síntomas no reconocidos"

