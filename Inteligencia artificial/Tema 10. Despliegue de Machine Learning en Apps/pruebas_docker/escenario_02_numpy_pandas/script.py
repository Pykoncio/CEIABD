import numpy as np
import pandas as pd

# Crear un array numpy
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Convertir el array numpy a un dataframe
df = pd.DataFrame(array, columns=['Columna1', 'Columna2', 'Columna3'])

print(array)
print(df)