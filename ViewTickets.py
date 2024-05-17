# Imports necessary modules
from tkinter import *
from tkinter import ttk
from DataBase import TicketDetails, EventDetails

def ViewTickets():
    # Creates the main window
    top4 = Tk()
    top4.geometry('500x300')
    top4.title('View tickets')
    
    # Fetches event names from the database
    event_names_list = EventDetails()[0]
    
    # Creates a variable to store the selected event
    selected_event = StringVar(top4)
    selected_event.set('Select event')  # Default value
    
    # Fetches ticket details from the database
    ticket_data = TicketDetails()
    
    # Functions to update the ticket table based on the selected event
    def ShowTickets():
        event_name = selected_event.get()  # Get the selected event name
        
        # Clears existing items in the ticket table
        for row in ticket_tree.get_children():
            ticket_tree.delete(row)
        
        # Populates the ticket table with tickets for the selected event
        for ticket in ticket_data[7]:
            if ticket[2] == event_name:  # Check if the ticket's event matches the selected event
                ticket_tree.insert("", "end", values=(ticket[0], ticket[1]))  # Insert Customer Name, Ticket ID
    
    # Label and OptionMenu for selecting the event
    Label(top4, text='Select Event:', font=('Arial Black', 16)).grid(row=0, column=0, padx=10, pady=10, sticky='w')
    OptionMenu(top4, selected_event, *event_names_list).grid(row=0, column=1)
    
    # Button to submit and update the ticket table
    Button(top4, text='Submit', command=ShowTickets, bg='green', fg='white', font=('Arial', 12)).grid(row=0, column=2, padx=10)
    
    # Creates the ticket table using Treeview
    ticket_tree = ttk.Treeview(top4, columns=("Customer Name", "Ticket ID"), show="headings")
    ticket_tree.heading("Customer Name", text="Customer Name")
    ticket_tree.heading("Ticket ID", text="Ticket ID")
    
    # Grid and configure scrollbar for the ticket table
    ticket_tree.grid(row=1, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)
    scrollbar = Scrollbar(top4, orient=VERTICAL, command=ticket_tree.yview)
    ticket_tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=3, sticky='ns')
    
    # Starts the main event loop
    top4.mainloop()

