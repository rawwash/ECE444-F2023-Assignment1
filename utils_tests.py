import utils

class Utils_Tests:
    def __init__(self, obj):
        self.utils_obj = obj
    
    #TESTING THE REVERSED INT FUNCTION
    def test_reverser(self):
        test_values = [432581, 0, -762819, "hi", 17.8]
        for val in test_values:
            try:
                print(self.utils_obj.reversed_int(val))
            except TypeError as e:
                print(f"Error with value {val}: {e}")
    
    #TESTING THE FORMATTER FUNCTION
    def test_formatter(self):
        test_values = [432581, 0, -762819, "hi", 17.8]
        for val in test_values:
            try:
                print(self.utils_obj.formatter(val))
            except TypeError as e:
                print(f"Error with value {val}: {e}")

if __name__ == "__main__":
    obj = utils.Utils()
    test_suite = Utils_Tests(obj)
    print("Testing Reversed")
    test_suite.test_reverser()
    print("\nTesting Formatter")
    test_suite.test_formatter()