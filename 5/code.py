"""Program for implementations of Higher Order functions"""

class HOFImplementations:
    """Different implementations of Higher Order functions"""

    @staticmethod
    def func_as_args():
        """Passing functions as arguments"""
        elements = [1,2,3,4,5,6,7,8,9,10]
        elements = list(filter(lambda x: x % 2 == 0,elements))
        # filter is a higher order func taking condition func
        print(f"After applying filer: {elements}")
        print("-----------------------------")


    @staticmethod
    def ret_func_from_func():
        """Returning Functions from functions"""
        def power(exponent):
            def raiser(base):
                return base ** exponent
            return raiser

        square = power(2)
        cube = power(3)

        print(f"Sq: {square(5)}")
        print(f"Cube: {cube(3)}")
        print("-----------------------------")


    @staticmethod
    def decorators():
        """Decorators as HOFs"""
        def upppercase(func):
            def wrapper():
                result = func()
                return result.upper()
            return wrapper


        @upppercase
        def greet():
            return "hello"
        print(f"After upper transform: {greet()}")
        print("-----------------------------")


def main():
    """Call different implementations"""
    hofs = HOFImplementations()
    hofs.func_as_args()
    hofs.ret_func_from_func()
    hofs.decorators()

if __name__ == "__main__":
    main()
