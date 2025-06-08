#Packages/libraries
import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import push_notebook
from bokeh.layouts import column
from bokeh.resources import INLINE

#Opens and read the data.txt file
with open('data.txt', 'r') as f:
    data_lines = f.readlines()[1:]  #Skips the first line (header) and read the rest of the lines

#initializes lists to store years and totals
years = []
totals = []


for line in data_lines: #loops and iterates lintes through the data in the txt file
    data = line.strip().split(",")  #Splits the line using a comma (",") as the separator
    if len(data) >= 14:  # Check if the line has at least 14 elements (including the header)
        year = int(data[0]) #Extracts year
        total_value = int(data[-1])  #Extracts GDP
        years.append(year) #Appends year to the year list
        totals.append(total_value)  #appends the GDP to the GDP list

#converts lists to NumPy arrays
years = np.array(years)
totals = np.array(totals)

#creates the bar plot
x_labels = [str(year) for year in years]
p = figure(x_range=x_labels, height=800, width=1000, title="Total for Each Year")
p.vbar(x=x_labels, top=totals, width=0.6, line_color="white", fill_color="blue")

#Plot graph
p.xaxis.axis_label = 'Year'
p.yaxis.axis_label = 'Total'
p.xgrid.grid_line_color = None
p.y_range.start = 0
p.title.text_font_size = '16pt'
p.xaxis.major_label_orientation = 1.2

#Displays the graph directly from jupiters notebook which makes it an interactive plot
show(column(p), notebook_handle=True)
