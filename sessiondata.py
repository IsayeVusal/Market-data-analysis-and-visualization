#Session data

#From our server logs, you can access the raw session data, that contains information about single visits to our website (= sessions). A click out is logged whenever a user clicks on a hotel and is redirected to the booking page. The booking field is binary and indicates if a hotel booking was logged after one of the click outs. Have a look at the data and check if there is any connection between the booking data and other given information. 

# read data
session = pd.read_csv("session_data.csv", sep=";")

session["time_spent"] = "None" # we need new column to add time spent while booking
session["time_spent"] = pd.to_datetime(session.session_end_text) - pd.to_datetime(session.session_start_text) # end time - start time

session["start_hour"] = session['session_start_text'].apply(lambda x: x.split(":")[0]) # to know exact hour when session started 
session["end_hour"] = session['session_end_text'].apply(lambda x: x.split(":")[0]) # hour when session ended

# start hour when booking was successful
booked = session.loc[session['booking'] == 1]
booked["start_hour"].value_counts()

# time spent when session was successful
booked = session.loc[session['booking'] == 1]
booked["time_spent"].value_counts()

# start hour when booking was unsuccessful
not_booked = session.loc[session['booking'] == 0]
not_booked["start_hour"].value_counts()

# time spent when booking was unsuccessful
not_booked = session.loc[session['booking'] == 0]
not_booked["time_spent"].value_counts()

session.head(10)

# Overall information when booking was successful
# Counting in which hour how many times hotel was booked (left side)
# Counting how much time was spent while booking was successful (right side)
start_hour_booked = booked["start_hour"].value_counts()
time_spent_booked = booked["time_spent"].value_counts()
for i, j in zip(start_hour_booked.items(), time_spent_booked.items()):
    print(i,j)
    
# Overall information when booking was unsuccessful
# Counting in which hour how many times hotel booking was unsuccessful (left side)
# Counting how much time was spent while booking was unsuccessful (right side)
start_hour_not_booked = not_booked["start_hour"].value_counts()
time_spent_not_booked = not_booked["time_spent"].value_counts()
for z, k in zip(start_hour_not_booked.items(), time_spent_not_booked.items()):
    print(z,k)
    
    
