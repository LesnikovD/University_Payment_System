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
        for item in self.name:
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(item.name,
                                                                     item.type_lesson,
                                                                     item.duration,
                                                                     item.paymentType,
                                                                     item.cost,
                                                                     item.totalCost))


class Lesson:
    def __init__(self, name, duration, paymentType, cost):
        self.__name = name
        self.__duration = duration
        self.__paymentType = paymentType
        self.__cost = cost
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


class Lecture(Lesson):
    def __init__(self, name, duration, paymentType, cost, totalCost):
        super(Lecture, self).__init__(name, duration, paymentType, cost)
        self.type_lesson = "Лекция"
        self.totalCost = int(totalCost)


class Seminar(Lesson):
    def __init__(self, name, duration, paymentType, cost, totalCost):
        super(Seminar, self).__init__(name, duration, paymentType, cost)
        self.type_lesson = "Семинар"
        self.totalCost = int(totalCost)


class Payment:
    def __init__(self, cost, duration):
        self.__cost = cost
        self.__duration = duration

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost


class TimePayment(Payment):
    def __init__(self, cost, duration):
        super(TimePayment, self).__init__(cost, duration)
        self.type = "Повременная"

    def totalCost(self):
        totalCost = int(self.cost * self.duration)
        return totalCost

    def showConditions(self):
        print("Стоимость занятия состовляет ", self.totalCost(), "в час")


class FixedPayment(Payment):
    def __init__(self, cost, duration):
        super(FixedPayment, self).__init__(cost, duration)
        self.type = "Фиксированная"

    def totalCost(self):
        totalCost = str(self.totalCost)
        return totalCost

    def showConditions(self):
        print("Стоимость занятия состовляет ", self.totalCost())


list1 = List()
hundred_per_hour = TimePayment(100, 10)
hundred_per_lesson = FixedPayment(100, 1)
hundred_per_hour.showConditions()

html = Lecture("HTML",
               hundred_per_hour.duration,
               hundred_per_hour.type,
               hundred_per_hour.cost,
               hundred_per_hour.totalCost())

list1.add(html)
list1.show()
