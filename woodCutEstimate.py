"""
This File contains all the needed components for the woodCutEstimate function.
"""

def woodCutEstimate(feed_rate, load_time, cut_list):
    """
    The woodCutEstimate function estimates the time it will take to cut all the wood in a given cut list. It does
    so using a few customizable parameters and some calculations using the cut list. It is assumed that you already
    have the needed wood for the cuts and that each cut will actually need to be cut and is not already available
    (ie there is no check to see if there is a wood of perfect size for one of the cuts). Instead, it uses an
    overestimation technique of using the sum of each boards' length and width to give an idea for how much will
    need to be fed to the table saw.

    Receives:
        - feed_rate - Feed rate of the table saw (common feed rates are between 10 and 30 ft/min)
        - load_time - The time it take to adjust the table saw to the proper settings and load the wood (generally
                      between 30 seconds to 2 minutes)
        - cut_list  - A list of cuts that
    Returns:
        - Time it takes to cut the wood (Float)
    """
    cut_length = 0
    for board in cut_list:
        cut_length += (board.get_length() + board.get_width())

    return feed_rate*cut_length + load_time*len(cut_list)
