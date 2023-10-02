from os import getenv
from src.utils.helpers import cargar_variable_entorno

class InterfazUsuario:
    def obtener_informacion_usuario(self):
        nombre = input("Por favor, ingresa tu nombre: ")
        lugar = input("Ingresa tu lugar de origen: ")
        return {"nombre": nombre, "lugar": lugar}

    def obtener_sintomas_usuario(self):
        ruta_sintomas = cargar_variable_entorno('SINTOMAS_FILE_PATH')
        sintomas_usuario = {}
        try:
            with open(ruta_sintomas, 'r') as f:
                sintomas = [line.strip() for line in f.readlines()]
                for sintoma in sintomas:
                    respuesta = input(f"Tiene {sintoma} (s/n): ").lower()
                    sintomas_usuario[sintoma] = respuesta
        except FileNotFoundError:
            print(f"Error: El archivo en '{ruta_sintomas}' no se encontró.")
        return sintomas_usuario
