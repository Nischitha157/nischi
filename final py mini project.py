import tkinter as tk
from tkinter import messagebox

# Initialize variables
today_movie = "DEVIL"
total_tickets = 100
booked_tickets = []

# Functions
def view_movie_info():
    info_text = f"""
    Today's Movie: {today_movie}
    Total Seats: {total_tickets}
    Available Seats: {total_tickets - len(booked_tickets)}
    Show Timings:
    - Morning Show: 10:00 AM - 1:00 PM
    - Evening Show: 7:00 PM - 10:00 PM
    """
    messagebox.showinfo("Movie Information", info_text)

def book_ticket():
    name = name_entry.get().strip()
    show = show_var.get()
    seat_number = seat_entry.get().strip()

    if not name or not seat_number:
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    try:
        seat_number = int(seat_number)
        if seat_number < 1 or seat_number > total_tickets:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Invalid seat number. Choose between 1 and 100.")
        return

    if any(ticket["seat_number"] == seat_number for ticket in booked_tickets):
        messagebox.showerror("Error", f"Seat {seat_number} is already booked.")
        return

    # Book ticket
    ticket = {
        "name": name,
        "show": "Morning Show" if show == "morning" else "Evening Show",
        "seat_number": seat_number,
    }
    booked_tickets.append(ticket)
    messagebox.showinfo("Success", f"Ticket booked for {name} at Seat {seat_number}.")
    update_booking_list()
    name_entry.delete(0, tk.END)
    seat_entry.delete(0, tk.END)

def cancel_booking():
    seat_number = seat_entry.get().strip()

    try:
        seat_number = int(seat_number)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid seat number to cancel.")
        return

    for ticket in booked_tickets:
        if ticket["seat_number"] == seat_number:
            booked_tickets.remove(ticket)
            messagebox.showinfo("Success", f"Booking for Seat {seat_number} canceled.")
            update_booking_list()
            return
    
    messagebox.showerror("Error", f"No booking found for Seat {seat_number}.")

def update_booking_list():
    booking_list.delete(0, tk.END)
    for ticket in booked_tickets:
        booking_list.insert(
            tk.END,
            f"Name: {ticket['name']}, Show: {ticket['show']}, Seat: {ticket['seat_number']}",
        )

# GUI Setup
root = tk.Tk()
root.title("Movie Ticket Booking System")
root.geometry("600x500")
root.resizable(False, False)

# Widgets
title_label = tk.Label(root, text="Movie Ticket Booking System", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

movie_info_button = tk.Button(root, text="View Movie Info", command=view_movie_info, bg="blue", fg="white")
movie_info_button.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

name_label = tk.Label(frame, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

show_label = tk.Label(frame, text="Show:")
show_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
show_var = tk.StringVar(value="morning")
show_dropdown = tk.OptionMenu(frame, show_var, "morning", "evening")
show_dropdown.grid(row=1, column=1, padx=5, pady=5)

seat_label = tk.Label(frame, text="Seat No:")
seat_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
seat_entry = tk.Entry(frame, width=30)
seat_entry.grid(row=2, column=1, padx=5, pady=5)

book_button = tk.Button(frame, text="Book Ticket", command=book_ticket, bg="#28a745", fg="white")
book_button.grid(row=3, column=0, padx=5, pady=10)

cancel_button = tk.Button(frame, text="Cancel Booking", command=cancel_booking, bg="#dc3545", fg="white")
cancel_button.grid(row=3, column=1, padx=5, pady=10)

# Booked Tickets List
list_label = tk.Label(root, text="Booked Tickets", font=("Arial", 14, "bold"))
list_label.pack(pady=10)
booking_list = tk.Listbox(root, width=80, height=10)
booking_list.pack(pady=10)

# Start GUI
root.mainloop()