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
                                                                     item.total))
            totalCost += int(item.total)
        print("Итого: ", totalCost)


class Lesson:
    def __init__(self, name, duration, cost, paymentType):
        self.__name = name
        self.__duration = duration
        self.__paymentType = paymentType.type
        self.__cost = cost
        self.__type_lesson = None
        self.total = paymentType.total(self.cost, self.duration)

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

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, total):
        self.__total = total

    def get_info(self):
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(self.name,
                                                                 self.type_lesson,
                                                                 self.duration,
                                                                 self.paymentType,
                                                                 self.cost,
                                                                 self.total))


class Lecture(Lesson):
    def __init__(self, name, duration, cost, paymentType):
        super(Lecture, self).__init__(name, duration, cost, paymentType)
        self.type_lesson = "Лекция"


class Seminar(Lesson):
    def __init__(self, name, duration, cost, paymentType):
        super(Seminar, self).__init__(name, duration, cost, paymentType)
        self.type_lesson = "Семинар"


class Payment:
    def __init__(self):
        self.__cost = 0
        self.__duration = 0

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration

    def total(self, cost, duration):
        return None


class TimePayment(Payment):
    def __init__(self):
        super(TimePayment, self).__init__()
        self.type = "Повременная"

    def total(self, cost, duration):
        return cost*duration


class FixedPayment(Payment):
    def __init__(self):
        super(FixedPayment, self).__init__()
        self.type = "Фиксированная"

    def total(self, cost, duration):
        return cost


tp = TimePayment()
fp = FixedPayment()

html = Lecture("HTML", 10, 900, tp)
js = Seminar("JS", 10, 800, fp)
css = Seminar("CSS", 10, 350, fp)
php = Lecture("PHP", 10, 450, tp)

list1 = List()
list2 = List()
list1.add(html, css)
list2.add(html, css, js)

list2.show()