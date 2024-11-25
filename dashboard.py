import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='darkgrid')

day_df = pd.read_csv("all_data.csv")
day_df.head()

# Preprocessing data
drop_col = ['instant', 'temp', 'atemp', 'hum', 'windspeed']
day_df.drop(columns=drop_col, inplace=True)

day_df['yr'] = day_df['yr'].map({0: '2011', 1: '2012'})
day_df['mnth'] = day_df['mnth'].map({1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'Mei', 6: 'Jun'})
day_df['season'] = day_df['season'].map({1: 'Musim Semi', 2: 'Musim Panas', 3: 'Musim Gugur', 4: 'Musim Dingin'})
day_df['weekday'] = day_df['weekday'].map({0: 'Minggu', 1: 'Senin', 2: 'Selasa', 3: 'Rabu', 4: 'Kamis', 5: 'Jumat', 6: 'Sabtu'})
day_df['weathersit'] = day_df['weathersit'].map({1: 'Cerah', 2: 'Berawan', 3: 'Hujan/Salju Ringan', 4: 'Cuaca Buruk'})
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
day_df[['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit']] = day_df[['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit']].astype('category')

# Filter data for the months Jan to Jun
day_df = day_df[day_df['mnth'].isin(['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun'])]

# Function to create monthly rent DataFrame
def create_monthly_rent_df(df):
    monthly_rent_df = df.groupby(by='mnth').agg({'cnt': 'sum'}).reset_index()
    ordered_months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun']
    monthly_rent_df['mnth'] = pd.Categorical(monthly_rent_df['mnth'], categories=ordered_months, ordered=True)
    return monthly_rent_df

# Function to create season and weather DataFrame
def create_season_weather_df(df):
    season_weather_df = df.groupby(['season', 'weathersit']).agg({'cnt': 'mean'}).reset_index()
    return season_weather_df

# Streamlit app
st.header('DATA ANALIST PENGGUNAAN SEPEDA SELAMA 6 BULAN')

# Monthly counts
monthly_rent_df = create_monthly_rent_df(day_df)

st.subheader('Jumlah Total Penyewa Sepeda per Bulan')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=monthly_rent_df, x='mnth', y='cnt', ax=ax)
ax.set_title('Jumlah Total Penyewa Sepeda Tahun 2011')
ax.set_xlabel('Bulan')
ax.set_ylabel('Jumlah Penyewa')
ax.grid(axis='y')
st.pyplot(fig)

# Find month with highest users
max_users = monthly_rent_df.loc[monthly_rent_df['cnt'].idxmax()]
st.write(f"Jumlah pengguna tertinggi terjadi pada bulan {max_users['mnth']} "
         f"dengan total {max_users['cnt']} penyewa sepeda.")

# Season and weather analysis
season_weather_df = create_season_weather_df(day_df)

st.subheader('Rata-Rata Jumlah Pengguna Sepeda Berdasarkan Kondisi Cuaca dan Musim')
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=season_weather_df, x='weathersit', y='cnt', hue='season', palette='Set2', ax=ax)
ax.set_title('Rata-Rata Jumlah Pengguna Sepeda Berdasarkan Kondisi Cuaca dan Musim')
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Rata-Rata Jumlah Pengguna Sepeda')
ax.legend(title='Musim', loc='upper right')
st.pyplot(fig)

# Find max usage combination
max_usage = season_weather_df.loc[season_weather_df['cnt'].idxmax
