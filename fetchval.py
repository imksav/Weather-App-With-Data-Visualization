import database
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
conn = database.connection()
root = tk.Tk()
#creating dataframe using sql command
sql_query = pd.read_sql_query('''
SELECT * FROM hourly_forecast''', conn)
hourly_df = pd.DataFrame(sql_query, columns=['location_name', 'date_list', 'hourly_time', 'hourly_temperature',
                                             'hourly_temperature_condition', 'hourly_humidity', 'hourly_cloud', 'hourly_wind_kph', 'is_day'])
date_list = hourly_df['date_list']
location_list = hourly_df['location_name']
hourly_list = hourly_df['hourly_time']
hourly_temp = pd.to_numeric(hourly_df['hourly_temperature'])
hourly_humidity = pd.to_numeric(hourly_df['hourly_humidity'])
root.withdraw()
#scatter plot


def scatter_plt(para_date):
    new_window = tk.Toplevel(root)
    new_window.title("Scatter plot")
    for date in date_list:
       if date == para_date:
           date_group_df = hourly_df.groupby('date_list')
           hourly_humidity1 = date_group_df.get_group(date)['hourly_humidity']
           location_list1 = date_group_df.get_group(date)['location_name']
           figure1 = plt.Figure(figsize=(6, 5), dpi=200)
           ax1 = figure1.add_subplot(111)
           ax1.scatter(location_list1, hourly_humidity1,
                       c='green', vmin=0, vmax=100)
           bar1 = FigureCanvasTkAgg(figure1, new_window)
           bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
           ax1.legend(['Humidity'])
           ax1.set_xlabel("Location")
           ax1.set_title(f'Date :{date} \nLocation vs Humidity')
           return (location_list1, hourly_humidity1)
           break


def bar_plt(para_date):
    new_window = tk.Toplevel(root)
    new_window.title("Bar Graph")
    for date in date_list:
        if date == para_date:
           date_group_df = hourly_df.groupby('date_list')
           hourly_humidity1 = date_group_df.get_group(
               date)['hourly_temperature']
           location_list1 = date_group_df.get_group(date)['location_name']
           hourly_humidity1 = pd.to_numeric(hourly_humidity1)
           figure1 = plt.Figure(figsize=(6, 5), dpi=100)
           plot1 = figure1.add_subplot(111)
           plot1.bar(location_list1, hourly_humidity1,
                     color="Maroon", width=0.4)
           plot1.legend(['Temperature'])
           plot1.set_xlabel("Location")
           plot1.set_title(f'Date :{date} \nLocation vs Temperature')
           bar1 = FigureCanvasTkAgg(figure1, new_window)
           bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
           break


def line_plot(para_date):
    new_window = tk.Toplevel(root)
    new_window.title("line Plot")
    for date in location_list:

        if date == para_date:
           date_group_df = hourly_df.groupby('location_name')
           hourly_humidity1 = pd.to_numeric(
               date_group_df.get_group(date)['hourly_humidity'])
           temp_list = pd.to_numeric(date_group_df.get_group(date)[
                                     'hourly_temperature'])
           figure1 = plt.Figure(figsize=(6, 5), dpi=200)
           ax1 = figure1.add_subplot(111)
           ax1.plot(temp_list)
           ax1.plot(hourly_humidity1)
           bar1 = FigureCanvasTkAgg(figure1, new_window)
           bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
           ax1.legend(['Temprature', 'Humidity'])
           ax1.set_xlabel("Location based temperature and humidity ")
           break


if __name__ == "__main__":
    bar_plt("")
    scatter_plt("")
    line_plot("")
    root.mainloop()
