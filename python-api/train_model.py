import pandas as pd 
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("./student_data.csv")

X = df[["Attendance", "Test_Marks", "Assignment_Marks", "Practical_Marks"]]
Y = df["Final_Marks"]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

model = LinearRegression()

model.fit(X_train,Y_train)

# save model
with open("./model.pkl","wb") as file:
    pickle.dump(model, file)

print("Model trained and saved successfully")

# download model 
from google.colab import files
files.download("model.pkl")

