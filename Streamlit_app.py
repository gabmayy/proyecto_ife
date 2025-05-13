import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Top 10 Programas Académicos", layout="centered")

# Cargar datos
df = pd.read_csv("datos_ife.csv")  # Ajusta el nombre del archivo

# Conteo global de valores válidos y NaNs
total_values = df.size
nan_count = df.isna().sum().sum()
valid_count = total_values - nan_count

# Mostrar estadísticas en Streamli
st.title("Exploración de datos")
st.header("Datos default")
st.write(f"**Total de datos:** {total_values}")
st.write(f"**Datos válidos:** {valid_count}")
st.write(f"**Datos NaN:** {nan_count}")
st.write(f"**Porcentaje de datos válidos:** {valid_count / total_values * 100:.2f}%")
st.write(f"**Porcentaje de datos NaN:** {nan_count / total_values * 100:.2f}%\n")

# Parámetros de layout
cols = 4  # columnas por fila en el grid
rows = math.ceil(len(df.columns) / cols)
fig, axes = plt.subplots(rows, cols, figsize=(cols * 4, rows * 4))

axes = axes.flatten()

for i, col in enumerate(df.columns):
    total = len(df)
    nan_count_col = df[col].isna().sum()
    valid_count_col = total - nan_count_col

    # 🎨 Pie chart
    sizes = [valid_count_col, nan_count_col]
    labels = ["Válidos", "NaN"]
    colors = ["#66bb6a", "#ef5350"]
    
    axes[i].pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    axes[i].axis('equal')
    axes[i].set_title(col, fontsize=8)

# Ocultar los subplots vacíos si hay
for j in range(i + 1, len(axes)):
    axes[j].axis("off")

plt.tight_layout()
plt.suptitle("Distribución de NaNs por columna", fontsize=16, y=1.02)

# Mostrar el gráfico en Streamlit
st.pyplot(fig)


# Cargar datos
df = pd.read_csv("datos_limpios.csv")  # Ajusta el nombre del archivo

# Conteo global de valores válidos y NaNs
total_values = df.size
nan_count = df.isna().sum().sum()
valid_count = total_values - nan_count


# Mostrar estadísticas en Streamlit
st.header("Datos con limpieza")
st.write(f"**Total de datos:** {total_values}")
st.write(f"**Datos válidos:** {valid_count}")
st.write(f"**Datos NaN:** {nan_count}")
st.write(f"**Porcentaje de datos válidos:** {valid_count / total_values * 100:.2f}%")
st.write(f"**Porcentaje de datos NaN:** {nan_count / total_values * 100:.2f}%\n")

# Parámetros de layout
cols = 4  # columnas por fila en el grid
rows = math.ceil(len(df.columns) / cols)
fig, axes = plt.subplots(rows, cols, figsize=(cols * 4, rows * 4))

axes = axes.flatten()

for i, col in enumerate(df.columns):
    total = len(df)
    nan_count_col = df[col].isna().sum()
    valid_count_col = total - nan_count_col

    # 🎨 Pie chart
    sizes = [valid_count_col, nan_count_col]
    labels = ["Válidos", "NaN"]
    colors = ["#66bb6a", "#ef5350"]
    
    axes[i].pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    axes[i].axis('equal')
    axes[i].set_title(col, fontsize=8)

# Ocultar los subplots vacíos si hay
for j in range(i + 1, len(axes)):
    axes[j].axis("off")

plt.tight_layout()
plt.suptitle("Distribución de NaNs por columna", fontsize=16, y=1.02)

# Mostrar el gráfico en Streamlit
st.pyplot(fig)

# Gráfica: Top 10 programas académicos por número de estudiantes
st.header("Top 10 programas ácadémicos")

top_programas = df["program.major_id"].value_counts().head(10)

fig, ax = plt.subplots()
top_programas.plot(kind="bar", ax=ax)
ax.set_title("Top 10 programas académicos por número de estudiantes")
ax.set_ylabel("Cantidad de estudiantes")
ax.set_xlabel("ID del programa")
st.pyplot(fig)

#Correlación entre variables en heatmap
st.header("Top 10 programas ácadémicos")
#num_df = df.select_dtypes(include="number")

# Calcular matriz de correlación
#corr = num_df.corr(numeric_only=True)

# Mostrar matriz como heatmap
#plt.figure(figsize=(14, 10))
#sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", square=True)
#plt.title("Mapa de correlación entre variables numéricas")
#st.pyplot(plt)
