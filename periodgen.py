import random

total_time = 180  # 3 hours in minutes

# Generate four random periods of time that add up to total_time
time_periods = []
for i in range(3):
    remaining_time = total_time - sum(time_periods)
    time_periods.append(random.randint(1, remaining_time))

# The last time period is whatever time is remaining to add up to total_time
time_periods.append(total_time - sum(time_periods))

# Print the time periods
for i, time_period in enumerate(time_periods):
    print(f"Period {i+1}: {time_period} minutes")
