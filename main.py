#libraries and modules of main
from tkinter import *
from tkinter import ttk
from DataBase import EventDetails, DeleteEvent
from ViewTickets import ViewTickets
from EventDetails import view_event_details
from Message import show_message
from CreateEvent import CreateEvent
from CancelTicket import CancelTicket

# This function is used to delete events
def delete_event(event_id):
     # This will call the DeleteEvent function from DataBase module to delete the event
    status = DeleteEvent(event_id)
    # This checks if deletion was successful
    if status == 'Success':
        # This refreshes the event table if it is successful 
        refresh_table()
    else:
        # This refreshes the event table if it is successful
        show_message('Error', status)

# This function is for refreshing the event table
def refresh_table():
    for row in event_tree.get_children():
        event_tree.delete(row)
    event_details = EventDetails()[5]
    for event in event_details:
        event_tree.insert("", "end", values=event)
    
    # Configure the scrollbar's view
    event_tree.update_idletasks()  # Update the widget to get accurate size information
    scrollbar.config(command=event_tree.yview)  # Configure the scrollbar's command option

# Function to handle double-click on an event and view event details
def on_event_double_click(event):
    item = event_tree.selection()[0]
    event_id = event_tree.item(item, "values")[1]
    view_event_details(event_id)

# Creates the main window
top = Tk()
top.geometry('900x600')
top.title('Event Management Application')

# Configures grid layout to make the table resize with the window
top.grid_columnconfigure(0, weight=1)
top.grid_rowconfigure(4, weight=1)

# Creates a custom style for the Treeview widget
style = ttk.Style()
style.configure("Treeview.Heading", padding=(10, 5))
style.configure("Treeview", rowheight=25)

# Creates the event table using Treeview widget
event_tree = ttk.Treeview(top, columns=("Event Name", "Event ID", "Event Date", "Event Time", "Event Duration"), show="headings")
event_tree.heading("Event Name", text="Event Name")
event_tree.heading("Event ID", text="Event ID")
event_tree.heading("Event Date", text="Event Date")
event_tree.heading("Event Time", text="Event Time")
event_tree.heading("Event Duration", text="Event Duration")

# Adds a vertical scrollbar
scrollbar = Scrollbar(top, orient=VERTICAL)
scrollbar.grid(row=1, column=2, sticky='ns')

# Configures Treeview widget to work with the scrollbar
event_tree.configure(yscrollcommand=scrollbar.set)

# Fetches initial event details and populate the event table
event_details = EventDetails()[5]
for event in event_details:
    event_tree.insert("", "end", values=event)

# Displays the event table on the main window
event_tree.grid(row=1, column=0, columnspan=2, sticky='nsew')

# Binds event double-click function to the event table
event_tree.bind("<Double-1>", on_event_double_click)

# Adds buttons for different functionalities
Button(top, text='View Tickets', bg='black', fg='white', width=12, font=('Tahoma', 18), command=ViewTickets).grid(row=2, column=0, pady=10)
Button(top, text='Cancel Ticket', bg='red', fg='white', width=12, font=('Tahoma', 18), command=CancelTicket).grid(row=3, column=0)
Button(top, text='Quit App', bg='red', fg='white', width=12, font=('Tahoma', 18), command=top.destroy).grid(row=4, column=1)
Button(top, text='Refresh Event Table', bg='#00008B', fg='white', width=18, font=('Tahoma', 12), command=refresh_table).grid(row=2, column=1)
Button(top, text='Create Event', bg='black', fg='white', width=12, font=('Tahoma', 18), command=CreateEvent).grid(row=0, column=1, pady=10)

# Adds a label for user guidance
Label(top, text='Select an Event', font=('Arial Black', 24)).grid(row=0, column=0, columnspan=2)

# Ensures the treeview resizes with the window
def resize_treeview(event):
    event_tree.column("Event Name", width=event.width // 5)
    event_tree.column("Event ID", width=event.width // 5)
    event_tree.column("Event Date", width=event.width // 5)
    event_tree.column("Event Time", width=event.width // 5)
    event_tree.column("Event Duration", width=event.width // 5)

top.bind('<Configure>', resize_treeview)

top.mainloop()