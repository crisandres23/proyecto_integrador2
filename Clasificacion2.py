import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score

# Leer los datos
nombre_archivo = "datos_procesados_nuevo.csv"
df = pd.read_csv(nombre_archivo)

# Eliminar la columna 'categoria_edad'
df = df.drop(columns=['categoria_edad'])

# Separar las características (X) y la variable objetivo (y)
X = df.drop(columns=['DEATH_EVENT'])
y = df['DEATH_EVENT']

# Partición del dataset de manera estratificada
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Ajustar un Random Forest
model_rf = RandomForestClassifier(random_state=42)
model_rf.fit(X_train, y_train)

# Predecir sobre el conjunto de prueba
y_pred_rf = model_rf.predict(X_test)

# Calcular la matriz de confusión
conf_matrix_rf = confusion_matrix(y_test, y_pred_rf)
print('Matriz de Confusión (Random Forest):')
print(conf_matrix_rf)

# Calcular F1-Score y comparar con la accuracy
f1_rf = f1_score(y_test, y_pred_rf)
accuracy_rf = accuracy_score(y_test, y_pred_rf)

print(f'F1-Score (Random Forest): {f1_rf}')
print(f'Accuracy (Random Forest): {accuracy_rf}')

