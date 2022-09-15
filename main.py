'''Entry point'''

from controllers.bruteforce import BruteForce


def main():
    controller = BruteForce()
    controller.recordActions()


if __name__ == "__main__":
    main()
