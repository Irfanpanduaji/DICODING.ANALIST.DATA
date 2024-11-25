import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='darkgrid')

day_df = pd.read_csv("all_data.csv")
day_df.head()

drop_col = ['instant', 'temp', 'atemp', 'hum', 'windspeed']
day_df.drop(columns=drop_col, inplace=True)

day_df['yr'] = day_df['yr'].map({
    0: '2011',
    1: '2012'
})
day_df['mnth'] = day_df['mnth'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'Mei', 6: 'Jun', 
})
day_df['season'] = day_df['season'].map({
    1: 'Musim Semi', 2: 'Musim Panas', 3: 'Musim Gugur', 4: 'Musim Dingin'
})
day_df['weekday'] = day_df['weekday'].map({
    0: 'Minggu', 1: 'Senin', 2: 'Selasa', 3: 'Rabu', 4: 'Kamis', 5: 'Jumat', 6: 'Sabtu'
})
day_df['weathersit'] = day_df['weathersit'].map({
    1: 'Cerah',
    2: 'Berawan',
    3: 'Hujan/Salju Ringan',
    4: 'Cuaca Buruk'
})
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
day_df[['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit']] = day_df[[
    'season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit']].astype('category')

day_df = day_df[day_df['mnth'].isin(['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun'])]

def create_season_rent_df(df):
    season_rent_df = df.groupby(by='season')[['registered', 'casual']].sum().reset_index()
    return season_rent_df

def create_monthly_rent_df(df):
    monthly_rent_df = df.groupby(by='mnth').agg({
        'cnt': 'sum'
    }).reset_index()
    ordered_months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun']
    monthly_rent_df['mnth'] = pd.Categorical(monthly_rent_df['mnth'], categories=ordered_months, ordered=True)
    return monthly_rent_df

def create_weather_rent_df(df):
    weather_rent_df = df.groupby(by='weathersit').agg({
        'cnt': 'sum'
    }).reset_index()
    return weather_rent_df

min_date = day_df['dteday'].min().date()
max_date = day_df['dteday'].max().date()

with st.sidebar:
    
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = day_df[(day_df['dteday'] >= pd.to_datetime(start_date)) & 
                (day_df['dteday'] <= pd.to_datetime(end_date))]

season_rent_df = create_season_rent_df(main_df)
monthly_rent_df = create_monthly_rent_df(main_df)
weather_rent_df = create_weather_rent_df(main_df)

st.header('DATA ANALIST PENGGUNAAN SEPEDA SELAMA 6 BULAN')

st.subheader('Jumlah Pengguna dalam 6 Bulan')
fig, ax = plt.subplots(figsize=(24, 8))
ax.plot(
    monthly_rent_df['mnth'],
    monthly_rent_df['cnt'],
    marker='o', 
    linewidth=2,
    color='tab:green'
)

for index, row in monthly_rent_df.iterrows():
    ax.text(index, row['cnt'] + 1, str(row['cnt']), ha='center', va='bottom', fontsize=12)

ax.tick_params(axis='x', labelsize=25, rotation=45)
ax.tick_params(axis='y', labelsize=20)
st.pyplot(fig)

st.subheader('Data Hubungan Cuaca dengan Musim')
fig, ax = plt.subplots(figsize=(10,6))
sns.barplot(x='mnth',
            y='cnt',
            data=day_df.groupby('mnth', observed=False)['cnt'].sum().reset_index(),
            ax=ax)
ax.set_title('Jumlah Pengguna Sepeda per Bulan (Jan-Jun)')
ax.set_xlabel('Bulan')
ax.set_ylabel('Jumlah Pengguna Sepeda')
st.pyplot(fig)

st.subheader('Heatmap Korelasi Data')
numerical_df = day_df.select_dtypes(include=['number'])
corr_matrix = numerical_df.corr()
fig, ax = plt.subplots(figsize=(10,8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True, ax=ax)
ax.set_title('Heatmap Korelasi Antar Variabel')
st.pyplot(fig)
