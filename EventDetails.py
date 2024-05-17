from tkinter import *
from tkinter import messagebox
from DataBase import EventDetails, DeleteEvent
from Book import Book

def view_event_details(event_id):
    top_event_details = Tk()  # Create a new window for each event detail
    top_event_details.resizable(False, False)  # Lock the window size
    top_event_details.geometry('350x350')  # Add margin of 5px on each side
    top_event_details.title('Event Details')
    event_details_frame = Frame(top_event_details)
    event_details_frame.pack(padx=5, pady=5)  # Margin around the frame

    # Fetch event details from the database
    event_details = EventDetails()[5]
    for event in event_details:
        if event_id == event[1]:
            show_details(event, event_details_frame, top_event_details)
            break

def show_details(event, top, top_event_details):
    Label(top, text=f'Event Name: {event[0]}', font=("Calibri", 11)).pack()
    Label(top, text=f'Event ID: {event[1]}', font=("Calibri", 11)).pack()
    Label(top, text=f'Event Date: {event[2]}', font=("Calibri", 11)).pack()
    Label(top, text=f'Event Time: {event[3]}', font=("Calibri", 11)).pack()
    Label(top, text=f'Event Duration: {event[4]}', font=("Calibri", 11)).pack()

    # Check if the event tuple includes the description field and wrap the text if necessary
    if len(event) > 5:
        description = event[5]
        wrap_length = 40  # Adjust the wrap length as needed
        if len(description) > wrap_length:
            wrapped_description = "\n".join([description[i:i+wrap_length] for i in range(0, len(description), wrap_length)])
            Label(top, text=f'What is this?\n{wrapped_description}', font=("Calibri", 14)).pack(padx=10, pady=10)
        else:
            Label(top, text=f'What is this?\n{description}', font=("Calibri", 14)).pack(padx=10, pady=10)
    
    Button(top, text='Book Now!', font=('Tahoma', 14), command=lambda: Book(event[1])).pack(pady=(10, 0))  # Margin above
    Button(top, text='Clear Event', font=('Tahoma', 14), bg='red', fg='white', command=lambda: clear_event(event[1], top_event_details)).pack(pady=(10, 0))  # Margin above

def clear_event(event_id, top):
    result = messagebox.askyesno('Confirm', 'Are you sure you want to clear this event?')
    if result:
        status = DeleteEvent(event_id)
        if status == 'Success':
            messagebox.showinfo('Success', 'Event cleared successfully')
            top.destroy()
        else:
            messagebox.showerror('Error', status)

