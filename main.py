'''Entry point'''

# from controllers.bruteforce import BruteForce
from controllers.optimized import Optimized
from views.view import View
import time


def main():
    # bruteForce version
    # controller = BruteForce()
    # start = time.time()
    # resultat = controller.bruteForce(controller.recordActions())
    # end = time.time()
    # View.showTimeOfExecution(start, end)
    # View.showThebestActionsCombo(resultat)

    # optimized version
    controller = Optimized()
    start = time.time()
    resultat = controller.OptimizedBruteForce(controller.findBestRateActions())
    end = time.time()
    View.showTimeOfExecution(start, end)
    View.showThebestActionsCombo(resultat)
    

if __name__ == "__main__":
    main()
