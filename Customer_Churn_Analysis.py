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
data.drop(data.columns[[13, 14, 16]], axis=1, inplace=True)
if "StreamingTV" not in data.columns and "StreamingMovies" not in data.columns and "PaperlessBilling" not in data.columns:
    print("Columns are dropped Successfully. :)")  #Checking if the columns dropped or not
else:
    print("Columns not dropped. :(")

data.info() #Displaying the data after removal of unnecessary data

# In our analysis I've examined the number of unique values in each dataset column. This exploration provides insights into the diversity and distribution of data attributes.
# Displaying the unique values
for i in data.columns:
    print("No. of unique values in",i,"is",data[i].nunique())

# Some common Variables
mask = data["Churn"] == "Yes"
mask2 = data["Churn"] == "No"
churned = data[data["Churn"] == "Yes"]
not_churned = data[data["Churn"] == "No"]
genders = ["Male", "Female"]
churn_customer = churned["customerID"].value_counts()
notchurn_customer = not_churned["customerID"].value_counts()

# Collecting the number of customers who are churned and who are not churned
print("Number of Customers who are Churned : ", churn_customer) # Dispalying the number of churned cusotmers
print("Number of customers who are not churned : ", notchurn_customer) # Dispalying the number of non-churned cusotmers
plt.title("Churned vs Non-Churned Customers") # Giving the title for the graph
sns.countplot(data=data, x="Churn", palette="dark") # Plotting the graph
plt.grid(True) # Providing the gridding for the graph
plt.show() # Dispalying the graph

# Comparing the between the genders who are customer churned
gender_count = churned["gender"].value_counts() # Counting the number of genders(males and females) in the customer list who are churned
print("Number of males and females : ")
print(gender_count) # Displaying the the gender count data
gender_plot = data.loc[mask, ["customerID", "gender"]] # Selecting the data
plt.title("Male vs Female in Churned Customers") # Giving the title for the graph
plt.pie(gender_count, labels=["Male", "Female"], autopct="%1.1f%%", shadow=True) # Plotting the graph
plt.show() # Displaying the graph

# Comparing the data of genders of senior citizens who are churned and non-churned
churned_counts = churned.groupby("gender")["SeniorCitizen"].sum() # Summing the number senior citizens who are churned on the basis of gender
not_churned_counts = not_churned.groupby("gender")["SeniorCitizen"].sum() # Summing the number senior citizens who are non-churned on the basis of gender
bar_width = 0.35
index = range(len(genders))
plt.title("Senior Citizen Comparison: Churned vs Non-Churned Customers") # Giving the title for the graph
plt.bar(index, churned_counts, bar_width, color="red", label="Churned") # Plotting the graph
plt.bar([i + bar_width for i in index], not_churned_counts, bar_width, color="green", label="Non-Churned") # Plotting the graph
plt.xlabel("Gender") # Providing the the name for x-axis 
plt.ylabel("Count") # Providing the the name for x-axis
plt.xticks([i + bar_width/2 for i in index], genders) #  Sets the x-axis ticks centered under each pair of bars, labeled with genders.
plt.legend(loc="upper left") # Displaying the meaning of the colored bars and positon of it to dispaly.
plt.grid(True) # Providing the gridding for the graph
plt.show() # Dispalying the graph

# Plotting churn rates by PaymentMethod
plt.figure(figsize=(10, 6)) # Setting the figure size
plt.title("Churn Rates by Payment Method") # Giving the title for the graph
sns.countplot(x="PaymentMethod", hue="Churn", data=data) # Plotting the graph
plt.xlabel("Payment Method") # Providing the the name for x-axis
plt.ylabel("Count") # Providing the the name for y-axis
plt.legend(title="Churn", loc="upper right", labels=["No", "Yes"]) # Displaying the title, meaning of the colored bars and positon of it to dispaly.
plt.xticks(rotation=45) # Rotating x-axis labels for better readability
plt.grid(True) # Providing the gridding for the graph
plt.show() # Dispalying the graph

# calculating the average tenure of churned customers by each category of contracts
avg_tenure = churned.groupby("Contract")["tenure"].mean().reset_index() # Calculating the mean of tenure on each cataegory of contract 
plt.title("Contract wise average tenure") # Giving the title for the graph 
sns.lineplot(x="Contract", y="tenure", data=avg_tenure) # Plotting the graph
plt.xlabel("Contract Types") # Providing the the name for x-axis
plt.ylabel("Tenure") # Providing the the name for y-axis
plt.grid(True) # Providing the gridding for the graph
plt.show() # Dispalying the graph

# Plotting churn rates by Contract type
plt.title("Churn Rates by Contract Type") # Giving the title for the graph
sns.countplot(x="Contract", hue="Churn", data=data) # Plotting the graph
plt.xlabel("Contract Type") # Providing the the name for x-axis
plt.ylabel("Count") # Providing the the name for y-axis
plt.legend(title="Churn", loc="upper right", labels=["No", "Yes"]) # Displaying the title, meaning of the colored bars and positon of it to dispaly.
plt.grid(True) # Providing the gridding for the graph
plt.show() # Dispalying the graph

# Comparing the data of types of paymnet methods used by churned and n
method1 = churned["PaymentMethod"].value_counts() # Counting the number of times each churned customer used which categories of payment methods
method2 = not_churned["PaymentMethod"].value_counts() # Counting the number of times each non-churned customer used which categories of payment methods
plt.title("Churn Rates by Contract Type") # Giving the title for the graph
plt.figure(figsize=(10, 6)) # Setting the figure size
plt.plot(method1.index, method1.values, color="darkred", marker="o") # Plotting the graph
plt.plot(method2.index, method2.values, linestyle="--", color="darkblue", marker="s") # Plotting the graph
plt.xlabel("Payment Method Type") # Providing the the name for x-axis
plt.ylabel("Count") # Providing the the name for y-axis
plt.legend(title="Churn", loc="upper right", labels=["No", "Yes"]) # Displaying the title, meaning of the colored bars and positon of it to dispaly.
plt.grid(True) # Providing the gridding for the graph
plt.show() # Dispalying the graph

# Calculate churn rates (%) for each service
services = ["OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport"] # Listing the online services provided by the Telecom Services
churn_rates = [] # Empty List 
# Filtering the data, calculating the churn rate as a percentage, retrieves the churn percentage for "Yes" and storing it
for service in services:
    service_churn_rate = data[data[service] == "Yes"]["Churn"].value_counts(normalize=True).mul(100).get("Yes", 0)
    churn_rates.append(service_churn_rate)
# Plotting the line graph
plt.figure(figsize=(10, 6)) # Setting the figure size
plt.title("Churn Rate Comparison by Services") # Giving the title for the graph
plt.plot(services, churn_rates, marker='o', linestyle="-", color="b", label="Churn Rate (%)") # Plotting the graph
plt.xlabel("Services") # Providing the the name for x-axis
plt.ylabel("Churn Rate (%)") # Providing the the name for y-axis
plt.xticks(rotation=45) # Rotating x-axis labels for better readability
plt.grid(True) # Providing the gridding for the graph
plt.legend() # Dispalying the labels defined during plotting
plt.tight_layout() # Adjusting layout to prevent overlapping
plt.show() # Dispalying the graph

# Select only numerical columns
# Slecting the columns containing the numerical data types and retrieving the name
numerical_cols = data.select_dtypes(include=[np.number]).columns
# Correlation matrix
plt.figure(figsize=(12, 8)) # Setting the figure size
plt.title("Correlation Matrix") # Giving the title for the graph
sns.heatmap(data[numerical_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f") # Plotting the graph
plt.show() # Dispalying the graph

# Plotting the Average tenure of the Churned customers
avg_tenure = churned.groupby("Contract")["tenure"].mean() # Getting mean of the tenures on the basis of contracts of churned customers
print("Average Tenure of churned customers : ", avg_tenure) # Displaying the average tenure
plt.figure() # Setting the figure
plt.title("Average Tenure of Churned cutomer") # Giving the title for the graph
sns.boxplot(x="Contract", y="tenure", data=churned) # Plotting the graph
plt.grid(True) # Providing the gridding for the graph
plt.show() # Dispalying the graph

# Plotting the Average Monthly Charges of the Churned customers
avg_monthly = churned.groupby("Contract")["MonthlyCharges"].mean() # Getting mean of the Monthly Charges on the basis of contracts of churned customers
print("Average Monthly Charges of churned customers : ", avg_monthly) # Displaying the average monthly charges
plt.figure() # Setting the figure
plt.title("Average Monthly Charges of Churned cutomer") # Giving the title for the graph
sns.boxplot(x="Contract", y="MonthlyCharges", data=churned) # Plotting the graph
plt.grid(True) # Providing the gridding for the graph
plt.show() # Dispalying the graph

# Plotting the Average Total Chargess of the Churned customers
churned[["TotalCharges"]] = churned[["TotalCharges"]].apply(pd.to_numeric, errors="coerce") #Converting the data type object to numeric
print(churned["TotalCharges"].dtype) # Printing the datatypes
avg_total = churned.groupby("Contract")["TotalCharges"].mean() # Getting mean of the Toatal Charges on the basis of contracts of churned customers
print("Average Total Charges of churned customers : ", avg_total) # Displaying the average total charges
plt.figure() # Setting the figure
plt.title("Average Total Charges of Churned cutomer") # Giving the title for the graph
sns.boxplot(x="Contract", y="TotalCharges", data=churned) # Plotting the graph
plt.grid(True) # Providing the gridding for the graph
plt.show() # Dispalying the graph

#Create a histogram to compare Monthly Charges for Churned vs. Non-Churned Customers
plt.figure(figsize=(20, 6)) # Setting the figure
plt.subplot(1,3,1) # Diving the graph in small parts
plt.title("Distribution of Monthly Charges for Churned vs. Non-Churned Customers") # Giving the title for the graph
sns.histplot(data=data, x="MonthlyCharges", hue="Churn", multiple="stack", kde=True) # Plotting the graph
plt.xlabel("Monthly Charges") # Providing the the name for x-axis
plt.ylabel("Count") # Providing the the name for y-axis
plt.grid(True) # Providing the gridding for the graph
plt.show() # Dispalying the graph

# Counting occurrences of Partner and Dependents
partner_dependents_counts = data.groupby(["Partner", "Dependents"]).size().reset_index(name="Count") # Getting and counting the data of customers having partners and dependents
plt.figure(figsize=(8, 8)) # Setting the figure
plt.title("Proportion of Customers by Partner and Dependents", pad=20)  # Giving the title for the graph
plt.pie(partner_dependents_counts["Count"], labels=partner_dependents_counts.apply(lambda x: f"Partner: {x["Partner"]}, Dependents: {x["Dependents"]}", axis=1), 
        autopct='%1.1f%%', startangle=140, colors=["#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3"]) # Plotting the graph
plt.axis("equal") # Ensuring the graph is in proper shape and size
plt.grid(True) # Providing the gridding for the graph
plt.show() # Dispalying the graph

# Plotting the Average tenure of the Churned customers by Payment Method
avg_tenure_payment = churned.groupby("PaymentMethod")["tenure"].mean() # Getting mean of the Tenure on the basis of contracts of churned customers
print("Average Tenure of churned customers by Payment Method :\n", avg_tenure_payment) # Displaying the average tenure on payment methods
plt.figure(figsize=(8, 4)) # Setting the figure
plt.title("Average Tenure of Churned Customers by Payment Method") # Giving the title for the graph
sns.boxplot(x="PaymentMethod", y="tenure", data=churned) # Plotting the graph
plt.xlabel("Payment Method") # Providing the the name for x-axis
plt.ylabel("Tenure") # Providing the the name for y-axis
plt.grid(True) # Providing the gridding for the graph
plt.xticks(rotation=45) # Rotating x-axis labels for better readability
plt.show() # Dispalying the graph

# Plotting the Average Monthly Charges of the Churned customers by Payment Method
avg_monthly_payment = churned.groupby("PaymentMethod")["MonthlyCharges"].mean() # Getting mean of the Monthly Charges on the basis of contracts of churned customers
print("Average Monthly Charges of churned customers by Payment Method :\n", avg_monthly_payment) # Displaying the average monthly charges on payment methods
plt.figure(figsize=(8, 4)) # Setting the figure
plt.title("Average Monthly Charges of Churned Customers by Payment Method") # Giving the title for the graph
sns.boxplot(x="PaymentMethod", y="MonthlyCharges", data=churned) # Plotting the graph
plt.xlabel("Payment Method") # Providing the the name for x-axis
plt.ylabel("Monthly Charges") # Providing the the name for y-axis
plt.grid(True) # Providing the gridding for the graph
plt.xticks(rotation=45) # Rotating x-axis labels for better readability
plt.show() # Dispalying the graph

# Plotting the Average Total Charges of the Churned customers by Payment Method
avg_total_payment = churned.groupby("PaymentMethod")["TotalCharges"].mean() # Getting mean of the Total Charges on the basis of contracts of churned customers
print("Average Total Charges of churned customers by Payment Method :\n", avg_total_payment) # Displaying the average total charges on payment methods
plt.figure(figsize=(8, 4)) # Setting the figure
plt.title("Average Total Charges of Churned Customers by Payment Method") # Giving the title for the graph
sns.boxplot(x="PaymentMethod", y="TotalCharges", data=churned) # Plotting the graph
plt.xlabel("Payment Method") # Providing the the name for x-axis
plt.ylabel("Total Charges") # Providing the the name for y-axis
plt.grid(True) # Providing the gridding for the graph
plt.xticks(rotation=45) # Rotating x-axis labels for better readability
plt.show() # Dispalying the graph