import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


data_1y = pd.read_csv("stock_data_with_history_1y_updated.csv")
data_2y = pd.read_csv("stock_data_with_history_2y_updated.csv")
data_5y = pd.read_csv("stock_data_with_history_5y_updated.csv")

data = pd.concat([data_1y, data_2y, data_5y], ignore_index=True)

y_data_dependent = data["Close"]
x_data_independent = data[["Open","High","Low","Volume","Dividends","Stock Splits"]]

x_train, x_test, y_train, y_test = train_test_split(x_data_independent,y_data_dependent,test_size=0.3)

classifier = LinearRegression()
classifier.fit(x_train,y_train)

predictions = classifier.predict(x_test)

print(predictions)

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
accuracy = r2 * 100  # accuracy calculation

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")
print(f"Accuracy on Test Data: {accuracy:.2f}%") 

print("\n")

unseen_data = pd.read_csv("Unseen_data.csv")

unseen_features = unseen_data[["Open", "High", "Low", "Volume", "Dividends", "Stock Splits"]]

unseen_predictions = classifier.predict(unseen_features)

if "Close" in unseen_data.columns:
    true_values = unseen_data["Close"]
    mse_unseen = mean_squared_error(true_values, unseen_predictions)
    r2_unseen = r2_score(true_values, unseen_predictions)
    accuracy_unseen = r2_unseen * 100  # <-- Accuracy percentage for unseen data

    print(f"Unseen Data Mean Squared Error: {mse_unseen}")
    print(f"Unseen Data R-squared: {r2_unseen}")
    print(f"Accuracy on Unseen Data: {accuracy_unseen:.2f}%")  # <-- Accuracy printed here

print("Predictions for Unseen Data:")
print(unseen_predictions)
