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


def get_date_string(array_position: tuple) -> str:
    """
    Take tuple corresponding to the current location of the commit_array
    and map that to the date it represents in a format that Github
    can understand

    :param array_position: a (w,d) tuple where w corresponds to the week
    number and d corresponds to the day of the week number
    :return: a formatted string of the date time
             format (Tue Jan 01 00:00:00 2019  -0400)
    """
    d = startdate - timedelta(days=n)
    rtn = d.strftime("%a %b %d %X %Y %z -0400")
    return rtn


def main(commit_array) -> None:
    """
    Take the commit_array and post a mock file back-dated
    to a github repository once for every commit as described for that
    location of the array

    :param commit_array: some number of days before start date

    :return: Github commit history should be updated
    """

    if len(argv) < 1 or len(argv) > 2:
        print("Error: Bad input.")
        sys.exit(1)
    n = int(argv[0])
    if len(argv) == 1:
        startdate = date.today()
    if len(argv) == 2:
        startdate = date(
            int(argv[1][0:4]), int(argv[1][5:7]), int(argv[1][8:10]))
    i = 0
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
    main(sys.argv[1:])
