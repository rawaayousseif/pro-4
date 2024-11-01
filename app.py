import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
@st.cache
def load_data():
    data = pd.read_csv('data/vehicles_us.csv')
    data.columns = data.columns.str.lower()  # Normalize column names to lowercase
    return data

# Main app function
def main():
    st.title("Car Advertisement Analysis")
    st.write("Explore the used car market data and pricing trends.")

    # Load data
    data = load_data()

    # Display dataset
    if st.checkbox("Show raw data"):
        st.subheader("Raw Dataset")
        st.write(data)

    # Display summary statistics
    if st.checkbox("Show summary statistics"):
        st.subheader("Summary Statistics")
        st.write(data.describe())

    # Filter by model year
    model_year = st.slider("Filter by model year:", int(data['model_year'].min()), int(data['model_year'].max()), 2010)
    filtered_data = data[data['model_year'] >= model_year]
    st.write(f"Cars from {model_year} and newer:", filtered_data)

    # Price distribution plot
    st.subheader("Price Distribution")
    fig, ax = plt.subplots()
    ax.hist(filtered_data['price'], bins=30)
    ax.set_xlabel("Price")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

    # Mileage vs Price Scatter plot
    st.subheader("Mileage vs. Price")
    fig, ax = plt.subplots()
    ax.scatter(filtered_data['mileage'], filtered_data['price'])
    ax.set_xlabel("Mileage")
    ax.set_ylabel("Price")
    st.pyplot(fig)

# Run the app
if __name__ == "__main__":
    main()
