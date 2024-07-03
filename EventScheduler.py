import datetime

class Event: #class 1
    def __init__(self, name, date, time, description): #constructor
        self.name = name
        self.date = date
        self.time = time
        self.description = description

    def display(self): #display the details
        print("Enter name:",self.name)
        print("Enter date:",self.date)
        print("Enter time:",self.time)
        print("Enter description:",self.description)


class Scheduler: #class 2
    def __init__(self):
        self.list = [] #empty list to add up the events
        self.last_event = None 

    def add(self, name, date, time, description): #adding the events
        try: #validation of date
            event_date = datetime.datetime.strptime(date, "%Y-%m-%d").date() #format for date
            event_time = datetime.datetime.strptime(time, "%H:%M").time( )  #format for time
            today = datetime.date.today()
            if event_date < today:
                print("This event cannot be added to a previous date/year. Please enter a valid date.")
                return
        except ValueError: #if date format is wrong
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
            return
        
        for con in self.list: #conflict oocurs if same time 2 events are added
            if con.date == date:
                existing_event_time = datetime.datetime.strptime(con.time, "%H:%M").time()
                if event_time == existing_event_time:
                    print("Cannot add event.Event is already booked at the same slot.")
                    return
                if event_time > existing_event_time and datetime.datetime.strptime(time, "%H:%M").time() < datetime.datetime.strptime(con.time, "%H:%M").time():
                    print("Slot booked.Please book it for the next day.")
                    return

        new_event = Event(name, date, time, description)
        if any(es.date == date and es.time == time for es in self.list): #checks if the date and time are conflicting or not.
            print("Cannot add event due to conflict.")
        else:
            self.list.append(new_event)
            self.last_event = new_event
            print("Event  added successfully.")
            
            for t in self.list:
                if t.date == date:
                    existing_event_time = datetime.datetime.strptime(t.time, "%H:%M").time()
                if event_time < existing_event_time:
                    print("Cannot add event.Please book an event for another time.")
                    
    def update(self):
        if self.last_event is None:
            print("No event to update.")
            return

        name = input("Enter new event name: ")
        date = input("Enter new event date: ")
        time = input("Enter new event time: ")
        description = input("Enter new event description: ")

        try: #validation of date
            event_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            today = datetime.date.today()
            if event_date < today:
                print("Cannot be updated to a previous date. Please enter a valid date.")
                return
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
            return

        if(es.date == date and es.time == time for es in self.list if es != self.last_event):
            print("Conflict. Updated the same data as added already.") 
        else:
            self.last_event.name = name
            self.last_event.date = date
            self.last_event.time = time
            self.last_event.description = description
            print("Event updated successfully.")

    def delete(self, name):
        for event in self.list:
            if event.name == name:
                self.events.remove(event)
                print("Event deleted successfully.")
                if self.last_event == event:
                    self.last_event = None
                return
        print("Event not found.")

    def display(self):
        if not self.list:
            print("No upcoming events.")
        else:
            for event in self.list:
                event.display()


def main():
    scheduler = Scheduler()

    while True:
        print("\nEVENT SCHEDULER\n1.Add Event \n2.Update Event \n3.Delete event \n4.Display event \n5.Exit")
    
        Option = input("Enter your choice: ")

        if Option == '1':
            name = input("Enter event name: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            time = input("Enter event time (HH:MM): ")
            description = input("Enter event description: ")
            scheduler.add(name, date, time, description)

        elif Option == '2':
            scheduler.update()

        elif Option == '3':
            name = input("Enter the name of the event to delete: ")
            scheduler.delete(name)

        elif Option == '4':
            scheduler.display()

        elif Option == '5':
            break

        else:
            print("Invalid. Choose from the above options.")

if __name__ == "__main__":
    main()
