class RepairStatus:
    def __init__(self, stuNo, stuPassWord, address, description, telephone):
        self.stuNo = stuNo
        self.stuPassWord = stuPassWord
        self.address = address
        self.description = description
        self.telephone = telephone

    def getNo(self):
        return self.stuNo

    def setNo(self, No):
        self.stuNo = No

    def getPassWord(self):
        return self.stuPassWord

    def setPassWord(self, PassWord):
        self.stuPassWord = PassWord

    def getAddress(self):
        return self.address

    def setAddress(self, Address):
        self.address = Address

    def getDescription(self):
        return self.description

    def setDescription(self, Description):
        self.description = Description

    def getTelephone(self):
        return self.telephone

    def SetTelephone(self, TelePhone):
        self.telephone = TelePhone


class RepairView:
    def printRepairDetails(self, stuNo, stuPassWord, address, description, telephone):
        print("Repair:")
        print("stuNo:{0}".format(stuNo))
        print("stuPassWord:{0}".format(stuPassWord))
        print("address:{0}".format(address))
        print("description:{0}".format(description))
        print("telephone:{0}".format(telephone))


class RepairController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def SetOrderStuNo(self, No):
        self.model.setNo(No)

    def SetOrderStuPassword(self, password):
        self.model.setPassWord(password)

    def setOrderStuAddress(self, address):
        self.model.setAddress(address)

    def setOrderDescription(self, description):
        self.model.setDescription(description)

    def setOrderTelephont(self, Telephone):
        self.model.SetTelephone(Telephone)

    def updateView(self):
        self.view.printRepairDetails(self.model.getNo(), self.model.getPassWord(),
                                     self.model.getAddress(), self.model.getDescription(), self.model.getTelephone())


# main
NewRepairOrder = RepairStatus(1, "2", 3, 4, 5)

NewView = RepairView()
NewController = RepairController(NewRepairOrder, NewView)
NewController.updateView()

NewController.SetOrderStuNo(12)
NewController.updateView()
