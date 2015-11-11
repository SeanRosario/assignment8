__author__ = 'SeansMBP'

import numpy as np

cumu_ret = dict()
daily_ret = dict()

def take_inputs_from_user():
    try:
        "Taking inputs"
        positions = []
        user_input = 0
        count = 0
        while user_input!="done":
            print """enter the position value or type "done" when finished"""
            user_input = raw_input()

            if user_input!="done":
                positions.insert(count,int(user_input))
            count = count +1
        print positions

        print "How many times would you like to randomly repeat the test?",
        num_trials = int(raw_input())

    except KeyboardInterrupt:
        print "Program terminated due to Keyboard Interrupt"
    except IOError:
        print "Error in input"
    except EOFError:
        print "EOFError"



def the_trials(num_trials,position):
    try:
        for trial in range(num_trials):
            cumu_ret[trial]=0
            position_value = float(1000/position)
            for i in range(position):
                cumu_ret[trial] = float(cumu_ret[trial]) + float(odds(position_value))

            daily_ret[trial] = float(cumu_ret[trial]/1000) - 1.0

        return daily_ret
    except:
        raise


def odds(value):
    if (np.random.randint(1, high=101))>=49:
        return value*2
    else:
        return 0
