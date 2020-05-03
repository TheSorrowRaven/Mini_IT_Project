import matplotlib.pyplot as plt

# Data to plot
labels = 'Clothing', 'Entertainment', 'Foods and drinks', 'Transportation'
sizes = [215, 130, 245, 210] #sample data
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()
