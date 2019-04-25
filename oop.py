class List:
    def __init__(self):
        self.name = []

    def __str__(self):
        for item in self.name:
            return str(item)

    def add(self, *args):
        for item in args:
            self.name.append(item)

    def show(self):
        totalCost = 0
        for item in self.name:
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(item.name,
                                                                     item.type_lesson,
                                                                     item.duration,
                                                                     item.paymentType,
                                                                     item.cost,
                                                                     self.total_cost(item.duration, item.cost)))
            totalCost += int(self.total_cost(item.duration, item.cost))
        print("Итого: ", totalCost)

    @staticmethod
    def total_cost(duration, cost):
        return duration * cost


class Lesson:
    def __init__(self, name, paymentType, duration):
        self.__name = name
        self.__duration = duration
        self.__paymentType = paymentType.type
        self.__cost = paymentType.cost
        self.__type_lesson = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration

    @property
    def paymentType(self):
        return self.__paymentType

    @paymentType.setter
    def paymentType(self, paymentType):
        self.__paymentType = paymentType

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    @property
    def type_lesson(self):
        return self.__type_lesson

    @type_lesson.setter
    def type_lesson(self, type_lesson):
        self.__type_lesson = type_lesson

    def get_cost(self):
        total_cost = self.duration * self.cost
        return total_cost

    def get_info(self):
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(self.name,
                                                                 self.type_lesson,
                                                                 self.duration,
                                                                 self.paymentType,
                                                                 self.cost,
                                                                 self.get_cost()))


class Lecture(Lesson):
    def __init__(self, name, paymentType, duration):
        super(Lecture, self).__init__(name, paymentType, duration)
        self.type_lesson = "Лекция"


class Seminar(Lesson):
    def __init__(self, name, paymentType, duration):
        super(Seminar, self).__init__(name, paymentType, duration)
        self.type_lesson = "Семинар"


class Payment:
    def __init__(self, cost):
        self.__cost = cost

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost


class TimePayment(Payment):
    def __init__(self, cost):
        super(TimePayment, self).__init__(cost)
        self.type = "Повременная"


class FixedPayment(Payment):
    def __init__(self, cost):
        super(FixedPayment, self).__init__(cost)
        self.type = "Фиксированная"
        self.duration = 1
