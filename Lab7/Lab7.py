import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = np.loadtxt("Bank_Customer.csv", skiprows=1, dtype=str, delimiter=",")

# Remove customer_id, encode country as one-hot features, and encode gender
# as a binary feature. Keep churn separate as the prediction target.
country_categories = np.unique(data[:, 2])
country_features = np.column_stack(
    [data[:, 2] == country for country in country_categories]
).astype(float)

gender_values = {"Female": 0.0, "Male": 1.0}
unknown_genders = set(data[:, 3]) - gender_values.keys()
if unknown_genders:
    raise ValueError(f"Unknown gender categories: {sorted(unknown_genders)}")
gender_feature = np.array([gender_values[gender] for gender in data[:, 3]])

feature_names = (
    ["credit_score"]
    + [f"country_{country}" for country in country_categories]
    + [
        "gender",
        "age",
        "tenure",
        "balance",
        "products_number",
        "credit_card",
        "active_member",
        "estimated_salary",
    ]
)
x = np.column_stack(
    (
        data[:, 1].astype(float),
        country_features,
        gender_feature,
        data[:, 4:11].astype(float),
    )
)
y = data[:, 11].astype(int)

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Save the complete dataset using the scaler fitted on training data only.
preprocessed_data = np.column_stack((scaler.transform(x), y))
np.savetxt(
    "Bank_Customer_Preprocessed.csv",
    preprocessed_data,
    delimiter=",",
    header=",".join(feature_names + ["churn"]),
    comments="",
    fmt="%.8g",
)

# 決策分類器
clf = LogisticRegression()

# 使用訓練集來訓練我們的分類器
clf.fit(x_train, y_train)
# 測試資料集中進行預測
pred = clf.predict(x_test)

#print (pred) # 預測分類，即客戶是否流失
#print (y_test) # 分類
print (str(accuracy_score(pred, y_test)*100 ) + "% ")   # 預測精度 