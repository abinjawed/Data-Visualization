from bokeh.plotting import figure, show
from bokeh.charts import BoxPlot, Histogram, Scatter
from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.layouts import gridplot

import pandas as pd

data = pd.read_csv("baseball.csv")

print(data.head())
print(len(pd.unique(data['name'])))

colormap = {'R': 'red', 'L': 'green', 'B' : 'blue'}
colors = [colormap[x] for x in data['handedness']]

source = ColumnDataSource(data)

tools = ["box_select", "hover", "pan", "box_zoom", "reset"]
p_all = figure(tools = tools, title = 'Batting Average vs Home Runs of all players', height = 200)
p_all.xaxis.axis_label = 'Average'
p_all.yaxis.axis_label = 'Home Runs'
p_all.circle(x="avg", y="HR", color = colors, hover_color="red", source = source)


view1 = CDSView(source=source, filters=[GroupFilter(column_name='handedness', group='R')])
p_R = figure(tools = tools, title = 'Batting Average vs Home Runs of right handed players', height = 200)
p_R.xaxis.axis_label = 'Average'
p_R.yaxis.axis_label = 'Home Runs'
p_R.circle(x="avg", y="HR", color = 'red', hover_color="yellow", view=view1, source = source)


view2 = CDSView(source=source, filters=[GroupFilter(column_name='handedness', group='L')])
p_L = figure(tools = tools, title = 'Batting Average vs Home Runs of left handed players', height = 200)
p_L.xaxis.axis_label = 'Average'
p_L.yaxis.axis_label = 'Home Runs'
p_L.circle(x="avg", y="HR", color = 'green', hover_color="yellow", view=view2, source = source)

view3 = CDSView(source=source, filters=[GroupFilter(column_name='handedness', group='B')])
p_B = figure(tools = tools, title = 'Batting Average vs Home Runs of both handed players', height = 200)
p_B.xaxis.axis_label = 'Average'
p_B.yaxis.axis_label = 'Home Runs'
p_B.circle(x="avg", y="HR", color = 'blue', hover_color="yellow", view=view3, source = source)


hist = Histogram(data, values='avg', title="Average of all", plot_height=300)
hist2 = Histogram(data, values='avg', label='handedness', color='handedness', legend='top_right',
                  title="Average of R, L and B handedness", plot_height=300)

hist3 = Histogram(data, values='HR', title="Home runs of all", plot_height=300)
hist4 = Histogram(data, values='HR', label='handedness', color='handedness', legend='top_right',
                  title="Home runs of R, L and B handedness", plot_height=300)

marker = {'R': 'red', 'L': 'green', 'B' : 'blue'}
markers = ['0.05' if x <= 0.05 else '0.01' if 0.05 < x <= 0.10 else '0.15' if 0.10 < x < 0.15 else '0.20' if 0.15 < x < 0.20 else '0.25' if 0.25 < x < 0.30 else '0.30' for x in data['avg']]

scatter1 = Scatter(data, x='weight', y='avg', color='handedness',
                  title="Weight vs Average", xlabel="Weight",
                  ylabel="Average", plot_height=300)

scatter2 = Scatter(data, x='height', y='avg', color='handedness',
                  title="Height vs Average", xlabel="Height",
                  ylabel="Average", plot_height=300)

scatter3 = Scatter(data, x='weight', y='HR', color='handedness',
                  title="Weight vs Home Runs", xlabel="Weight",
                  ylabel="Home Runs", plot_height=300)

scatter4 = Scatter(data, x='height', y='HR', color='handedness',
                  title="Height vs Home Runs", xlabel="Height",
                  ylabel="Home Runs", plot_height=300)

show(gridplot([[p_all],[p_L],[p_R], [p_B], [hist], [hist2], [hist3], [hist4], [scatter1], [scatter2], [scatter3], [scatter4]],
