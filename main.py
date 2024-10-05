import tkinter as tk
from send_logs import send_app_logs, send_system_logs, send_setup_logs

def send_logs():
    send_system_logs(system_label_var, system_label)
    send_app_logs(application_label_var, application_label)
    send_setup_logs(setup_label_var, setup_label)


root = tk.Tk()
root.geometry("300x300")
root.title("Event Scanner")
root.configure(background="black")

#Creating Title
title = tk.Label(root, text="Event Scanner", font=("Roboto", 18,'bold'), bg="black", fg="White")
title.pack(padx=20, pady=15)

#Creating System Health
system_health_frame = tk.Frame(root, bg="black")

system_health_frame.columnconfigure(0, weight=1)
system_health_frame.columnconfigure(0, weight=2)


system_label = tk.Label(system_health_frame, text="System:", font=("Roboto", 16), bg="black", fg="white")
application_label = tk.Label(system_health_frame, text="Application:", font=("Roboto", 16), bg="black", fg="white")
setup_label = tk.Label(system_health_frame, text="Setup:", font=("Roboto", 16), bg="black", fg="white")

#StringVars
system_label_var = tk.StringVar()
application_label_var = tk.StringVar()
setup_label_var = tk.StringVar()

system_label_var.set("Unchecked")
application_label_var.set("Unchecked")
setup_label_var.set("Unchecked")

system_is_good =  tk.Label(system_health_frame, textvariable=system_label_var, font=("Roboto", 16), bg="black", fg="red")
application_is_good =  tk.Label(system_health_frame, textvariable=application_label_var, font=("Roboto", 16), bg="black", fg="red")
setup_is_good =  tk.Label(system_health_frame, textvariable=setup_label_var, font=("Roboto", 16), bg="black", fg="red")

system_label.grid(column=0, row=0)
application_label.grid(column=0, row=1)
setup_label.grid(column=0, row=2)

system_is_good.grid(column=1, row=0)
application_is_good.grid(column=1, row=1)
setup_is_good.grid(column=1, row=2)

system_health_frame.pack(padx=20, pady=15)

#Create ReCheck Button
button = tk.Button(text="Re-Check", font=('Roboto', 12, 'bold'), command=send_logs)
button.pack(padx=20, pady=15)

root.mainloop()

