import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('your_excel_file.xlsx')

plt.plot(df['X'], df['Y'])

plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')

plt.show()

