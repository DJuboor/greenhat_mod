# Copyright (c) 2015 Angus H. (4148)
# Distributed under the GNU General Public License v3.0 (GPLv3).

from datetime import date, timedelta
from random import randint
from time import sleep
import sys
import subprocess
import numpy as np


def build_array():
    """
    Build an NxM array corresponding to the week and day, respectively,
    of which the [i,j]'th index of the array is equal to the amount
    of Github commits for that day

    :return: Week x Day array containing commit counts for each position
    """

    # initialize a matrix for the year
    #   53 weeks (52 weeks + current week)  x  7 days
    array = numpy.zeros(shape=(53, 7)).astype(int)
    weeks, days = array.shape

    # Random amount of commits per day
    for week in range(weeks):
        for day in range(days):
            daily_commits = randint(1, 5)
            array[week, day] = daily_commits

    # Negate tail end of current week (if today is mid-week)

    # today.weekday returns 0 = monday, 6 = sunday. Github starts week on Sunday
    #    So we have to add some catches for this
    current_weekday = date.today().weekday()

    last_week = weeks - 1
    for day in range(days):
        if day - 1 > current_weekday:  # day-1 fixes indexing monday as start of week
            array[last_week, day] = -1

        if current_weekday == 6:  # fixes the broken case where Sunday = 6 (because it should = 0 for github)
            array[last_week, 1:] = -1

    return array


def get_date_string(n: int, startdate: object) -> str:
    """
    We'll need a function that can return the formatted datetime string
    when given how many days from today.

    :param n: Number of days since start date
    :param startdate: the fatetime object of the day we want to count from

    :return:
    """
    d = startdate - timedelta(days=n)
    rtn = d.strftime("%a %b %d %X %Y %z -0400")
    return rtn


def build_commit_records(commit_array: np.array) -> list:
    """
    In order to be able to commit our random commits to github, we're going to
    need to generate a list of the dates in which we need to commit (in the
    right date-time format) and the amount of times we need to commit for that
    date.

    :param commit_array: a 53x7 numpy array of the amount of commits generated
                            by the build_array function
    :return: A list of lists containing the formatted datetime string and the
                corresponding number of commits for that day.
    """

    flat_commits = [
        day for week in commit_array for day in week  # Nested loop
        if day != -1  # Making sure that we skip days that haven't happened yet
    ]

    # Let's generate a list of date-time formats for our flat random array
    commit_records = []
    for days_prior in range(
            364, -1, -1):  # 365 days in a year, but indexed at 0 so (365-1)
        today = date.today()
        prior_date = get_date_string(days_prior, today)

        commit_index = 364 - days_prior  # since we're itterating in reverse

        commit_records.append([prior_date, flat_commits[commit_index]])

    return commit_records


def main(commit_array) -> None:
    """
    Take the commit_array and post a mock file back-dated
    to a github repository once for every commit as described for that
    location of the array

    :param commit_array: some number of days before start date

    :return: Github commit history should be updated
    """

    while i <= n:
        curdate = get_date_string(i, startdate)
        num_commits = randint(1, 10)
        for commit in range(0, num_commits):
            subprocess.call(
                "echo '" + curdate + str(randint(0, 1000000)) +
                "' > realwork.txt; git add realwork.txt; GIT_AUTHOR_DATE='" +
                curdate + "' GIT_COMMITTER_DATE='" + curdate +
                "' git commit -m 'update'; git push;",
                shell=True)
            sleep(.5)
        i += 1
    subprocess.call(
        "git rm realwork.txt; git commit -m 'delete'; git push;", shell=True)


if __name__ == "__main__":
    array = build_array()
    commit_record = build_commit_records(array)

    print(commit_record)
