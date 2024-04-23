swim_time_range = (int(input(" What Time did you finish Your swim sector of the triathlon in minutes? ")))
cycle_time_range = (int(input(" What Time did you finish Your cycle sector of the triathlon in minutes? ")))
Run_time_range = (int(input(" What Time did you finish Your run sector of the triathlon in minutes? ")))

total_time_taken = (swim_time_range + cycle_time_range + Run_time_range )

print("You completed triathlon in ", total_time_taken, "Minutes !")
if total_time_taken < 101:
    print("Well done! you finished within the quailyifing time, and have been awarded the provinicial Colours")

elif total_time_taken <= 105:
    print("Well done! you finished within 5 minutes of the quailyifing time, and have been awarded the provinicial half Colours award")

elif total_time_taken <= 110:
    print("Well done! you finished within 10 minutes of the quailyifing time, and have been awarded the provinicial scroll")

else:
    total_time_taken >= 111
    print ("Congratulations, on finishing, unfortunately you finished outside of the quailyifing timed, no award was issued")