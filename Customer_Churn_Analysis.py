# Importing the pandas library 
import pandas as pd

# Importing the matplotlib library for plotting the data
import matplotlib.pyplot as plt

# Importing the seaborn library for also plotting the data
import seaborn as sns

# Importing the Numpy library for storing and arranging the data
import numpy as np

# Reading, Loading and Displaying the data of csv file
read = pd.read_csv("D:\Downloads\Telco-Customer-Churn.csv") #Reading the data

data = pd.DataFrame(read) #Loading and making the DataFrame 
data.head() # Dispalying the frist few rows of dataframe

data.info()  #Getting information about the dataframe (columns, data types, non-null values)

data.describe() #Getting the summary statistics of numerical columns

# Dropping the unuseful columns and data from the csv file
data.drop(data.columns[[14, 16]], axis=1, inplace=True)
if "StreamingMovies" not in data.columns and "PaperlessBilling" not in data.columns:
    print("Columns are dropped Successfully. :)")
else:
    print("Columns not dropped. :(")

# Some common Variables
mask = data["Churn"] == "Yes"
mask2 = data["Churn"] == "No"
churned = data[data["Churn"] == "Yes"]
not_churned = data[data["Churn"] == "No"]
genders = ["Male", "Female"]
churn_customer = churned["customerID"].value_counts()
notchurn_customer = not_churned["customerID"].value_counts()

# Collecting the number of customers who are churned and who are not churned
print("Number of Customers who are Churned : ", churn_customer)
print("Number of customers who are not churned : ", notchurn_customer)
plt.title("Churned vs Non-Churned Customers")
sns.countplot(data=data, x="Churn", palette="dark")
plt.grid(True)
plt.show()

# Comparing the between the genders who are customer churned
gender_count = churned["gender"].value_counts()
print("Number of males and females : ")
print(gender_count)
gender_plot = data.loc[mask, ["customerID", "gender"]]
plt.title("Male vs Female in Churned Customers")
plt.pie(gender_count, labels=["Male", "Female"], autopct="%1.1f%%", shadow=True)
plt.show()

# Comparing the data of genders of senior citizens who are churned and non-churned
churned_counts = churned.groupby("gender")["SeniorCitizen"].sum()
not_churned_counts = not_churned.groupby("gender")["SeniorCitizen"].sum()
bar_width = 0.35
index = range(len(genders))
plt.title("Senior Citizen Comparison: Churned vs Non-Churned Customers")
plt.bar(index, churned_counts, bar_width, color="red", label="Churned")
plt.bar([i + bar_width for i in index], not_churned_counts, bar_width, color="green", label="Non-Churned")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.xticks([i + bar_width/2 for i in index], genders)
plt.legend(loc="upper left")
plt.grid(True)
plt.show()

# Plotting churn rates by PaymentMethod
plt.figure(figsize=(10, 6))
sns.countplot(x='PaymentMethod', hue='Churn', data=data)
plt.title('Churn Rates by Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Count')
plt.legend(title='Churn', loc='upper right', labels=['No', 'Yes'])
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# calculating the average tenure of churned customers by each category of contracts
avg_tenure = churned.groupby("Contract")["tenure"].mean().reset_index()
plt.title("Contract wise average tenure")
sns.lineplot(x="Contract", y="tenure", data=avg_tenure)
plt.xlabel("Contract Types")
plt.ylabel("Tenure")
plt.grid(True)
plt.show()

