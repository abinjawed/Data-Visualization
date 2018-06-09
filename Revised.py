from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.layouts import gridplot

import pandas as pd

data = pd.read_csv("baseball.csv")

print(data.head())
print(len(pd.unique(data['name'])))

colormap = {'R': 'red', 'L': 'green', 'B' : 'blue'}
colors = [colormap[x] for x in data['handedness']]

#source = ColumnDataSource(data=dict(avg=data['avg'], HR=data['HR'], handedness=data['handedness']))
source = ColumnDataSource(data)

tools = ["box_select", "lasso_select", "hover", "pan", "box_zoom", "reset"]
p_all = figure(tools = tools, title = 'Batting Average vs Home Runs of all players', height = 200, width=1200)
p_all.xaxis.axis_label = 'Average'
p_all.yaxis.axis_label = 'Home Runs'
p_all.circle(data["avg"], data["HR"], color = colors, hover_color="red")


view1 = CDSView(source=source, filters=[GroupFilter(column_name='handedness', group='R')])
p_R = figure(tools = tools, title = 'Batting Average vs Home Runs of right handed players', height = 200, width=1200)
p_R.xaxis.axis_label = 'Average'
p_R.yaxis.axis_label = 'Home Runs'
p_R.circle(x="avg", y="HR", color = 'red', hover_color="yellow", view=view1, source = source)


view2 = CDSView(source=source, filters=[GroupFilter(column_name='handedness', group='L')])
p_L = figure(tools = tools, title = 'Batting Average vs Home Runs of left handed players', height = 200, width=1200)
p_L.xaxis.axis_label = 'Average'
p_L.yaxis.axis_label = 'Home Runs'
p_L.circle(x="avg", y="HR", color = 'green', hover_color="yellow", view=view2, source = source)

view3 = CDSView(source=source, filters=[GroupFilter(column_name='handedness', group='B')])
p_B = figure(tools = tools, title = 'Batting Average vs Home Runs of both handed players', height = 200, width=1200)
p_B.xaxis.axis_label = 'Average'
p_B.yaxis.axis_label = 'Home Runs'
p_B.circle(x="avg", y="HR", color = 'blue', hover_color="yellow", view=view3, source = source)


# hist = Histogram(data, values='avg', title="Average of all", plot_height=300)
# hist2 = Histogram(data, values='avg', label='handedness', color='handedness', legend='top_right',
#                   title="Average of R, L and B handedness", plot_height=300)
#
# hist3 = Histogram(data, values='HR', title="Home runs of all", plot_height=300)
# hist4 = Histogram(data, values='HR', label='handedness', color='handedness', legend='top_right',
#                   title="Home runs of R, L and B handedness", plot_height=300)

marker = {'R': 'red', 'L': 'green', 'B' : 'blue'}
markers = ['0.05' if x <= 0.05 else '0.01' if 0.05 < x <= 0.10 else '0.15' if 0.10 < x < 0.15 else '0.20' if 0.15 < x < 0.20 else '0.25' if 0.25 < x < 0.30 else '0.30' for x in data['avg']]

scatter1 = figure(tools = tools, title="Weight vs Average", height = 200, width=1200)
scatter1.xaxis.axis_label = 'Weight'
scatter1.yaxis.axis_label = 'Average'
scatter1.scatter(data['weight'], y=data['avg'], color=colors)

scatter2 = figure(tools = tools, title="Height vs Average", height = 200, width=1200)
scatter2.xaxis.axis_label = 'Height'
scatter2.yaxis.axis_label = 'Average'
scatter2.scatter(data['height'], data['avg'], color=colors)

scatter3 = figure(tools = tools, title="Weight vs Home Runs", height = 200, width=1200)
scatter3.xaxis.axis_label = 'Weight'
scatter3.yaxis.axis_label = 'Home Runs'
scatter3.scatter(data['weight'], data['HR'], color=colors)

scatter4 = figure(tools = tools, title="Height vs Home Runs", height = 200, width=1200)
scatter4.xaxis.axis_label = 'Height'
scatter4.yaxis.axis_label = 'Home Runs'
scatter4.scatter(data['height'], data['HR'], color=colors)

#show(gridplot([[p_all],[p_L],[p_R], [p_B], [hist], [hist2], [hist3], [hist4], [scatter1], [scatter2], [scatter3], [scatter4]]))
show(gridplot([[p_all],[p_L],[p_R], [p_B], [scatter1], [scatter2], [scatter3], [scatter4]]))
