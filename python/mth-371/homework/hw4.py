from mth_371 import *

# ┬ ┬┌─┐┌┬┐┌─┐┬ ┬┌─┐┬─┐┬┌─  ┌─┐┌─┐┬ ┬┬─┐
# ├─┤│ ││││├┤ ││││ │├┬┘├┴┐  ├┤ │ ││ │├┬┘
# ┴ ┴└─┘┴ ┴└─┘└┴┘└─┘┴└─┴ ┴  └  └─┘└─┘┴└─


def luby_p_vector(B, weight):
    return pvec


def luby_coarse(mtx, weight_vec):
    return pmtx * adjMtx * pmtx.T


# testing #####################################################################


##################################################################### testing #


def recursive_luby(filepath):
    """
    In this main function we can read the file path with read_data function,
    then call the luby_coarse() function , and a stopping point is once the coarse graph
    has reached desired size.
    """
    data = read_csv(filepath)
    stopping = floor(mtx.shape[0] / 8)
    coarse = luby_coarse(mtx)

    """
    some example code
    while True:
      if :check if graph is small enough
            break
      else:
            do luby coarsing
    """
    return


# testing #####################################################################


##################################################################### testing #
