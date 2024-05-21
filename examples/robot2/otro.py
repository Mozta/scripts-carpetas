import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
project_dir = os.path.dirname(parent_dir)

print(f"Directorio del proyecto: {project_dir}  \n")
print(f"Directorio actual: {current_dir}  \n")
print(f"Directorio padre: {parent_dir}  \n")

sys.path.append(project_dir)
