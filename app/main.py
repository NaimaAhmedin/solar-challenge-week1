import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Solar Energy Dashboard", layout="wide")

st.title("☀️ Solar Energy Dashboard")

# Upload CSV file
uploaded_file = st.file_uploader("Upload cleaned solar dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip()  # Remove spaces in column names

    st.write("Available columns:", df.columns.tolist())

    if "Month" in df.columns and "DNI" in df.columns:
        # Select months to visualize
        selected_months = st.multiselect(
            "Select Months", options=sorted(df["Month"].unique()), default=sorted(df["Month"].unique())
        )

        filtered_df = df[df["Month"].isin(selected_months)]

        # Boxplot of DNI by Month
        st.subheader("Boxplot of DNI by Month")
        fig, ax = plt.subplots()
        sns.boxplot(data=filtered_df, x="Month", y="DNI", palette="Set2", ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # Top Months by Avg DNI
        st.subheader("Top Months by Average DNI")
        top_months = (
            filtered_df.groupby("Month")["DNI"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
            .rename(columns={"DNI": "Average DNI"})
        )
        st.dataframe(top_months)

    else:
        st.error("Required columns ('Month' and 'DNI') not found in the uploaded dataset.")
