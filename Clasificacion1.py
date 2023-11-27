import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# Leer los datos
nombre_archivo = "datos_procesados_nuevo.csv"
df = pd.read_csv(nombre_archivo)

# Eliminar la columna 'categoria_edad'
df = df.drop(columns=['categoria_edad'])

# Graficar la distribución de clases
plt.figure(figsize=(6, 4))
sns.countplot(x='DEATH_EVENT', data=df, palette='muted')
plt.title('Distribución de Clases')
plt.xlabel('DEATH_EVENT')
plt.ylabel('Número de Instancias')
plt.show()

# Separar las características (X) y la variable objetivo (y)
X = df.drop(columns=['DEATH_EVENT'])
y = df['DEATH_EVENT']

# Partición del dataset de manera estratificada
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Ajustar un árbol de decisión y calcular la accuracy sobre el conjunto de test
model = DecisionTreeClassifier(random_state=42)

# Experimenta con los parámetros del árbol de decisión para mejorar la precisión
# Por ejemplo, puedes ajustar max_depth, min_samples_split, min_samples_leaf, etc.
# model = DecisionTreeClassifier(random_state=42, max_depth=..., min_samples_split=..., min_samples_leaf=...)

model.fit(X_train, y_train)

# Predecir sobre el conjunto de test
y_pred = model.predict(X_test)

# Calcular la accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

