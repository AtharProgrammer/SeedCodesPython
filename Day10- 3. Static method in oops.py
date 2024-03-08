from datetime import datetime

class DateUtils:
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def parse_date(date_str):
        return datetime.strptime(date_str, DateUtils.DATE_FORMAT)

# You can call the static method to parse a date string
date_obj = DateUtils.parse_date("2024-03-08")
formatted_date = date_obj.strftime("%Y-%m-%d")

print(formatted_date)  # Output: 2024-03-08
