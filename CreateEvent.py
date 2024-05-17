from tkinter import *
from GenerateNewCode import random_id  # Importing the function to generate a random ID
from DataBase import EventDetails, CreateNewEvent  # Importing functions related to event details
from Message import show_message  # Importing a function to display messages
from tkcalendar import DateEntry  # Importing DateEntry widget from tkcalendar
from datetime import date  # Importing date module to get current date

def CreateEvent():
    """
    Function to create a new event by inputting event details through a GUI.

    This function creates a GUI window for entering event details such as name, date, time, duration, and description.
    It uses functions from the GenerateNewCode, DataBase, Message, and tkcalendar modules.
    """
    event_ids = EventDetails()[1]  # Fetch event IDs from the database
    
    top2 = Tk()  # Create a new Tkinter window for creating an event
    top2.resizable(False, False)  # Lock the window size to prevent resizing
    top2.geometry('500x500')  # Set the window size
    top2.title('Create new Event')  # Set the window title
    
    event_name = StringVar(top2)  # Variable to store event name
    event_id = StringVar(top2)  # Variable to store event ID
    event_date = StringVar(top2)  # Variable to store event date (initialized with today's date)
    event_date.set(date.today())
    event_time = StringVar(top2)  # Variable to store event time
    event_duration = StringVar(top2)  # Variable to store event duration
    event_description = StringVar()  # Variable to store event description
    
    while True:
        new_event_id = random_id()  # Generate a random event ID
        if new_event_id not in event_ids:  # Check if the ID is unique
            event_id.set(new_event_id)  # Set the generated ID
            break  # Exit the loop if a unique ID is generated
        continue  # Continue generating IDs until a unique one is found

    def CreateNow():
        """
        Function to handle the event creation process when the 'Submit' button is clicked.
        """
        if len(event_name.get()) < 5:  # Check if event name is valid
            show_message('Error', 'Enter valid details')  # Display error message
            return
        
        # Retrieve text from description_text widget
        description_text_content = description_text.get("1.0", END)
        
        # Create the event using CreateNewEvent function from the DataBase module
        event_status = CreateNewEvent(
            event_name.get(), event_id.get(), event_date.get(), 
            event_time.get(), event_duration.get(), description_text_content  # Pass the description content here
        )
        if event_status == 'Success':  # Check if event creation is successful
            show_message('Success', 'Event created successfully')  # Display success message
            top2.destroy()  # Close the window on successful event creation
        else:
            show_message('Error', event_status)  # Display error message if event creation fails
    
    # GUI elements for entering event details
    Label(top2, text='Enter details', font=('Arial Black', 14)).grid(row=0, column=0, padx=10, pady=10, columnspan=2)
    Label(top2, text='Event Name', font=('Calibri', 12)).grid(row=1, column=0, padx=10, pady=10, sticky='w')
    Entry(top2, textvariable=event_name).grid(row=1, column=1)
    Label(top2, text='Event Id', font=('Calibri', 12)).grid(row=2, column=0, padx=10, pady=10, sticky='w')
    Entry(top2, textvariable=event_id, state='disabled').grid(row=2, column=1)
    Label(top2, text='Event Date', font=('Calibri', 12)).grid(row=3, column=0, padx=10, sticky='w', pady=10)
    DateEntry(top2, selectmode='day', year=2023, month=1, day=25, textvariable=event_date).grid(row=3, column=1)
    Label(top2, text='Event Time(24hrs)', font=('Calibri', 12)).grid(row=4, column=0, padx=10, pady=10, sticky='w')
    Entry(top2, textvariable=event_time).grid(row=4, column=1)
    Label(top2, text='Event Duration', font=('Calibri', 12)).grid(row=5, column=0, padx=10, pady=10, sticky='w')
    Entry(top2, textvariable=event_duration).grid(row=5, column=1)
    Label(top2, text='Description', font=('Calibri', 12)).grid(row=6, column=0, padx=10, pady=10, sticky='w')
    description_text = Text(top2, height=4, width=30, wrap=WORD, padx=5, pady=5)  # Text widget for event description
    description_text.grid(row=6, column=1)
    
    Button(top2, text='Submit', bg='green', fg='white', font=('Tahoama', 17), width=9, command=CreateNow).grid(row=7, column=0, pady=10, columnspan=2)
    
    top2.mainloop()  # Start the GUI event loop to handle user interactions
