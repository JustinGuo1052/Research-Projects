import math

def mean_change(s):
    length = len(s)
    # print(length)
    l_sum = 0
    for i in range(0, length - 1):
        l_sum += abs(s[i + 1] - s[i])

    # print(l_sum, amplitude)
    return l_sum / length


def average_change(s):
    length = len(s)
    sum = 0
    amplitude = max(s) - min(s)

    if amplitude == 0:
        return 0
    for i in range(length - 1):
        sum += abs(s[i + 1] - s[i])

    return sum / amplitude


def inte(s):
    sum = 0
    for i in range(len(s) - 1):
        sum += 0.5 * 1 * (abs(s[i + 1]) + abs(s[i]))
    return sum


def gmean(arr):
    pro = 1
    for i in arr:
        if i == 0:
            continue
        pro *= i
    pro = math.pow(pro, 1 / len(arr))
    return pro

def colored_line_between_pts(x, y, c, ax, **lc_kwargs):
    """
    Plot a line with a color specified between (x, y) points by a third value.

    It does this by creating a collection of line segments between each pair of
    neighboring points. The color of each segment is determined by the
    made up of two straight lines each connecting the current (x, y) point to the
    midpoints of the lines connecting the current point with its two neighbors.
    This creates a smooth line with no gaps between the line segments.

    Parameters
    ----------
    x, y : array-like
        The horizontal and vertical coordinates of the data points.
    c : array-like
        The color values, which should have a size one less than that of x and y.
    ax : Axes
        Axis object on which to plot the colored line.
    **lc_kwargs
        Any additional arguments to pass to matplotlib.collections.LineCollection
        constructor. This should not include the array keyword argument because
        that is set to the color argument. If provided, it will be overridden.

    Returns
    -------
    matplotlib.collections.LineCollection
        The generated line collection representing the colored line.
    """
    # Create a set of line segments so that we can color them individually
    # This creates the points as an N x 1 x 2 array so that we can stack points
    # together easily to get the segments. The segments array for line collection
    # needs to be (numlines) x (points per line) x 2 (for x and y)
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(segments, **lc_kwargs)

    # Set the values used for colormapping
    lc.set_array(c)

    return ax.add_collection(lc)