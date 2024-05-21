import sys
import os

# Obtener el directorio principal del proyecto
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
print(f"Directorio del proyecto: {project_dir}  \n")

sys.path.append(project_dir)

# Importar las librerías
from libraries import datos as d

datos = d.generar_datos()
print(datos)