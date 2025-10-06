import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score

st.title("📊 Beginner-Friendly ML Dashboard")

# --- Step 1: Upload CSV ---
file = st.file_uploader("Upload your CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)

    # --- Step 2: Remove ID/Index Columns Automatically ---
    for col in df.columns:
        if "id" in col.lower() or col.lower() == "index":
            df.drop(col, axis=1, inplace=True)

    # --- Step 3: Data Preview ---
    st.subheader("Data Preview")
    st.dataframe(df.head(10))

    # --- Step 4: Summary Statistics ---
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # --- Step 5: Boxplot for Selected Feature ---
    st.subheader("Boxplot for Outliers")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    if numeric_cols:
        selected_box_col = st.selectbox("Select numeric column for boxplot", numeric_cols)
        plt.figure(figsize=(6,4))
        sns.boxplot(df[selected_box_col])
        st.pyplot(plt)
    else:
        st.info("No numeric columns available for boxplot.")

    # --- Step 6: Correlation Heatmap (if 2+ numeric columns) ---
    st.subheader("Correlation Heatmap")
    if len(numeric_cols) >= 2:
        selected_corr_cols = st.multiselect("Select at least 2 numeric columns for correlation", numeric_cols, default=numeric_cols[:2])
        if len(selected_corr_cols) >= 2:
            plt.figure(figsize=(6,4))
            sns.heatmap(df[selected_corr_cols].corr(), annot=True, cmap="coolwarm")
            st.pyplot(plt)
        else:
            st.warning("Please select at least 2 columns for correlation heatmap.")
    else:
        st.info("Not enough numeric columns for correlation heatmap.")

    # --- Step 7: Select Model and Features ---
    st.subheader("Machine Learning Model Training")
    model_type = st.selectbox("Select model type", ["Linear Regression", "Logistic Regression"])
    target_column = st.selectbox("Select target column (y)", df.columns)
    feature_columns = st.multiselect("Select feature columns (X)", [col for col in df.columns if col != target_column])

    # --- Step 8: Train Model Only When Button Pressed ---
    if st.button("Train Model"):
        if not feature_columns:
            st.warning("Please select at least one feature column for training.")
        else:
            X = df[feature_columns]
            y = df[target_column]

            # --- Step 9: Split Data ---
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # --- Step 10: Train Model ---
            if model_type == "Linear Regression":
                model = LinearRegression()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)
                st.success("Linear Regression Trained Successfully!")
                st.write(f"R2 Score: {r2_score(y_test, y_pred):.2f}")
                st.write(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}")
            elif model_type == "Logistic Regression":
                model = LogisticRegression(max_iter=1000)
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)
                st.success("Logistic Regression Trained Successfully!")
                st.write(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

            # --- Step 11: Show Predictions vs Actual ---
            st.subheader("Prediction vs Actual")
            result_df = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
            st.dataframe(result_df.head(10))
