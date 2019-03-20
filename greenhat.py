# Copyright (c) 2015 Angus H. (4148)
# Distributed under the GNU General Public License v3.0 (GPLv3).

from datetime import date, timedelta
from random import randint
from time import sleep
import sys
import subprocess


def get_date_string(n: int, startdate: object) -> str:
    """
    :param n: some number of days before start date
    :param startdate: the date on which we're starting from
    :return: a formatted string of the date time
             format (Tue Jan 01 00:00:00 2019  -0400)
    """
    d = startdate - timedelta(days=n)
    rtn = d.strftime("%a %b %d %X %Y %z -0400")
    return rtn


# main app
def main(argv) -> None:
    """
    :param argv: a variable argument which takes an input of number of
    days and a start date in format 'yyyy-mm-dd', if no start date
    is given then the start date is assumed to be today
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
