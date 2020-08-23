class Car:
    def __init__(self, VehicleID, EngineSize):
        self.__VehicleID = str(VehicleID)
        self.__EngineSize = int(EngineSize)

    def SetPurchasePrice(self, price):
        self.__PurchasePrice = price

    def SetRegistration(self, Registration):
        self.__Registration = Registration

    def SetDateOfRegistration(self, DateOfRegistration):
        self.__DateOfRegistration = DateOfRegistration

    def GetVehicleID(self):
        return self.__VehicleID

    def GetRegistration(self):
        return self.__Registration

    def GetDateOfRegistration(self):
        return self.__DateOfRegistration

    def GetEngineSize(self):
        return self.__EngineSize

    def GetPurchasePrice(self):
        return self.__PurchasePrice


car = Car("asd", 12)

car.SetPurchasePrice(555)
car.SetRegistration
print(car.GetEngineSize())
