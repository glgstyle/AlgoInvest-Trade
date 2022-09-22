'''Entry point'''

from controllers.bruteforce import BruteForce
from views.view import View
import time


def main():
    controller = BruteForce()
    start = time.time()
    resultat = controller.bruteForce(controller.recordActions())
    end = time.time()
    View.showTimeOfExecution(start, end)
    View.showThebestActionsCombo(resultat)
    

if __name__ == "__main__":
    main()
