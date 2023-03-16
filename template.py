import pandas as pd
import random

total_time = 180  # 3 hours in minutes

# Generate four random periods of time that add up to total_time
time_periods = []
for i in range(3):
    remaining_time = total_time - sum(time_periods)
    time_periods.append(random.randint(1, remaining_time))

# The last time period is whatever time is remaining to add up to total_time
time_periods.append(total_time - sum(time_periods))


# Define the data for the dataframe
data = {
    'Date': ['2023-03-16', '2023-03-17', '2023-03-18'],
    'Hours/Minutes': 'blah',
    'Activity': ['Exercise', 'Work', 'Reading']
    }

# Create the dataframe
df = pd.DataFrame(data)

# Print the dataframe
print(df)
