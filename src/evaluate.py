from sklearn.metrics import accuracy_score, classification_report

def evaluate_model(model, X_test, y_test, model_name="Model"):
    # Prints accuracy and classification report for a given model
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print(model_name)
    print(f"Accuracy: {accuracy * 100:.2f}%\n")
    print(classification_report(y_test, predictions))