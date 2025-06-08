#Packages/Libraries
import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import NumeralTickFormatter
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool

#initialize empty lists
years = [] 
gdp = []

with open("gdpdata.txt", "r") as f: #opens and reads the file
    data_lines = f.readlines()[1:]  #skips the first line (header) and read the rest of the lines

for line in data_lines: #Loops line through each data line in the gdp data file
    data = line.strip().split(",")  #Splits the line into a list of values using ","
    if len(data) >= 2:
        year = int(data[0]) #Extracts year
        gdp_value = float(data[1]) #Extracts GDP
        years.append(year) #Appends year to the year list
        gdp.append(gdp_value) #appends the GDP to the GDP list

#Creates a ColumnDataSource from the data
source = ColumnDataSource(data=dict(years=years, gdp=gdp))

#Creates graph with dimensions
p = figure(title='Yearly GDP', x_axis_label='Year', y_axis_label='GDP (Billion USD)',
           width=800, height=400)

#Color of line in line graph
p.line('years', 'gdp', source=source, line_width=2, line_color='blue')

#Y-axis tick labels as billions
p.yaxis[0].formatter = NumeralTickFormatter(format='$0,0')

#Hover tool to display GDP value on mouse hover
hover = HoverTool()
hover.tooltips = [('Year', '@years'), ('GDP', '@gdp{$0.00}')]
p.add_tools(hover)

#Displays the plot
show(p)
