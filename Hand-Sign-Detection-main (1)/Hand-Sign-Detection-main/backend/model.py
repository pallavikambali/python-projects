def train_gesture_model(csv_path):
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score, classification_report
    import joblib

    # Load data
    df = pd.read_csv(csv_path, header=None)

    # Split features and labels
    X = df.iloc[:, 1:]   # 42 features
    y = df.iloc[:, 0]    # label

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Model (strong baseline)
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    # Train
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nReport:\n", classification_report(y_test, y_pred))

    # Save model
    joblib.dump(model, "gesture_model.pkl")

    return model

train_gesture_model("gesture_data.csv")