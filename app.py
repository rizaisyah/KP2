import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from datetime import datetime, time
from plotly.subplots import make_subplots
import seaborn as sns
from pytube import YouTube
from PIL import Image
import requests
from io import BytesIO

# Load data
data = pd.read_csv('19-23 ISPU Kota Yogyakarta.csv')
data['Waktu'] = pd.to_datetime(data['Waktu'])
option = st.sidebar.selectbox('Select Option', ('Introduction', 'ISPU tool', 'Analysis Tool', 'Download Resources'))
if option == 'Introduction':
    # Display introduction content
    st.title('Welcome to the Streamlit App')
    st.write('This app provides an introduction to Streamlit and its features.')
    st.write('Feel free to explore the different options in the sidebar.')
        # YouTube video link
    video_link = "https://www.youtube.com/watch?v=OBCuZGLKygg"
    st.video(video_link)
elif option == 'ISPU tool'
        st.write('ISPU tool selected')
    
        data['Waktu'] = pd.to_datetime(data['Waktu'])
    
        option = st.radio("Select ISPU Calculation Option:", ('Manual Input', 'From Data'))
    
        def get_category(I):
            if I >= 1 and I <= 50:
                return "Baik"
            elif I >= 51 and I <= 100:
                return "Sedang"
            elif I >= 101 and I <= 200:
                return "Tidak Sehat"
            elif I >= 201 and I <= 300:
                return "Sangat Tidak Sehat"
            elif I >= 301:
                return "Berbahaya"
            else:
                return "Kategori tidak ditemukan"
    
        if option == 'Manual Input':
            data_manual = {
                'ISPU': [0, 50, 100, 200, 300, 1000],
                'PM10': [0, 50, 150, 350, 420, 500],
                'PM2p5': [0, 15.5, 55.4, 150.4, 250.4, 500],
                'SO2': [0, 52, 180, 400, 800, 1000],
                'CO': [0, 4000, 8000, 15000, 30000, 45000],
                'O3': [0, 120, 235, 400, 800, 1000],
                'NO2': [0, 80, 200, 1130, 2260, 3000],
                'HC': [0, 45, 100, 215, 432, 648]
            }
    
            df_manual = pd.DataFrame(data_manual)
    
            st.sidebar.title('ISPU Calculator')
            st.sidebar.markdown('''Jenis partikel:
            PM10 (1) | PM2p5 (2) | SO2 (3) | CO (4) | O3 (5) | NO2 (6) | HC (7)''')
            partikel = st.sidebar.selectbox('Select Partikel', ['PM10', 'PM2p5', 'SO2', 'CO', 'O3', 'NO2', 'HC'])
            xx = st.sidebar.number_input('Konsentrasi ambien nyata hasil pengukuran')
    
            if partikel in df_manual.columns:
                xb = df_manual.loc[df_manual[partikel] <= xx, partikel].max()
                xa = df_manual.loc[df_manual[partikel] >= xx, partikel].min()
                ib = df_manual.loc[df_manual[partikel] == xb, 'ISPU'].values[0]
                ia = df_manual.loc[df_manual[partikel] == xa, 'ISPU'].values[0]
    
                if isinstance(ia, str) or isinstance(ib, str):
                    st.write(f'Invalid ISPU values for {partikel}')
                else:
                    i = ((ia - ib) / (xa - xb)) * (xx - xb) + ib
                    st.write(f'ISPU terhitung (I) {partikel}: {i}')
    
                    category = get_category(i)
                    st.write("Kategori status: ", category)
    
            else:
                st.write(f'Invalid partikel selection: {partikel}')
    
        elif option == 'From Data':
                data['ISPU_PM10'] = pd.cut(data['PM10'], bins=[-float('inf'), 50, 150, 350, 420, 500, float('inf')], labels=[0, 50, 100, 200, 300, 1000])
                data['ISPU_PM2p5'] = pd.cut(data['PM2p5'], bins=[-float('inf'), 15.5, 55.4, 150.4, 250.4, 500, float('inf')], labels=[0, 50, 100, 200, 300, 1000])
                data['ISPU_SO2'] = pd.cut(data['SO2'], bins=[-float('inf'), 52, 180, 400, 800, 1000, float('inf')], labels=[0, 50, 100, 200, 300, 1000])
                data['ISPU_CO'] = pd.cut(data['CO'], bins=[-float('inf'), 4000, 8000, 15000, 30000, 45000, float('inf')], labels=[0, 50, 100, 200, 300, 1000])
                data['ISPU_O3'] = pd.cut(data['O3'], bins=[-float('inf'), 120, 235, 400, 800, 1000, float('inf')], labels=[0, 50, 100, 200, 300, 1000])
                data['ISPU_NO2'] = pd.cut(data['NO2'], bins=[-float('inf'), 80, 200, 1130, 2260, 3000, float('inf')], labels=[0, 50, 100, 200, 300, 1000])
                data['ISPU_HC'] = pd.cut(data['HC'], bins=[-float('inf'), 45, 100, 215, 432, 648, float('inf')], labels=[0, 50, 100, 200, 300, 1000])
            
                st.write(data)
            
                # Convert categorical columns to numeric
                data['ISPU_PM2p5'] = pd.to_numeric(data['ISPU_PM2p5'])
                data['ISPU_PM10'] = pd.to_numeric(data['ISPU_PM10'])
                data['ISPU_SO2'] = pd.to_numeric(data['ISPU_SO2'])
                data['ISPU_CO'] = pd.to_numeric(data['ISPU_CO'])
                data['ISPU_O3'] = pd.to_numeric(data['ISPU_O3'])
                data['ISPU_NO2'] = pd.to_numeric(data['ISPU_NO2'])
                data['ISPU_HC'] = pd.to_numeric(data['ISPU_HC'])
            
                # Date range selection
                start_date = st.date_input('Start Date')
                end_date = st.date_input('End Date')
            
                # Convert start_date and end_date to datetime objects
                start_datetime = pd.to_datetime(start_date)
                end_datetime = pd.to_datetime(end_date)
            
                # Filter data based on date range
                filtered_data = data[(data['Waktu'].dt.date >= start_datetime) & (data['Waktu'].dt.date <= end_datetime)]
            
                # Calculate the mean ISPU for each pollutant
                mean_ISPU_PM2p5 = filtered_data['ISPU_PM2p5'].mean()
                mean_ISPU_PM10 = filtered_data['ISPU_PM10'].mean()
                mean_ISPU_SO2 = filtered_data['ISPU_SO2'].mean()
                mean_ISPU_CO = filtered_data['ISPU_CO'].mean()
                mean_ISPU_O3 = filtered_data['ISPU_O3'].mean()
                mean_ISPU_NO2 = filtered_data['ISPU_NO2'].mean()
                mean_ISPU_HC = filtered_data['ISPU_HC'].mean()
            
                # Create a bar chart
                pollutants = ['PM2.5', 'PM10', 'SO2', 'CO', 'O3', 'NO2', 'HC']
                mean_ISPU_values = [mean_ISPU_PM2p5, mean_ISPU_PM10, mean_ISPU_SO2, mean_ISPU_CO, mean_ISPU_O3, mean_ISPU_NO2, mean_ISPU_HC]
                
                # Define color list and labels based on ISPU value ranges
                colors = ['green' if value <= 50 else 'blue' if value <= 100 else 'yellow' if value <= 200 else 'red' if value <= 300 else 'black' for value in mean_ISPU_values]
                labels = ['Sehat' if value <= 50 else 'Sedang' if value <= 100 else 'Tidak Sehat' if value <= 200 else 'Sangat Tidak Sehat' if value <= 300 else 'Berbahaya' for value in mean_ISPU_values]
                
                fig = go.Figure(data=[go.Bar(x=pollutants, y=mean_ISPU_values, marker=dict(color=colors))])
                fig.update_layout(
                    title='Mean ISPU Values for Pollutants',
                    xaxis_title='Pollutants',
                    yaxis_title='Mean ISPU Values'
                )
                
                # Add labels to the bars
                for i, value in enumerate(mean_ISPU_values):
                    fig.add_annotation(
                        x=pollutants[i],
                        y=value,
                        text=labels[i],
                        showarrow=False,
                        font=dict(color='black', size=12),
                        yshift=10 if value > 300 else -20
                    )
    
                st.plotly_chart(fig)
                
elif option == 'Analysis tools':
        # Display tools content
        st.title('Tools')
        st.write('Choose a tool from the options below.')
        st.write('Correlation tool selected')
        # Select pollutant columns (B to H) and meteorology columns (I to P)
        pollutant_columns = data.columns[1:8]
        meteorology_columns = data.columns[8:16]
    
        # Sidebar inputs
        selected_pollutant = st.sidebar.selectbox('Select Pollutant', pollutant_columns)
        selected_meteorology = st.sidebar.selectbox('Select Meteorology Data', meteorology_columns)
    
        # Start and end date inputs
        start_date = st.sidebar.date_input('Start Date', min_value=data['Waktu'].min().to_pydatetime().date(), max_value=data['Waktu'].max().to_pydatetime().date(), value=data['Waktu'].min().to_pydatetime().date())
        end_date = st.sidebar.date_input('End Date', min_value=data['Waktu'].min().to_pydatetime().date(), max_value=data['Waktu'].max().to_pydatetime().date(), value=data['Waktu'].min().to_pydatetime().date())
    
        # Hour and minute range inputs
        start_hour = st.sidebar.selectbox('Start Hour', range(24), 0)
        start_minute = st.sidebar.selectbox('Start Minute', range(0, 60, 30), 0, format_func=lambda x: f'{x:02d}')
        end_hour = st.sidebar.selectbox('End Hour', range(24), 23)
        end_minute = st.sidebar.selectbox('End Minute', range(0, 60, 30), 1, format_func=lambda x: f'{x:02d}')
    
        # Create start and end datetime objects
        start_datetime = datetime.combine(start_date, time(start_hour, start_minute))
        end_datetime = datetime.combine(end_date, time(end_hour, end_minute))
    
        # Filter data based on selected date and time range
        filtered_data = data[(data['Waktu'] >= start_datetime) & (data['Waktu'] <= end_datetime)]
    
        # Create line plot for the correlation between selected pollutant and meteorology data using Plotly
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x=filtered_data['Waktu'], y=filtered_data[selected_pollutant], mode='lines', name=selected_pollutant), secondary_y=False)
        fig.add_trace(go.Scatter(x=filtered_data['Waktu'], y=filtered_data[selected_meteorology], mode='lines', name=selected_meteorology), secondary_y=True)
    
        # Update the layout with titles and y-axis labels
        fig.update_layout(
            title=f'Correlation between {selected_pollutant} and {selected_meteorology}',
            xaxis_title='Time',
            yaxis=dict(title=selected_pollutant, side='left'),
            yaxis2=dict(title=selected_meteorology, side='right')
        )
    
        # Display the correlation line plot
        st.plotly_chart(fig)
    
        # Create separate line plot for the selected pollutant data
        fig_pollutant = go.Figure()
        fig_pollutant.add_trace(go.Scatter(x=filtered_data['Waktu'], y=filtered_data[selected_pollutant], mode='lines', name=selected_pollutant))
        fig_pollutant.update_layout(title=f'{selected_pollutant} Trend', xaxis_title='Time', yaxis_title='Concentration')
        st.plotly_chart(fig_pollutant)
    
        # Create separate line plot for the selected meteorology data
        fig_meteorology = go.Figure()
        fig_meteorology.add_trace(go.Scatter(x=filtered_data['Waktu'], y=filtered_data[selected_meteorology], mode='lines', name=selected_meteorology))
        fig_meteorology.update_layout(title=f'{selected_meteorology} Trend', xaxis_title='Time', yaxis_title='Value')
        st.plotly_chart(fig_meteorology)
    
        # Calculate the mean, maximum, and minimum values of the selected pollutant column
        pollutant_mean = filtered_data[selected_pollutant].mean()
        pollutant_max = filtered_data[selected_pollutant].max()
        pollutant_min = filtered_data[selected_pollutant].min()
        
        # Calculate the mean, maximum, and minimum values of the selected meteorology column
        meteorology_mean = filtered_data[selected_meteorology].mean()
        meteorology_max = filtered_data[selected_meteorology].max()
        meteorology_min = filtered_data[selected_meteorology].min()
        
        # Calculate the maximum value and its corresponding date for the selected pollutant
        pollutant_max_value = filtered_data[selected_pollutant].max()
        pollutant_max_date = filtered_data.loc[filtered_data[selected_pollutant] == pollutant_max_value, 'Waktu'].iloc[0]
        
        # Calculate the minimum value and its corresponding date for the selected pollutant
        pollutant_min_value = filtered_data[selected_pollutant].min()
        pollutant_min_date = filtered_data.loc[filtered_data[selected_pollutant] == pollutant_min_value, 'Waktu'].iloc[0]
        
        # Calculate the maximum value and its corresponding date for the selected meteorology data
        meteorology_max_value = filtered_data[selected_meteorology].max()
        meteorology_max_date = filtered_data.loc[filtered_data[selected_meteorology] == meteorology_max_value, 'Waktu'].iloc[0]
        
        # Calculate the minimum value and its corresponding date for the selected meteorology data
        meteorology_min_value = filtered_data[selected_meteorology].min()
        meteorology_min_date = filtered_data.loc[filtered_data[selected_meteorology] == meteorology_min_value, 'Waktu'].iloc[0]
        
        # Display the mean, maximum, and minimum values for the selected pollutant
        st.write("Pollutant:", selected_pollutant)
        st.write("Mean:", pollutant_mean)
        st.write("Maximum:", pollutant_max_value, "Date:", pollutant_max_date)
        st.write("Minimum:", pollutant_min_value, "Date:", pollutant_min_date)
        
        # Display the mean, maximum, and minimum values for the selected meteorology data
        st.write("Meteorology Data:", selected_meteorology)
        st.write("Mean:", meteorology_mean)
        st.write("Maximum:", meteorology_max_value, "Date:", meteorology_max_date)
        st.write("Minimum:", meteorology_min_value, "Date:", meteorology_min_date)
        
        # Calculate the correlation coefficient between the selected pollutant and meteorology data
        correlation_coefficient = filtered_data[[selected_pollutant, selected_meteorology]].corr().iloc[0, 1]
        
        # Display the correlation coefficient
        st.write("Correlation Coefficient:", correlation_coefficient)

    


        st.header('Data Analysis')

        # Date range selection
        start_date = st.date_input('Start Date', value=data['Waktu'].min().to_pydatetime().date())
        end_date = st.date_input('End Date', value=data['Waktu'].max().to_pydatetime().date())
    
        # Convert start_date and end_date to datetime objects
        start_datetime = pd.to_datetime(start_date)
        end_datetime = pd.to_datetime(end_date)
    
        # Filter data based on date range
        filtered_data = data[(data['Waktu'] >= start_datetime) & (data['Waktu'] <= end_datetime)]
    
        # Summary statistics
        st.subheader('Summary Statistics')
    
        # Calculate mean, median, and standard deviation for each pollutant
        summary_stats = filtered_data.describe()[1:4]
    
        # Display summary statistics in a table
        st.table(summary_stats)
    
        # Trend analysis
        st.subheader('Trend Analysis')
    
        # Line plot for each pollutant
        fig, ax = plt.subplots(figsize=(10, 6))
    
        # Define the range for each particle
        particle_ranges = {
            'PM10': (0, 500),
            'PM2p5': (0, 500),
            'SO2': (0, 1000),
            'CO': (0, 50000),
            'O3': (0, 1000),
            'NO2': (0, 3000),
            'HC': (0, 1000)
        }
    
        # Plot the trends for each pollutant
        for pollutant in filtered_data.columns[1:8]:
            ax.plot(filtered_data['Waktu'], filtered_data[pollutant], label=pollutant)
            
            # Set the y-axis range for each pollutant
            ax.set_ylim(particle_ranges[pollutant])
    
        # Set labels and title
        ax.set_xlabel('Time')
        ax.set_ylabel('Concentration')
        ax.set_title('Trend Analysis of Pollutants')
    
        # Add legend
        ax.legend()
    
        # Display the plot in the app
        st.pyplot(fig)
    
        # Additional data analysis and visualizations can be added here
    
        # Compute the correlation matrix
        correlation_matrix = filtered_data.corr()
    
        st.subheader('Heatmap Analysis')
        # Create a heatmap using seaborn
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
    
        # Set the title and labels
        plt.title('Correlation Matrix')
        plt.xlabel('Variables')
        plt.ylabel('Variables')
    
        # Display the plot in Streamlit app
        st.pyplot(fig)
    
        # Additional data analysis and visualizations can be added here

    
elif option == 'Download Resources':
        # Load data from CSV file
        data = pd.read_csv('19-23 ISPU Kota Yogyakarta.csv')
        data['Waktu'] = pd.to_datetime(data['Waktu'])
    
        # Sidebar options
        selected_columns = st.sidebar.multiselect('Select Columns', data.columns, key="select_columns_ipu")
    
        # Get the minimum and maximum dates from the data
        min_date = data['Waktu'].min().date()
        max_date = data['Waktu'].max().date()
    
        # Get the selected start and end dates from the user
        start_date = st.sidebar.date_input('Start Date', min_value=min_date, max_value=max_date, value=min_date, key="start_date_ipu")
        end_date = st.sidebar.date_input('End Date', min_value=min_date, max_value=max_date, value=max_date, key="end_date_ipu")
    
        # Filter data based on selected time range
        filtered_data = data[(data['Waktu'].dt.date >= start_date) & (data['Waktu'].dt.date <= end_date)]
    
        # Filter data based on selected columns
        filtered_data = filtered_data[selected_columns]
    
        # Display filtered DataFrame
        st.write(filtered_data)

        # Download CSV file
        if st.button('Download CSV'):
            csv_data = filtered_data.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv_data,
                file_name="filtered_data.csv",
                mime="text/csv")




    










