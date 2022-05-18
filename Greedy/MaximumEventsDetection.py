# class that creates instances of each event
class Events():

    def __init__(self, start, end, index):

        self.start = start
        self.end = end
        self.index = index


# Function that takes all registered events and returns events 
# that are possible by maximizing no of events that going to happen
# Here we are maximizing no of events that are happening means we are greedly approaching to our problem

def BestPossibleEvents(Form):

    # Initially we don't have any possible events    
    MaxPossibleEvents = []

    # Sorting Form instances based on end time of the events
    Form.sort(key = lambda item : item.end)

    # Always first event happens, so we append it to possible events
    MaxPossibleEvents.append(Form[0].index)

    # Endtime of event
    TimeLimit = Form[0].end

    # Looping through each instance in Form and appending
    # Events that are possible to happen
    for i in range(1,len(Form)):

        # If next event start time is less than current event end time
        # Then next event also possible to happend, therefore append event
        if Form[i].start > TimeLimit:

            # Append index to list, so that we can get data using index later
            MaxPossibleEvents.append(Form[i].index)

            # Change time limit to current event end time
            TimeLimit = Form[i].end

    return MaxPossibleEvents


# List with start time of all events registered
Start=[1, 1.5, 1.8, 3, 8.5, 9.2, 2.5]

# List with end time of all evenst regestered
End=[1.2, 2.1, 2.8, 5, 8.5, 9.75, 3]

# Initilizing list
Form=[]

# Creating instances from Events class with respect to every event that is registered
for i in range(len(Start)):
    Form.append(Events(Start[i], End[i],i))

BestEventss = BestPossibleEvents(Form)

for i in BestEventss:
    print(f"{Start[i]} - {End[i]}")


# output

# 1 - 1.2
# 1.5 - 2.1
# 2.5 - 3
# 8.5 - 8.5
# 9.2 - 9.75
