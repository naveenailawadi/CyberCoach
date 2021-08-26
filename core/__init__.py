import pandas as pd
from core.tools import countdown


# make a general spin set class
class SpinSet:
    def __init__(self, min_rpm, max_rpm, rpe, minutes, seconds):
        # store the variables
        self.min_rpm = min_rpm
        self.max_rpm = max_rpm
        self.rpe = rpe
        self.minutes = minutes
        self.seconds = seconds

        # make a total seconds variable for the countdown
        self.total_seconds = (minutes * 60) + seconds

    # make a function that outputs everything
    def __repr__(self):
        return f"\nMin RPM: {self.min_rpm}\nMax RPM: {self.max_rpm}\nRPE: {self.rpe}"


# make a general coach class
class SpinCoach:
    # import the workout from a csv
    def __init__(self, filename):
        # import the dataframe
        df = pd.read_csv(filename)

        # turn the dataframe into a bunch of sets
        self.sets = [SpinSet(row['min_rpm'], row['max_rpm'], row['rpe'],
                             row['minutes'], row['seconds']) for index, row in df.iterrows()]

    # make a function that tells you to do an entire workout (from sets)
    def coach(self):
        # iterate over all the sets
        for spinset in self.sets:
            # output the set
            print(spinset)

            # output a live timer
            countdown(spinset.total_seconds)

            # return to the next line
            print('\n')
