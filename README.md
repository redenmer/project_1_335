# Project 1 CPSC-335
Ian Martinez <br>
b.ianmartinez98@csu.fullerton.edu <br>
9-26-23 <br>
CPSC-335 <br>
Submission for Project 1 <br>

## Output For Cases

![test_cases](https://github.com/redenmer/project_1_335/assets/60246207/cc11e57d-6de7-4393-abee-20f473b51a15)




## GitHub Repo
https://github.com/redenmer/project_1_335

## How to use:
In order to use project1_starter.py Make sure to have the following on your system:
+ input.txt
+ project1_starter.py
+ output.txt

### Steps For best Results:

1. First thing you want to do is input person 1's schedule
2. Input Person 1's Clock-in and Clock-out time
3. The desired length for the meeting in terms of minutes
4. Input person 2's Schedule
5. Person 2's Clock-in and Clock-out time

**This program is very case and format sensitive**
**All inputs should follow the following format:**

```

[['09:00', '10:00'], ['11:30', '12:30'], ['14:30', '15:30']]
08:30,17:00
30
[['10:00', '11:00'], ['12:30', '13:30'], ['15:30', '16:30']]
09:00,17:30

```
**Unfortuntely this program only works if the following criteria are met**
**all value must be in military time xx:xx for any given time**
**Multiple Inputs at one time is not supported, meaning one input at one time**
```
[['09:00', '10:00'], ['11:30', '12:30'], ['14:30', '15:30']]
08:30,17:00
30
[['10:00', '11:00'], ['12:30', '13:30'], ['15:30', '16:30']]

[['09:30', '10:30'], ['11:00', '12:00'], ['14:00', '15:00']]
09:00,16:00
45
[['10:00', '11:00'], ['12:30', '13:30'], ['15:30', '16:30']]
09:00,17:00
```
```
Only thing that'll compile and give output
[['09:00', '10:00'], ['11:30', '12:30'], ['14:30', '15:30']]
08:30,17:00
30
[['10:00', '11:00'], ['12:30', '13:30'], ['15:30', '16:30']]

Output: Common Available Time Slots:
[08:30 - 09:00]
[11:00 - 11:30]
[13:30 - 14:30]
[16:30 - 17:00]
```
## Time Complexity Analysis
