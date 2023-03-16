import pandas as pd

# Define the data for the dataframe
data = {'Date': ['2023-03-16', '2023-03-17', '2023-03-18'],
        'Hours/Minutes': ['1h 30m', '2h 15m', '45m'],
        'Activity': ['Exercise', 'Work', 'Reading']}

# Create the dataframe
df = pd.DataFrame(data)

# Print the dataframe
print(df)
