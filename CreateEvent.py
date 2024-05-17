from tkinter import *
from GenerateNewCode import random_id
from DataBase import EventDetails, CreateNewEvent
from Message import show_message
from tkcalendar import DateEntry
from datetime import date

def CreateEvent():
    event_ids = EventDetails()[1]
    
    top2 = Tk()
    top2.resizable(False, False)
    top2.geometry('500x500')  # Increased height to accommodate the larger description box
    top2.title('Create new Event')
    
    event_name = StringVar(top2)
    event_id = StringVar(top2)
    event_date = StringVar(top2)
    event_date.set(date.today())
    event_time = StringVar(top2)
    event_duration = StringVar(top2)
    event_description = StringVar()  # Removed top2 from here
    
    while True:
        new_event_id = random_id()
        if new_event_id not in event_ids:
            event_id.set(new_event_id)
            break

    def CreateNow():
        if len(event_name.get()) < 5:
            show_message('Error', 'Enter valid details')
            return
        
        # Retrieve text from description_text widget
        description_text_content = description_text.get("1.0", END)
        
        event_status = CreateNewEvent(
            event_name.get(), event_id.get(), event_date.get(), 
            event_time.get(), event_duration.get(), description_text_content  # Pass the description content here
        )
        if event_status == 'Success':
            show_message('Success', 'Event created successfully')
            top2.destroy()  # Close the window on successful event creation
        else:
            show_message('Error', event_status)
    
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
    description_text = Text(top2, height=4, width=30, wrap=WORD, padx=5, pady=5)
    description_text.grid(row=6, column=1)
    
    Button(top2, text='Submit', bg='green', fg='white', font=('Tahoama', 17), width=9, command=CreateNow).grid(row=7, column=0, pady=10, columnspan=2)
    
    top2.mainloop()
