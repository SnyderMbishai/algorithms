from datetime import datetime


def is_deletion_candidate(date):
    """
    True if not 1st date of the month or if older than 14 days
    """

    date = datetime.strptime(date, "%Y-%m-%d")
    time_lapsed = (datetime.now() - date).days

    if date.day != 1 and time_lapsed > 14:
        return True
    return False


print(is_deletion_candidate("2021-04-01"))
