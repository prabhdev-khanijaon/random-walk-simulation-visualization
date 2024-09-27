import plotly.express as px

from random_walk import RandomWalk


# Allow the user to make new walks as long as the program is active.
while True :
    # Make a random walk.
    rw = RandomWalk(100_000)
    rw.fill_walk()

    # Assign the result's data points to plot and color in order.
    point_numbers = range(rw.num_points)

    # Visualize the results.
    fig = px.scatter(x=rw.x_values, y=rw.y_values, color=point_numbers, 
                     color_continuous_scale='Blues', 
                     title="A Random Walk With 100,000 Points",
                     template='plotly_dark')
    
    # Emphasize the first and last points.
    fig.add_scatter(x=[rw.x_values[0]], y=[rw.y_values[0]], 
                    mode='markers', 
                    marker=dict(size=20, color='green', symbol='circle'),
                    name='Start')
    fig.add_scatter(x=[rw.x_values[-1]], y=[rw.y_values[-1]], 
                    mode='markers', 
                    marker=dict(size=20, color='red', symbol='circle'),
                    name='End')
    
    fig.show()


    new_walk = input("Make another random walk? (y/n): ")
    if new_walk == 'n' :
        break