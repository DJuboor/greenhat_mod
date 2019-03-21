from datetime import date, timedelta
from random import randint
import numpy as np


def build_array():
    """
    Build an NxM array corresponding to the week and day, respectively,
    of which the [i,j]'th index of the array is equal to the amount
    of Github commits for that day

    :return: Week x Day array containing commit counts for each position
    """

    # initialize a matrix for the year:
    #    53 weeks (52 weeks + current week)  x  7 days
    array = np.zeros(shape=(53, 7)).astype(int)
    weeks, days = array.shape

    # Random amount of commits per day
    for week in range(weeks):
        for day in range(days):
            daily_commits = randint(1, 5)
            array[week, day] = daily_commits

    # Negate tail end of current week (if today is mid-week)
    current_weekday = date.today().weekday()

    last_week = weeks - 1
    for day in range(days):
        if day > current_weekday:
            array[last_week, day] = 0

    return array


def array_builder(input_string: str) -> array:

    # Letter Dictionary
    # Build 7x52 array of zeros (using Numpy)
    # take string input, turn to lowercase
    # Letter-by-letter insert into the array of zeros
return our_array
