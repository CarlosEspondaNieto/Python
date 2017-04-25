class Number:
    def __init__(self, number):
        """The constructor of a Number
        """
        try:
            self.number = float(number)
        except ValueError as e:
            print(e)
            print("That's not a number!")
            raise ValueError  # Programatically raising an exception
        self.factorial = self.__factorial()

    def __str__(self):
        """__unicode__ in pyton 2.7
        """
        return str(self.number)

    def __factorial(self):
        """Private method: Returns the factorial of a number
        """
        _, number = 1, self.number  # It's common to use an underscore
        while number >= 1:          # for a value that you're going to throw
            _ = _ * number
            number = number - 1
        return _

    @property
    def as_dict(self):
        """Returns an instance of the object as a
        dictionary
        """
        return self.__dict__  # __dict__ magic function

    def get_factorial(self):
        """Gets and print the factorial of the number
        """
        print("The factorial of {} is {}".format(
            self.number, self.__factorial()))  # Be careful of indentation

    def calculator(self, operation, another_number):
        """It allows to calculate basic arithmetic operations
        """
        operations_dict = {
            'times': '*',
            'plus': '+',
            'divide': '/',
            'minus': '-'
        }

        try:
            another_number = float(another_number)
        except ValueError:
            print("That's not a number!")

        if operation in operations_dict:
            string_to_eval = '%s%s%s' % (self.number,
                                         operations_dict.get(operation),
                                         another_number)
            print(string_to_eval)
            return eval(string_to_eval)
        else:
            print("It's not possible to perform that operation")
