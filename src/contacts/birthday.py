import datetime


class Birthday:
    def __init__(self, value):
        # self.set_value(value)
        self.value = value

    def is_valid(self, value):

        try:
            datetime.strptime(value, "%Y-%m-%d")
            return True
        except ValueError as e:
            raise ValueError(f"Wrong date format: {e}")

    def set_value(self, value):
        if value:
            if not self.is_valid(value):
                raise ValueError("Invalid value")
        self.value = value

    def __str__(self):
        return str(self.value)
