class MetroTickets:
    def __init__(self, total_tickets):
        self.total_tickets = total_tickets
        self.current_ticket = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_ticket <= self.total_tickets:
            ticket = (f"Ticket- {self.current_ticket}")
            self.current_ticket += 1
            return ticket
        else:
            raise StopIteration

metro = MetroTickets(6)
for i in metro:
    print(i)