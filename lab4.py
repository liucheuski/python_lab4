# Kласс Airline: Пункт назначения, Номер рейса, Тип самолета, Время вылета, Дни недели.
# Функции- члены реализуют запись и считывание полей (проверка корректности).
# Создать список объектов. Вывести:
# a)	список рейсов для заданного пункта назначения;
# б) список рейсов для заданного дня недели;.

class Airline:
    lines_list = []
    days = ('Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su')

    def __init__(self, destination, flight, plane, flight_time, week_day):
        self.__destination = destination
        self.__flight = flight
        self.__plane = plane
        self.__flight_time = flight_time
        self.__week_day = week_day

    # dest getter&setter
    def get_destination(self):
        return self.__destination

    def set_destination(self, destination):
        if self.is_destination_exist(destination):
            print("\33[31m\033[1m {}".format('This destination has existed already.'))
            destination = int(input("\33[0m {}".format('Type another destination: ')))
            self.__destination = self.set_destination(destination)
        else:
            self.__destination = destination
            return destination

    # flight getter&setter
    def get_flight(self):
        return self.__flight

    def set_flight(self, flight):
        if self.is_flight_exist(flight):
            print("\33[31m\033[1m {}".format('This flight has existed already.'))
            flight = int(input("\33[0m {}".format('Type another flight: ')))
            self.set_flight(flight)
        else:
            self.__flight = flight
            return flight

    # plane getter&setter
    def get_plane(self):
        return self.__plane

    def set_plane(self, plane):
        self.__plane = plane

    # flight_time getter&setter
    def get_flight_time(self):
        return self.__flight_time

    def set_flight_time(self, flight_time):
        self.__flight_time = flight_time

    # week_day getter&setter
    def get_week_day(self):
        return self.__week_day

    def set_week_day(self, week_day):
        if self.is_corect_week_day(week_day):
            self.__week_day = week_day
            return week_day
        else:
            print(
                "\33[31m\033[1m {}".format('Wrong week day format, try once again. Choose one from ' + str(self.days)))
            week_day = str(input("\33[31m\033[1m {}".format('Type once again, just correct now: ')))
            self.__week_day = self.set_week_day(week_day)

    @classmethod
    def is_destination_exist(cls, destination):
        if len(Airline.get_lines_list()) != 0:
            for i in range(len(Airline.lines_list)):
                if Airline.lines_list[i].get_destination() == destination:
                    return True
                else:
                    return False
        return False

    @classmethod
    def is_flight_exist(cls, flight):
        if len(Airline.get_lines_list()) != 0:
            for i in range(len(Airline.lines_list)):
                if Airline.lines_list[i].get_flight() == flight:
                    return True
            else:
                return False
        return False

    @classmethod
    def is_corect_week_day(cls, week_day):
        if Airline.days.__contains__(week_day):
            return True
        else:
            return False

    @classmethod
    def find_all_by_destination(cls, destination):
        for i in range(len(Airline.lines_list)):
            if Airline.lines_list[i].get_destination() == destination:
                print(i)
            else:
                print("That's all what we can find")

    @classmethod
    def find_all_by_day(cls, day):
        for i in range(len(Airline.lines_list)):
            if Airline.lines_list[i].get_week_day == day:
                print(i)
            else:
                print("That's all what we can find")

    @staticmethod
    def get_lines_list():
        return Airline.lines_list

    @staticmethod
    def add_line_to_list(line):
        Airline.lines_list.append(line)


def create_line():
    destination = str(input('Type destination: '))
    flight = str(input('Type flight: '))
    plane = str(input("Type plane: "))
    flight_time = str(input("Type flight_time: "))
    week_day = str(input("Type week_day in format " + str(Airline.days)))
    line = Airline(destination, flight, plane, flight_time, week_day)
    line.set_destination(destination)
    line.set_flight(flight)
    line.set_plane(plane)
    line.set_flight_time(flight_time)
    line.set_week_day(week_day)
    Airline.add_line_to_list(line)


option = 1
while option != 0:
    print("\33[0m\033[1m {}".format('\nList of options. Please select one'))
    print('1 - Add a airline')
    print('2 - Find all airlines for a destination')
    print('3 - Find all airlines for a day')
    print('0 - Exit')
    option = int(input('\nEnter a number of option: '))
    if option == 1:
        print('Let\'s go...')
        create_line()
    elif option == 2:
        destination = str(input('\nType destination: '))
        Airline.find_all_by_destination(destination)
    elif option == 3:
        day = str(input('\nType day: '))

    elif option == 0:
        print("\033[36m {}".format('\nGood Bye!'))
        option = 0
    else:
        print("\033[33m {}".format('\nThis option is not present in the list, please try again'))
        print("\33[0m {}".format(''))
        continue
