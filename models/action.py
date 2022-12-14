'''An action'''


class Action:

    def __init__(self, name="", cost=0, profit=0, is_preprocessed=False):
        self.name = name
        # used for optimized algorithm
        if is_preprocessed:
            self.cost = int(float(cost) * 100)
            self.profit = int(float(profit) * 100)
        # used for bruteforce algorithm
        else:
            self.cost = float(cost)
            self.profit = float(profit)

    # Getters

    @property
    def name(self):
        return self._name

    @property
    def cost(self):
        return self._cost

    @property
    def profit(self):
        return self._profit

    # Setters

    @name.setter
    def name(self, name):
        self._name = name

    @cost.setter
    def cost(self, cost):
        self._cost = cost

    @profit.setter
    def profit(self, profit):
        self._profit = profit

    # return the name instead of action.object
    def __str__(self):
        return f'{self.name}, {self.cost}, {self.profit}'

    # return the action if it's in a list
    def __repr__(self):
        return self.__str__()
