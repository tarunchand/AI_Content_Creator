import datetime


class GeneralUtility:

    @staticmethod
    def get_date_time():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
