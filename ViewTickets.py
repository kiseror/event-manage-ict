from tkinter import *
from tkinter import ttk
from DataBase import TicketDetails, EventDetails

def ViewTickets():
    top4 = Tk()
    top4.geometry('500x300')
    top4.title('View tickets')
    
    event_names_list = EventDetails()[0]
    
    selected_event = StringVar(top4)
    selected_event.set('Select event')
    
    ticket_data = TicketDetails()
    
    # Function to update the ticket table based on the selected event
    def ShowTickets():
        event_name = selected_event.get()
        
        # Clear existing items in the table
        for row in ticket_tree.get_children():
            ticket_tree.delete(row)
        
        # Populate the ticket table with tickets for the selected event
        for ticket in ticket_data[7]:
            if ticket[2] == event_name:
                ticket_tree.insert("", "end", values=(ticket[0], ticket[1]))  # Customer Name, Ticket ID
    
    Label(top4, text='Select Event:', font=('Arial Black', 16)).grid(row=0, column=0, padx=10, pady=10, sticky='w')
    OptionMenu(top4, selected_event, *event_names_list).grid(row=0, column=1)
    
    Button(top4, text='Submit', command=ShowTickets, bg='green', fg='white', font=('Arial', 12)).grid(row=0, column=2, padx=10)
    
    # Create the ticket table using Treeview
    ticket_tree = ttk.Treeview(top4, columns=("Customer Name", "Ticket ID"), show="headings")
    ticket_tree.heading("Customer Name", text="Customer Name")
    ticket_tree.heading("Ticket ID", text="Ticket ID")
    
    ticket_tree.grid(row=1, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)
    
    # Configure scrollbar
    scrollbar = Scrollbar(top4, orient=VERTICAL, command=ticket_tree.yview)
    ticket_tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=3, sticky='ns')
    
    top4.mainloop()
