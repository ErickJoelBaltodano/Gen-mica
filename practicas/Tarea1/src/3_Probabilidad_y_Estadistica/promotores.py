import pandas as pd
import matplotlib.pyplot as plt

# Definimos los promotores a buscar
promotores = ["AGATAG", "TGATAG", "AGATAA", "TGATAA"]

# Leer el archivo (una secuencia por línea)
with open("promotores.txt", "r") as f:
    secuencias = [line.strip() for line in f if line.strip()]

# Contar ocurrencias de cada promotor en cada secuencia
conteos = {p: [] for p in promotores}

for seq in secuencias:
    for p in promotores:
        conteos[p].append(seq.count(p))

# Convertir a DataFrame
df = pd.DataFrame(conteos)

# Boxplot
plt.figure(figsize=(8, 6))
df.boxplot()
plt.title("Distribución de ocurrencias de promotores")
plt.ylabel("Número de ocurrencias")
plt.show()

# Calcular media y desviación estándar
stats = df.describe().loc[["mean", "std"]]
stats.rename(index={"mean": "media", "std": "desvE"}, inplace=True)
print("Medias y desviaciones estándar:")
print(stats)