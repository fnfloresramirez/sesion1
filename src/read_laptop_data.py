# Importing the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# List of common encodings to try
encodings = ['latin1', 'cp1252', 'iso-8859-1', 'utf-16']

for encoding in encodings:
    try:
        print(f"\nTrying encoding: {encoding}")
        # Read the CSV file with current encoding
        df = pd.read_csv('laptop_price.csv', encoding=encoding)
        
        # If we get here, the encoding worked
        print("Successfully read the file!")
        
        # Display basic information about the dataset
        print("\nDataset Information:")
        print("=" * 50)
        print(f"Number of rows: {len(df)}")
        print(f"Number of columns: {len(df.columns)}")
        print("\nColumn names:")
        print(df.columns.tolist())
        print("\nFirst 5 rows of the dataset:")
        print(df.head())
        print("\nBasic statistics:")
        print(df.describe())
        print(df.info())

        print(df.columns)
        
        break
        
    except UnicodeDecodeError:
        print(f"Failed with {encoding} encoding, trying next...")
        continue
    except Exception as e:
        print(f"An error occurred with {encoding} encoding: {str(e)}")
        continue
else:
    print("\nAll encoding attempts failed. Please check the file encoding.") 

# EDA - Histograma de los precios
sns.histplot(df['Price_euros'])
plt.title("Distribucion de los precios de las laptops")
plt.show()

# Gráfica de precios por compañía
plt.figure(figsize=(12, 6))
sns.boxplot(x='Company', y='Price_euros', data=df)
plt.title('Distribución de Precios por Compañía')
plt.xlabel('Compañía')
plt.ylabel('Precio (Euros)')
plt.xticks(rotation=45, ha='right')  # Rotar etiquetas para mejor legibilidad
plt.tight_layout()  # Ajustar el layout para evitar que se corten las etiquetas
plt.show()

# Insight: Esta gráfica nos permite ver que Apple tiene los precios más altos en promedio,
# mientras que otras compañías como HP y Dell tienen una gama más amplia de precios,
# ofreciendo opciones tanto económicas como de gama alta.

# Gráfica de precios por tipo de laptop
plt.figure(figsize=(12, 6))
sns.boxplot(x='TypeName', y='Price_euros', data=df)
plt.title('Distribución de Precios por Tipo de Laptop')
plt.xlabel('Tipo de Laptop')
plt.ylabel('Precio (Euros)')
plt.xticks(rotation=45, ha='right')  # Rotar etiquetas para mejor legibilidad
plt.tight_layout()  # Ajustar el layout para evitar que se corten las etiquetas
plt.show()

# Insight: Esta gráfica revela que los Ultrabooks tienden a tener los precios más altos,
# mientras que los Notebooks y Netbooks tienen precios más accesibles. Los Gaming laptops
# muestran una amplia gama de precios, desde opciones económicas hasta modelos de alta gama.

# Gráfica de precios por tamaño de pantalla
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Inches', y='Price_euros', data=df, alpha=0.6)
plt.title('Relación entre Tamaño de Pantalla y Precio')
plt.xlabel('Tamaño de Pantalla (Pulgadas)')
plt.ylabel('Precio (Euros)')

# Agregar línea de tendencia
sns.regplot(x='Inches', y='Price_euros', data=df, scatter=False, color='red')

# Agregar grid para mejor lectura
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Insight: La gráfica muestra que no hay una correlación fuerte entre el tamaño de la pantalla y el precio.
# Los precios más altos se encuentran en laptops de tamaño medio (13-15 pulgadas), lo que sugiere
# que otros factores como la marca, tipo de laptop y especificaciones técnicas tienen mayor impacto
# en el precio que el tamaño de la pantalla.

# Tarea 1:
# Crear cada 1 de las 3 graficas y agregar 1 insight por cada una.
# Relacion de los precios (Price_euros) por compañia (Company) -->
# Relacion de los precios (Price_euros) por tipo de laptop (TypeName) -->
# Relacion de los precios (Price_euros) por tamaño de pantalla (Inches) -->

