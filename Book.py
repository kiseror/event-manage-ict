from tkinter import *
from GenerateNewCode import random_id  # Importing the function to generate a random ID
from DataBase import TicketDetails, EventDetails, BookTicket  # Importing functions related to ticket and event details
from Message import show_message  # Importing a function to display messages

# Function to handle booking of tickets
#This function creates a GUI window to input customer details and book tickets for an event.
#It uses functions from the GenerateNewCode, DataBase, and Message modules.
def Book(event_id=None):
    ticket_ids = TicketDetails()[1]  # Fetch ticket IDs from the database
    event_names_list = EventDetails()[0]  # Fetch event names from the database

    top1 = Tk()  # Create a new Tkinter window for booking
    top1.resizable(False, False)  # Lock the window size to prevent resizing
    top1.geometry('300x280')  # Set the window size
    top1.title('Book ticket')  # Set the window title

    customer_name = StringVar(top1)  # Variable to store customer name
    ticket_id = StringVar(top1)  # Variable to store ticket ID
    event_name = StringVar(top1)  # Variable to store event name

    event_name.set('Select event')  # Set default value for event selection

    while True:
        new_ticket_id = random_id()  # Generate a random ticket ID
        if new_ticket_id not in ticket_ids:  # Check if the ID is unique
            ticket_id.set(new_ticket_id)  # Set the generated ID
            break  # Exit the loop if a unique ID is generated
        continue  # Continue generating IDs until a unique one is found

# This code functions to handle the booking process when the 'Confirm' button is clicked.
    def BookNow():
        if len(customer_name.get()) < 5:  # Check if customer name is valid
            show_message('Error', 'Enter valid details')  # Display error message
            return  # Exit the function if details are invalid
        
        # Book the ticket using BookTicket function from the DataBase module
        booking_status = BookTicket(customer_name.get(), ticket_id.get(), event_name.get())
        if booking_status == 'Success':  # Check if booking is successful
            show_message('Success', 'Booking successful')  # Display success message
            top1.destroy()  # Close the booking window
            return  # Exit the function after successful booking
        else:
            show_message('Error', booking_status)  # Display error message if booking fails

    # GUI elements for customer details and booking confirmation
    Label(top1, text='Enter details', font=('Arial Black', 14)).grid(row=0, column=0, padx=10, pady=10, columnspan=2)
    Label(top1, text='Name', font=('Calibri', 12)).grid(row=1, column=0, padx=10, pady=10, sticky='w')
    Entry(top1, textvariable=customer_name).grid(row=1, column=1)
    Label(top1, text='Ticket Id', font=('Calibri', 12)).grid(row=2, column=0, padx=10, pady=10, sticky='w')
    Entry(top1, textvariable=ticket_id, state='disabled').grid(row=2, column=1)
    Label(top1, text='Event', font=('Calibri', 12)).grid(row=3, column=0, padx=10, sticky='w', pady=10)
    OptionMenu(top1, event_name, *event_names_list).grid(row=3, column=1)
    Button(top1, text='Confirm', bg='green', fg='white', font=('Tahoma', 17), width=9, command=lambda: BookNow()).grid(row=4, column=1, pady=10)

    top1.mainloop()  # Start the GUI event loop to handle user interactions
