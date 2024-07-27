#1. Real-World Python Dictionary Applications
#Task 1: Restaurant Menu Update
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

#add
restaurant_menu["Beverages"] = {"Water": 0.99, "Soda": 2.50}
#update
restaurant_menu["Main Course"]["Steak"] = 17.99
#delete
del restaurant_menu["Starters"]["Bruschetta"]

print(restaurant_menu)

#####
#2. Python Programming Challenges for Customer Service Data Handling
#Task 1: Customer Service Ticket Tracker 
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
next_ticket_id = 3  

def generate_ticket_id(next_id):
    return f"Ticket{str(next_id).zfill(3)}"

def open_ticket(tickets, next_id, customer, issue):
    ticket_id = generate_ticket_id(next_id)
    tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
    print(f"{ticket_id} opened for {customer}.")
    return next_id + 1

def update_ticket_status(tickets, ticket_id, status):
    if ticket_id in tickets:
        tickets[ticket_id]["Status"] = status
        print(f"{ticket_id} status updated to {status}.")
    else:
        print(f"{ticket_id} not found.")

def display_tickets(tickets, status_filter=None):
    for ticket_id, info in tickets.items():
        if status_filter is None or info["Status"] == status_filter:
            print(f"{ticket_id}: {info}")

def main():
    global next_ticket_id
    while True:
        print("""
        Service Ticket System:
        1. Open a new ticket
        2. Update ticket status
        3. Display all tickets
        4. Display tickets by status
        5. Quit
        """)
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            customer = input("Enter customer name: ")
            issue = input("Enter issue description: ")
            next_ticket_id = open_ticket(service_tickets, next_ticket_id, customer, issue)
        elif choice == '2':
            ticket_id = input("Enter ticket ID: ")
            status = input("Enter new status (open/closed): ")
            update_ticket_status(service_tickets, ticket_id, status)
        elif choice == '3':
            display_tickets(service_tickets)
        elif choice == '4':
            status_filter = input("Enter status to filter by (open/closed): ")
            if status_filter!= "closed" or status_filter!= "open":
                print("Invalid input, try again!")
            else:
                display_tickets(service_tickets, status_filter)
        elif choice == '5':
            print("Thank you for using the service ticket system! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
