from src.interfaz_usuario import InterfazUsuario
from src.diagnostico import Diagnostico, Sintoma
from src.utils.helpers import cargar_variables_entorno
from experta import Fact

def main():
    try:
        cargar_variables_entorno()
        interfaz = InterfazUsuario()
        usuario = interfaz.obtener_informacion_usuario()
        sintomas = interfaz.obtener_sintomas_usuario()

        motor_diagnostico = Diagnostico()
        motor_diagnostico.reset()
        declarar_sintomas(motor_diagnostico, sintomas)

        motor_diagnostico.run()

        diagnostico = motor_diagnostico.obtener_diagnostico()
        imprimir_resultados(usuario, diagnostico)

    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

def declarar_sintomas(motor_diagnostico, sintomas):
    motor_diagnostico.declare(Sintoma(**sintomas))



def imprimir_resultados(usuario, diagnosticos):
    print(f"{usuario['nombre']}, basado en tus síntomas:")
    if diagnosticos:
        if isinstance(diagnosticos, list):
            for diagnostico in diagnosticos:
                print("- " + diagnostico)
        else:
            print("- " + diagnosticos)
    else:
        print("No se pudo determinar un diagnóstico basado en los síntomas proporcionados.")
    print(
    "Recuerda, los diagnósticos proporcionados son solamente posibilidades y no deben ser "
    "considerados como diagnósticos médicos definitivos. Por favor, consulta a un profesional "
    "de la salud para obtener un diagnóstico adecuado."
    )


if __name__ == "__main__":
    main()
