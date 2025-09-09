class MyClass:

    def registry(self) -> None:
        print("Start process")
        self.__verify()
        self.__verify_registry()
        self.__inser_data()
        print("End process")
    
    def __verify(self) -> None:
        print("Verify data")
    
    def __verify_registry(self) -> None:
        print("Verify registry")

    def __inser_data(self) -> None:
        print("Insert in database")

obj = MyClass()
obj.registry()