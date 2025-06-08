#Packages/libraries
import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import HoverTool
from bokeh.palettes import Spectral11

#Opens and read the data from the file
filename = "data.txt"

with open(filename, "r") as file: #opens and reads the data txt file
    data_str = file.read()

#Covers data_str to a list of lines and split each line into data points
data_lines = data_str.strip().split("\n") #converts file name to list
header = data_lines[0].split(",") #extracts header column
data_values = [line.split(",") for line in data_lines[1:]] #splits the line into data points

#coverts the data_values list to a NumPy array
data_array = np.array(data_values, dtype=np.float64)

#Extracts the years and monthly data from the array
years = data_array[:, 0]
monthly_data = data_array[:, 1:-1] / 1_000_000  #Divides by 1 million to get consumption in million liters

#Creates the graph
p = figure(width=800, height=500, title="Monthly Data for Each Year", x_axis_label="Months", y_axis_label="Consumption (Million Liters)")

#Creates the line plot for each year with a hover for each month
for i, year in enumerate(years): #loop that iterates through the elements of years
    data_source = {
        'x': np.arange(1, 13), #represents the months in the data
        'y': monthly_data[i], # y -axis is the monthly consumption
        'year': [str(year)] * 12,#displays monthly hober information
        'value': ['{:,}M'.format(int(value * 1_000_000)) for value in monthly_data[i]] # iterates values through the monthly data to show the hover
    }
    p.line(x='x', y='y', source=data_source, line_width=2, color=Spectral11[i % len(Spectral11)], legend_label=str(year))

#Adds the hover tools
hover = HoverTool()
hover.tooltips = [('Year', '@year'), ('Month', '$name'), ('Value', '@value')]
p.add_tools(hover)

#Customizes the plot
p.legend.title = "Year"
p.xaxis.ticker = np.arange(1, 13)
p.xaxis.major_label_overrides = {i: month for i, month in enumerate(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], 1)}

#Saves the plot to an HTML file and show it
output_file("line_graph.html")
show(p)
