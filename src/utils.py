import os
import sys
import dill
import pandas as pd
from src.exception import CustomException
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV



def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        print(f"[save_object] About to save object to {file_path}")
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
        print(f"[save_object] Successfully saved object to {file_path}")

    except Exception as e:
        print(f"[save_object] Exception occurred: {e}")
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            print(f"Model: {list(models.keys())[i]}")
            print(f"  Train R2 Score: {train_model_score}")
            print(f"  Test R2 Score: {test_model_score}")
            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    # Sample data for testing
    import numpy as np
    from sklearn.linear_model import LinearRegression
    from sklearn.tree import DecisionTreeRegressor

    # Generate random data
    X_train = np.random.rand(100, 3)
    y_train = np.random.rand(100)
    X_test = np.random.rand(20, 3)
    y_test = np.random.rand(20)

    models = {
        "LinearRegression": LinearRegression(),
        "DecisionTree": DecisionTreeRegressor()
    }
    param = {
        "LinearRegression": {},
        "DecisionTree": {"max_depth": [2, 4, 6]}
    }

    print("Calling evaluate_models...")
    report = evaluate_models(X_train, y_train, X_test, y_test, models, param)
    print("Report:", report)


