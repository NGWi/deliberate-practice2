import pandas as pd
import matplotlib.pyplot as plt

# Data preparation
data = {
    'Food Category': ['Dunkin', 'Deli', 'Wings', 'Indian', 'Pizza', 'Chinese', 'Thai', 'Greek', 'Italian', 'American'],
    'DoorDash': [13.04, 16.47, 16.01, 27.50, 26.27, 63.93, 67.11, 109.55, 133.62, 157.32],
    'Grubhub': [16.61, 20.13, 18.04, 27.32, 26.67, 59.88, 65.06, 101.15, 130.07, 148.39],
    'Uber Eats': [15.93, 19.87, 16.40, 26.25, 25.67, 67.82, 68.57, 100.95, 129.75, 163.50]
}

df = pd.DataFrame(data)

# Set the index to the Food Category
df.set_index('Food Category', inplace=True)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['DoorDash'], marker='o', label='DoorDash', linestyle='-')
plt.plot(df.index, df['Grubhub'], marker='o', label='Grubhub', linestyle='-')
plt.plot(df.index, df['Uber Eats'], marker='o', label='Uber Eats', linestyle='-')

plt.title('Total Prices Across Food Orders by Delivery Service')
plt.xlabel('Food Category')
plt.ylabel('Total Price ($)')
plt.xticks(rotation=45)
plt.legend(title='Delivery Service')
plt.tight_layout()

# Show the plot
plt.show()