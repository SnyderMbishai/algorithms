import re, datetime

def extract_date(string_with_date):
    date_string = f"{string_with_date}"
    match = re.search('\d{4}-\d{2}-\d{2}', date_string)
    date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()
    return date

date = "I have a meeting on 2018-12-10 in New York"
print(extract_date(date))
