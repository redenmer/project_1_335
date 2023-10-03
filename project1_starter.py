#Ian Martinez
# CPSC 335-09
# b.ianmartinez98@csu.fullerton.edu





  # Input values are coming from text.file
import re
from datetime import datetime, timedelta

def find_common_available_time(person1_intervals, person2_intervals, work_start, work_end, min_meeting_duration_minutes):
    work_start_time = datetime.strptime(work_start, '%H:%M')
    work_end_time = datetime.strptime(work_end, '%H:%M')

    merged_intervals = []
    for interval in person1_intervals + person2_intervals:
        start_time = datetime.strptime(interval[0], '%H:%M')
        end_time = datetime.strptime(interval[1], '%H:%M')
        merged_intervals.append((start_time, end_time))

    merged_intervals.sort(key=lambda x: x[0])

    common_available_slots = []

    current_time = work_start_time

    min_meeting_duration = timedelta(minutes=min_meeting_duration_minutes)

    for interval in merged_intervals:
        start_time, end_time = interval

        if start_time > current_time:
            gap_duration = start_time - current_time
            if gap_duration >= min_meeting_duration and end_time <= work_end_time:
                common_available_slots.append([current_time.strftime('%H:%M'), start_time.strftime('%H:%M')])

        current_time = max(current_time, end_time)

    if work_end_time - current_time >= min_meeting_duration:
        common_available_slots.append([current_time.strftime('%H:%M'), min(current_time + min_meeting_duration, work_end_time).strftime('%H:%M')])

    return common_available_slots

# Read input
with open('input.txt', 'r') as file:
    person1_intervals = eval(file.readline().strip())
    print("Person 1 Schedule")
    print("Schedule:", person1_intervals)
    work_hours1 = file.readline().strip().split(',')
    print("Working Hours:", work_hours1)
    meeting_duration = int(file.readline().strip())
    print("Meeting Duration:", meeting_duration, "minutes")

    person2_intervals = eval(file.readline().strip())
    print("\nPerson 2 Schedule")
    print("Schedule:", person2_intervals)
    work_hours2 = file.readline().strip().split(',')
    print("Working Hours:", work_hours2)

common_available_time_slots = find_common_available_time(
    person1_intervals, person2_intervals, work_hours1[0], work_hours1[1], meeting_duration
)

with open('output.txt', 'w') as output_file:
    if common_available_time_slots:
        output_file.write("Common Available Time Slots:\n")
        for slot in common_available_time_slots:
            output_file.write(f"[{slot[0]} - {slot[1]}]\n")
    else:
        output_file.write("No common available time slots.\n")
