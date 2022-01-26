import database
from tkinter import  ttk
import fetchval
import tkinter as tk
root = tk.Tk()
root.geometry("650x650")
root.resizable(False, False)
root.iconbitmap("icon/weathericon.ico")
root.title(" Data visualization ")
# creating frame

title_frame = tk.Frame(root,
                       padx=95, pady=25, width=40, height=65)
first_frame = tk.Frame(root,
                       padx=95, pady=25, width=40, height=65)
second_frame = tk.Frame(root,
                        padx=95, pady=25, width=40, height=65)
third_frame = tk.Frame(root,
                       padx=95, pady=25, width=40, height=65)
# frame postion in root
title_frame.grid(row=0, columnspan=5)
first_frame.grid(row=1, columnspan=5)
second_frame.grid(row=2, columnspan=5)
third_frame.grid(row=3, columnspan=5)

# creating label for title frame
Title_label = tk.Label(title_frame, background="blue",
                       text="Data Visualization", font=('Aerial 22 bold'), padx=85, pady=5).grid(row=2, column=0)

# date selection lablel
date_label = tk.Label(first_frame, text="Select Date :", font=(
    'Aerial 22 bold'), padx=25, pady=10).grid(row=0, column=1)
date_label1 = tk.Label(second_frame, text="Select Date :", font=(
    'Aerial 22 bold'), padx=25, pady=10).grid(row=0, column=1)
# location label
location_label = tk.Label(third_frame, text="Select Location :", font=(
    'Aerial 22 bold'), padx=25, pady=10).grid(row=0, column=1)

# fetching data from database to put in combox box
conn = database.connection()

sql_query = "SELECT distinct date_list FROM fewing_view_database.hourly_forecast ;"
get_date_val = database.select_from_table(conn, sql_query)
date_list = []
for val in get_date_val:
    date_list.append((str(val).strip("(',')")))


# create combox
# combox for date
selected_date = tk.StringVar()
date_cb = ttk.Combobox(first_frame, width=25, textvariable=selected_date,
                       values=date_list, font=("TkDefaultFont", 14))
date_cb.grid(row=0, column=2)
date_cb.current(0)


# combox for bar
selected_date1 = tk.StringVar()
date_cb1 = ttk.Combobox(
    second_frame, textvariable=selected_date1, values=date_list, font=("TkDefaultFont", 14))
date_cb1.grid(row=0, column=2)
date_cb1.current(0)
# date_cb1.set(date_list[0])


# fetching location data from database
sql_query = "SELECT distinct location_name FROM fewing_view_database.hourly_forecast ;"
get_date_val = database.select_from_table(conn, sql_query)
location_list = []
for val in get_date_val:
    location_list.append((str(val).strip("(',')")))


# combox for location
selected_location = tk.StringVar()
location_cb = ttk.Combobox(third_frame, textvariable=selected_location, values=location_list, font=(
    "TkDefaultFont", 14))
location_cb.grid(row=0, column=2)
location_cb.current(0)

#buttons and their functons

scatter_plt_btn = tk.Button(first_frame, text="Scatter Plot ", font=(
    'Aerial 22 bold'), padx=25, pady=5,command=lambda:fetchval.scatter_plt(date_cb.get()))
scatter_plt_btn.grid(row=2, column=1, columnspan=3)
bar_plt_btn = tk.Button(second_frame, text="Bar graph", font=(
    'Aerial 22 bold'), padx=25, pady=5,command=lambda: fetchval.bar_plt(date_cb1.get()))
bar_plt_btn.grid(row=2, column=1, columnspan=3)

line_plt_btn = tk.Button(third_frame, text="Line Plot ", font=(
    'Aerial 22 bold'), padx=25, pady=5,command=lambda: fetchval.line_plot(location_cb.get()))
line_plt_btn.grid(row=2, column=1, columnspan=3)

if __name__ == "__main__":
    root.mainloop()
