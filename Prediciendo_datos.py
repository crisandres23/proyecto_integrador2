import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Leer los datos
nombre_archivo = "datos_procesados_nuevo.csv"
df = pd.read_csv(nombre_archivo)
# Eliminar las columnas DEATH_EVENT, age y categoria_edad
X = df.drop(columns=['DEATH_EVENT', 'age', 'categoria_edad'])

# Separar los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, df['age'], test_size=0.2, random_state=42)

# Inicializar y ajustar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Predecir las edades en el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular el error cuadrático medio
mse = mean_squared_error(y_test, y_pred)
print(f'Error Cuadrático Medio: {mse}')
