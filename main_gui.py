import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import database
# function...................
# contants labeling
def ui_label():
     # win.geometry("650x650+500+100")
     win.resizable(0,0)
     
     win.title("Weather App With Data Visualization")
     # date = tkinter.Label(win, text="Date:", font=('Times 12 bold')).place(relx=0.08, rely=0.1, anchor='ne')
     # city = tkinter.Label(win, text="City/Town:", font=('Times 12 bold')).place(relx=0.35, rely=0.1, anchor='ne')
     # city = tkinter.Label(win, text="Temperature (C):", font=('Times 12 bold')).place(relx=0.68, rely=0.1, anchor='ne')
     
# refresh button function
def on_click(name):
     print("on click printing")
     # name = name_Tf.get()
     print(name)
     conn = database.connection()
     cursor = conn.cursor()
     sql_select_query = """SELECT daily_forecast.location_name, date_list, sunrise_time, sunset_time, moonrise_time, moonset_time, general_info.current_location_temperature FROM daily_forecast INNER JOIN general_info WHERE daily_forecast.location_name = general_info.location_name AND daily_forecast.location_name=%s"""
     cursor.execute(sql_select_query, (name,))
     # sql_select_query = """select * from general_info where location_name = %s"""
     # cursor.execute(sql_select_query, (name,))
     
     rows = cursor.fetchall()
     # rows = database.select_from_table(conn, sql_query)
     for row in rows:
          print(row)
          tree.insert("", tk.END, values=row)
     # for item in all_data:
     #      city = item[1]
     #      lat = item[2]
     #      lon = item[3]
     #      temp = item[4]
     #      img = item[5]
     #      date = tkinter.Label(win,text ='2022-01-26', font=('Times 12 bold underline')).place(relx=0.20, rely=0.1, anchor='ne')
     #      city = tkinter.Label(win,text = city, font = ('Times 12 bold underline')).place(relx=0.48, rely=0.1, anchor='ne')
     #      temperature = tkinter.Label(win, text=temp+ 'degree Celsius', font = ('Times 12 bold underline')).place(relx=0.91, rely=0.1, anchor='ne')
     
     
# pure gui
win = tk.Tk()
# ui_label()
# win.resizable(0,0)
win.title("Weather App With Data Visualization")
def welcomeMessage():
     name = name_Tf.get()
     on_click(name)
def clear():
     for item in tree.get_children():
          tree.delete(item)
Label(win, text="Enter City Name").pack()
name_Tf = Entry(win)
name_Tf.pack()
search_btn = tk.Button(win, text="Search", command = welcomeMessage)
search_btn.pack(pady=20, side = TOP)
clear_btn = tk.Button(win, text="Clear", command = clear)
clear_btn.pack(pady=20, side = TOP)
# Label("City Name", text="").grid()
# table design

tree = ttk.Treeview(win, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')
tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="City Name")
tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="Date")
tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="Sunrise")
tree.column("#4", anchor=tk.CENTER)
tree.heading("#4", text="Sunset")
tree.column("#5", anchor=tk.CENTER)
tree.heading("#5", text="Moonrise")
tree.column("#6", anchor=tk.CENTER)
tree.heading("#6", text="Moonset")
tree.column("#7", anchor=tk.CENTER)
tree.heading("#7", text="Temperature (C)")
tree.pack()


# refreshing button
# Label(win, text='Student_Name').grid(row=0)
# o1 = Entry(win)
# o1.grid(row=0, column=1)

if __name__ == "__main__":
     win.mainloop()
