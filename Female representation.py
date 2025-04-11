import plotly.graph_objects as go
import numpy as np
import os

european_males = 59
southern_african_males = 12
european_females = 4
southern_african_females = 0
unknown_unknown = 6

european_male_size = 30
southern_african_male_size = 28
european_female_size = 24
southern_african_female_size = 22
unknown_size = 18

gender = (
    ['Male'] * european_males +
    ['Male'] * southern_african_males +
    ['Female'] * european_females +
    ['Unknown'] * unknown_unknown
)

nationality = (
    ['European'] * european_males +
    ['Southern African'] * southern_african_males +
    ['European'] * european_females +
    ['Unknown'] * unknown_unknown
)

sample_size = (
    [f'Male = {european_males}, European = {european_males}'] * european_males +
    [f'Male = {southern_african_males}, Southern African = {southern_african_males}'] * southern_african_males +
    [f'Female = {european_females}, European = {european_females}'] * european_females +
    [f'Unknown = {unknown_unknown}'] * unknown_unknown
)

x_positions = np.concatenate([
    np.random.normal(0, 0.2, european_males),
    np.random.normal(0, 0.1, southern_african_males),
    np.random.normal(1, 0.1, european_females),
    np.random.normal(2, 0.1, unknown_unknown)
])

y_positions = np.concatenate([
    np.random.normal(0, 0.3, european_males),
    np.random.normal(1, 0.13, southern_african_males),
    np.random.normal(0, 0.1, european_females),
    np.random.normal(2, 0.1, unknown_unknown)
])

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[None], y=[None],
    mode='markers',
    marker=dict(size=southern_african_female_size, color='magenta', opacity=0.6),
    name='Southern African Female',
    showlegend=True
))

fig.add_trace(go.Scatter(
    x=x_positions[european_males + southern_african_males:
                  european_males + southern_african_males + european_females],
    y=y_positions[european_males + southern_african_males:
                  european_males + southern_african_males + european_females],
    mode='markers',
    marker=dict(size=european_female_size, color='red', opacity=0.6),
    name='European Female',
    text=sample_size[european_males + southern_african_males:
                     european_males + southern_african_males + european_females],
    hoverinfo='text'
))

fig.add_trace(go.Scatter(
    x=x_positions[european_males:european_males + southern_african_males],
    y=y_positions[european_males:european_males + southern_african_males],
    mode='markers',
    marker=dict(size=southern_african_male_size, color='green', opacity=0.6),
    name='Southern African Male',
    text=sample_size[european_males:european_males + southern_african_males],
    hoverinfo='text'
))

fig.add_trace(go.Scatter(
    x=x_positions[:european_males],
    y=y_positions[:european_males],
    mode='markers',
    marker=dict(size=european_male_size, color='blue', opacity=0.6),
    name='European Male',
    text=sample_size[:european_males],
    hoverinfo='text'
))

fig.add_trace(go.Scatter(
    x=x_positions[european_males + southern_african_males + european_females:],
    y=y_positions[european_males + southern_african_males + european_females:],
    mode='markers',
    marker=dict(size=unknown_size, color='grey', opacity=0.6),
    name='Unknown',
    text=sample_size[european_males + southern_african_males + european_females:],
    hoverinfo='text'
))

fig.update_layout(
    title='<b>Female Representation in the Southern African Collection</b>',
    title_font=dict(family="Times New Roman", size=20),
    title_x=0.5,
    font=dict(family="Times New Roman", size=12),
    xaxis_title='<b>Gender</b>',
    yaxis_title='<b>Nationality</b>',
    xaxis=dict(tickvals=[0, 1, 2], ticktext=['Male', 'Female', 'Unknown']),
    yaxis=dict(tickvals=[0, 1, 2], ticktext=['European', 'Southern African', 'Unknown']),
    showlegend=True,
    legend=dict(
        traceorder='normal',
        itemsizing='constant',
        font=dict(size=12)
    )
)

output_path = os.path.expanduser("~/Desktop/index.html")
fig.write_html(output_path)
print(f"Plot saved to {output_path}")
