#Ian Martinez
# CPSC 335-09
# b.ianmartinez98@csu.fullerton.edu




  #
  # Declare each variable that will used to distinguish each thing
  # Set each value to zero since it'll be our initial vlaue for each vector

  # Input values are coming from text.file
import re

def process_person_schedule(file, person_name):
    print(f"{person_name} Schedule")
    busy_schedule = file.readline().strip()  # Read and store the schedule line
    print("Schedule:", busy_schedule)
    busy_time_values = re.findall(r'\d{2}:\d{2}', busy_schedule)
    print("Values:", busy_time_values)

    working_hours = file.readline().strip()  # Read and store the working hours line
    print("Working Hours:", working_hours)
    working_time_values = re.findall(r'\d{1,2}:\d{2}', working_hours)
    print("Time Values:", working_time_values)



    # Return the time values as a tuple
    return busy_time_values, working_time_values

# Usage example
with open('input.txt', 'r') as file:
    busy_time_values1, working_time_values1 = process_person_schedule(file, "Person 1")
    print("")
    busy_time_values2, working_time_values2 = process_person_schedule(file, "Person 2")

    meeting = file.readline().strip()
    print(meeting, "\n")
    merging_busy_time = busy_time_values1 + busy_time_values2
    merging_working_time = working_time_values1 + working_time_values2
    print("Both of their Schedules: " , merging_busy_time)
    print("\n")
    print("Both of their Clock-In Times: ", merging_working_time)
    print("\n")
    merging_busy_time.sort(key=lambda x: x[1])
    print("Sorted Schedules", merging_busy_time)





# Now you can access the time values outside the function
