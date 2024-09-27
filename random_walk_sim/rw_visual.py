import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True :
    # Make a random walk.
    rw = RandomWalk(100_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('bmh')
    # Make the plotting window better fit your screen.
    fig, ax = plt.subplots(figsize=(9, 6))
    # Use a colormap to show the order of the points in the walk.
    # To color the points according to their position in the walk,
    #   pass the c argument a list containing the position of each point.
    # Remove the black outline from each dot.
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=1)
#    ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.set_aspect('equal')

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
               s=100)
    
    # Remove the axes, so they don't distract from the path of each walk.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n' :
        break