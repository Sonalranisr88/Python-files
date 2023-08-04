distance_km = 10
time_minutes = 43
time_seconds = 30

distance_miles = distance_km * 0.621371

time_hours = (time_minutes + time_seconds / 60) / 60

time_per_mile = (time_minutes * 60 + time_seconds) / distance_miles

speed_mph = distance_miles / time_hours

print("Average time per mile:", round(time_per_mile, 2), "minutes")
print("Average speed:", round(speed_mph, 2), "miles per hour")

