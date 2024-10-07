import requests
import json
from colorama import Fore, Back, Style, init
# Inicializamos Colorama
init(autoreset=True)

# Mensajes de ejemplo
print(Fore.GREEN + Style.BRIGHT + """    
                                __  __
                                \ \/ /
                                 \  / 
                                 /  \ 
                                /_/\_\ 
                          By: Hack Underway
""")



def obtener_datos_usuario(nombre_usuario):
    url = f"https://api.memory.lol/v1/tw/{nombre_usuario}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None

def mostrar_datos_organizados(datos):
    if not datos:
        return

    for cuenta in datos.get("accounts", []):
        print(f"ID de la cuenta: {cuenta.get('id_str')}")
        print("Nombres de usuario:")
        for nombre, fechas in cuenta.get("screen_names", {}).items():
            fechas_str = ", ".join(fechas)
            print(f"  - {nombre}: {fechas_str}")

def main():

    nombre_usuario = input("Por favor, introduce un nombre de usuario de 𝕏: ")
    datos = obtener_datos_usuario(nombre_usuario)
    print("\nDatos obtenidos:")
    mostrar_datos_organizados(datos)

if __name__ == "__main__":
    main()
