### Mental durumlar üzerinden sınıflandırma ve bu sınıflandırma üzerinden kişinin mental durum çıkarım yapan model.


# Gerekli olan kütüpaneleri import etme.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# Veriyi yükleyin
file_path = r'../data/depresyon.csv'
data = pd.read_csv(file_path)

# Veriyi ön işleme
# Kategorik değişkenleri sayısal değerlere dönüştürmek için Label Encoding kullanın
# print(data.dtypes) # Bütün veri seti  object türünde
 
label_encoders = {}
for column in data.columns:
    if data[column].dtype == 'object':
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le
        """
        Bir sütunda olan verileri unique hale getirir her birine 0,1,2,3 ..  gibi birbirinden farklı dijitleri dönüştürür. 
        Bütün sütunu karşılıklarını çevirir ve veri setim sayısal değerlere dönüşmüş olur.

        """
## print(data)

# Verinin genel bir özetini görüntüleyin
# print(data.describe()) # Her sütuna özgü istatistiksel değerleri verir.
# print(data.info()) # Türünü null değer sayısını verir.
# print(data.isnull().sum()) # Önemlidir boş veri olup olmadığını bilmemiz gerekir.


# Veriyi görselleştirin
# plt.figure(figsize=(12, 6))
# sns.countplot(x='Mood_Swings', data=data)
# plt.title('Mood Swings Distribution')
# plt.show()

# plt.figure(figsize=(12, 6))
# sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
# plt.title('Feature Correlation Matrix')
# plt.show()

# Özellikleri ve hedef değişkeni tanımlayın -- Öz nitelik ve hedef öğrenim değişkeni
X = data.drop(columns=['Mood_Swings'])
y = data['Mood_Swings']

# Veriyi eğitim ve test setlerine ayırın
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Karar ağacı sınıflandırıcısını eğitin
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Test seti üzerinde tahmin yapın
y_pred = model.predict(X_test)

# Modeli değerlendirin
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(report)

# Karar ağacını görselleştirin
plt.figure(figsize=(20, 10))
plot_tree(model, feature_names=X.columns.tolist(), class_names=label_encoders['Mood_Swings'].classes_.tolist(), filled=True)
plt.title('Decision Tree Visualization')
plt.savefig("../figures/kararağacı.png", dpi=320)
plt.show()
