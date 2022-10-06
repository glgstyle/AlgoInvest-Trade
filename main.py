'''Entry point'''

from controllers.bruteforce import BruteForce
from controllers.optimized import Optimized
from views.view import View
import time
import tracemalloc


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
    # tracemalloc.start()
    start = time.time()
    actions = controller.recordActions()
    resultat = controller.OptimizedBruteForce(500, actions)
    end = time.time()
    View.showTimeOfExecution(start, end)
    View.showThebestActionsCombo(resultat)
    # print(tracemalloc.get_traced_memory())
    

if __name__ == "__main__":
    main()

