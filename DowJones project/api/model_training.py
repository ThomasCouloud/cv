import xgboost as xgb
from sklearn.model_selection import GridSearchCV
import joblib
from prepro import preprocess_data, load_data
import os
from datetime import datetime

path_to_model_directory = os.path.join(os.path.dirname(__file__),'trainedModel')
if not os.path.exists(path_to_model_directory):
    os.makedirs(path_to_model_directory, exist_ok=True)

def train_and_save_model(train_X, train_y, best_params):
    xgb_grid = GridSearchCV(xgb.XGBRegressor(), best_params, cv=5, n_jobs=5, verbose=True)
    xgb_grid.fit(train_X, train_y)
    best_model = xgb.XGBRegressor(**xgb_grid.best_params_)
    best_model.fit(train_X, train_y)
    
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    timestamped_model_filename = os.path.join(path_to_model_directory, f"model_{current_datetime}.joblib")
    
    joblib.dump(best_model, timestamped_model_filename)

    return {"message": f"Model trained and saved successfully to {timestamped_model_filename}", "best_params": xgb_grid.best_params_}

if __name__ == "__main__":
    ticker = "AAPL"  
    train_X, train_y, _, _, _ = preprocess_data(load_data(ticker))
    best_params = { 
        'nthread': [4], 
        'objective': ['reg:squarederror'], 
        'learning_rate': [0.03, 0.05, 0.07], 
        'max_depth': [5, 6, 7], 
        'min_child_weight': [4], 
        'silent': [1], 
        'subsample': [0.7], 
        'colsample_bytree': [0.7], 
        'n_estimators': [100, 500, 1000]
    }
    result = train_and_save_model(train_X, train_y, best_params)
    print(result)