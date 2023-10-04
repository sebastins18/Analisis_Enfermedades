"""
Este módulo define la interfaz de usuario para obtener información del usuario y sus síntomas.
"""

from src.utils.helpers import cargar_variable_entorno

class InterfazUsuario:
    """
    Esta clase proporciona métodos para interactuar con el usuario y 
    obtener su información y síntomas.
    """
    def obtener_informacion_usuario(self):
        """
        Solicita al usuario que proporcione su nombre y lugar de origen.
        """
        nombre = input("Por favor, ingresa tu nombre: ")
        lugar = input("Ingresa tu lugar de origen: ")
        return {"nombre": nombre, "lugar": lugar}

    def obtener_sintomas_usuario(self):
        """
        Solicita al usuario que proporcione información sobre sus síntomas.
        """
        ruta_sintomas = cargar_variable_entorno('SINTOMAS_FILE_PATH')
        sintomas_usuario = {}
        try:
            with open(ruta_sintomas, 'r', encoding='utf-8') as file:
                sintomas = [line.strip() for line in file.readlines()]
                for sintoma in sintomas:
                    respuesta = input(f"Tiene {sintoma} (s/n): ").lower()
                    sintomas_usuario[sintoma] = respuesta
        except FileNotFoundError:
            print(f"Error: El archivo en '{ruta_sintomas}' no se encontró.")
        return sintomas_usuario
