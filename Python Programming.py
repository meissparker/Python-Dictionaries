service_tickets = {"111": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"}, 
                   "222": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"},
                   "333": {"Customer": "Beatrice", "Issue": "Payment Issue", "Status": "closed"}}

def open(service_tickets, ticket_id, name, description, status):
    if ticket_id not in service_tickets:
        service_tickets[ticket_id] = {"Customer": name, "Issue": description, "Status": status}
        print(f"Ticket # {ticket_id} added.")
    else:
        print(f"Ticket # {ticket_id} already exists.")

def update(service_tickets, ticket_id, status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = status
        print(f"Ticket # {ticket_id} status updated.")
    else:
        [print(f"Ticket # {ticket_id} not found.")]

def display(service_tickets):
    for ticket_id, details in service_tickets.items():
        print(f"Ticket ID: {ticket_id}, Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")

while True:
    print("\n Customer Service Ticket Tracking System")
    print("\n1: Open Ticket\n2: Update Ticket\n3: Display Tickets\n4: Exit ")
    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        tid = int(input("Enter Ticket ID #: "))
        name = input("Enter the customer name: ")
        desc = input("Enter the description of the problem: ")
        status = input("Enter the ticket status (Open/Closed): ")
        open(service_tickets, tid, name, desc, status)
    elif choice == 2:
        tid = int(input("Enter Ticket ID #: "))
        status = input("Enter the ticket status (Open/Closed): ")
        update(service_tickets, tid, status)
    elif choice == 3:
        display(service_tickets)
    elif choice == 4:
        print("Exiting System...")
        break










