import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def main():
    """
    Climate Insight: A data science tool for climate modeling and analysis.
    
    This script provides a basic framework for loading climate data, 
    training a regression model, and evaluating its performance.
    
    Parameters:
    None
    
    Returns:
    None
    """
    # Load climate data
    data = pd.read_csv('climate_data.csv')
    
    # Preprocess data
    X = data.drop(['temperature'], axis=1)
    y = data['temperature']
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train a random forest regressor model
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)
    
    # Make predictions and evaluate the model
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse}')
    
    # Example usage
    example_input = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
    example_prediction = model.predict(example_input)
    print(f'Example Prediction: {example_prediction}')

if __name__ == '__main__':
    main()