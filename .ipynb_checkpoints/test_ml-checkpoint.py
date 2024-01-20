import pytest
# TODO: add necessary import
from sklearn.ensemble import RandomForestClassifier
from ml.model import (
    compute_model_metrics,
    inference,
    train_model
)

# TODO: implement the first test. Change the function name and input as needed
def test_train_model():
    """
    Check if train_model returns the expected result
    """
    # Your code here
    X_train = [[1,1,1,1,1],[1,1,1,1,1]]
    y_train = [[1,1,1,1,1],[1,1,1,1,1]]
    m = train_model(X_train, y_train)
    p = m.predict(X_train)
    assert p.all() == 1


# TODO: implement the second test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    Check if the compute_model_metrics function returns the expected value for F1
    """
    # Your code here
    y_test = [1,1,1,1,1]
    preds = [1,1,1,1,1]   
    p, r, fb = compute_model_metrics(y_test, preds)
    assert fb == 1


# TODO: implement the third test. Change the function name and input as needed
def test_inference():
    """
    Check if the inference functions returns the expected result
    """
    X_train = [[1,1,1,1,1],[1,1,1,1,1]]
    y_train = [[1,1,1,1,1],[1,1,1,1,1]]  
    X_test = [[1,1,1,1,1],[1,1,1,1,1]] 
    rf = RandomForestClassifier()
    model = rf.fit(X_train, y_train)
    p = inference(model, X_test)
    assert p.all() == 1