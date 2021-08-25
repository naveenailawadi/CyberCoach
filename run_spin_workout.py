from core import SpinCoach
import sys


# make a main function
def main(filename):
    # load the file with the coach
    coach = SpinCoach(filename)

    # run the workout
    coach.coach()


if __name__ == '__main__':
    main(sys.argv[1])
