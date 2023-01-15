from PyQt5 import QtWidgets
from run import Ui_MainWindow
import sys
import ethSol

Tb = ethSol.Table()



class Main(QtWidgets.QMainWindow):
    MaxID = 0



    def createOrder(self):
        NameT =self.ui.lineEdit_6.text()
        Name = self.ui.lineEdit_7.text()
        SurName = self.ui.lineEdit_8.text()
        ThirdName = self.ui.lineEdit_9.text()

        if(NameT == ""):
            return
        if (Name == ""):
            return
        if (SurName == ""):
            return
        if (ThirdName == ""):
            return


        DocNum = self.ui.lineEdit_11.text()
        if (DocNum == ""):
            return



        DocNum = int(DocNum)
        PhoneNum = self.ui.lineEdit_12.text()
        Email = self.ui.lineEdit_13.text()

        if (PhoneNum == ""):
            return
        if (Email == ""):
            return

        Ddd = self.ui.lineEdit_17.text()
        Dmm = self.ui.lineEdit_18.text()
        Dyy = self.ui.lineEdit_19.text()

        if (Ddd == ""):
            return
        if (Dmm == ""):
            return
        if (Dyy == ""):
            return

        Ddate = Ddd + '.' + Dmm + '.' + Dyy

        Rdd = self.ui.lineEdit_20.text()
        Rmm = self.ui.lineEdit_21.text()
        Ryy = self.ui.lineEdit_22.text()

        if (Rdd == ""):
            return
        if (Rmm == ""):
            return
        if (Ryy == ""):
            return

        Rdate = Rdd + '.' + Rmm + '.' + Ryy

        if Tb.findTour(NameT) == 99999:
            return

        Price = 0


        for i in range(0,self.ui.tableWidget.rowCount()):
            if NameT == ((self.ui.tableWidget.item(i,1).text())):
                Price = int(self.ui.tableWidget.item(i,4).text())
                break



        Tb.create_order(NameT,Name,SurName,ThirdName,"Passport",DocNum,PhoneNum,Email,Ddate,Rdate,Price/2)

        itemTourName = QtWidgets.QTableWidgetItem(str(NameT))
        itemName = QtWidgets.QTableWidgetItem(str(Name))
        itemSurName = QtWidgets.QTableWidgetItem(str(SurName))
        itemThirdName = QtWidgets.QTableWidgetItem(str(ThirdName))
        itemDocType = QtWidgets.QTableWidgetItem(str("Passport"))
        itemDocNum = QtWidgets.QTableWidgetItem(str(DocNum))
        itemPhoneNum = QtWidgets.QTableWidgetItem(str(PhoneNum))
        itemEmail = QtWidgets.QTableWidgetItem(str(Email))
        itemDdate = QtWidgets.QTableWidgetItem(str(Ddate))
        itemRdate = QtWidgets.QTableWidgetItem(str(Rdate))
        itemPrice = QtWidgets.QTableWidgetItem(str(Price))

        columCount = 10
        self.ui.tableWidget_2.setColumnCount(columCount)
        rowCount = self.ui.tableWidget_2.rowCount()
        rowCount += 1
        self.ui.tableWidget_2.setRowCount(rowCount)

        self.ui.tableWidget_2.setItem(rowCount - 1, 0, itemTourName)
        self.ui.tableWidget_2.setItem(rowCount - 1, 1, itemName)
        self.ui.tableWidget_2.setItem(rowCount - 1, 2, itemSurName)
        self.ui.tableWidget_2.setItem(rowCount - 1, 3, itemThirdName)
        self.ui.tableWidget_2.setItem(rowCount - 1, 4, itemDocType)
        self.ui.tableWidget_2.setItem(rowCount - 1, 5, itemDocNum)
        self.ui.tableWidget_2.setItem(rowCount - 1, 6, itemPhoneNum)
        self.ui.tableWidget_2.setItem(rowCount - 1, 7, itemEmail)
        self.ui.tableWidget_2.setItem(rowCount - 1, 8, itemDdate)
        self.ui.tableWidget_2.setItem(rowCount - 1, 9, itemRdate)

        #self.ui.tableWidget_2.setHorizontalHeaderItem(0, itemName)
        self.ui.tableWidget_2.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem(str("Tour Name")))
        self.ui.tableWidget_2.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem(str("Name")))
        self.ui.tableWidget_2.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem(str("Surname")))
        self.ui.tableWidget_2.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem(str("Thirdname")))
        self.ui.tableWidget_2.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem(str("Document Type")))
        self.ui.tableWidget_2.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem(str("Document Number")))
        self.ui.tableWidget_2.setHorizontalHeaderItem(6, QtWidgets.QTableWidgetItem(str("Phone Number")))
        self.ui.tableWidget_2.setHorizontalHeaderItem(7, QtWidgets.QTableWidgetItem(str("Email")))
        self.ui.tableWidget_2.setHorizontalHeaderItem(8, QtWidgets.QTableWidgetItem(str("Departure Date")))
        self.ui.tableWidget_2.setHorizontalHeaderItem(9, QtWidgets.QTableWidgetItem(str("Return Date")))









    def deleteTour(self):
        _id = self.ui.lineEdit_5.text()

        tl = -1
        id_tab = -1
        gt = self.ui.tableWidget.rowCount()
        for i in range(0,gt):
            if self.ui.tableWidget.item(i,0).text() == str(_id):
                tl = i
                id_tab = i
                break

        if(tl != -1):
            Tb.delete_tour(_id)
            self.ui.tableWidget.removeRow(tl)

            it0 = QtWidgets.QTableWidgetItem(str("ID"))
            it1 = QtWidgets.QTableWidgetItem(str("Название тура"))
            it2 = QtWidgets.QTableWidgetItem(str("Название тур-оператора"))
            it3 = QtWidgets.QTableWidgetItem(str("Общий доход"))
            it4 = QtWidgets.QTableWidgetItem(str("Цена"))
            it5 = QtWidgets.QTableWidgetItem(str("Скидка"))

            self.ui.tableWidget.setHorizontalHeaderItem(0, it0)
            self.ui.tableWidget.setHorizontalHeaderItem(1, it1)
            self.ui.tableWidget.setHorizontalHeaderItem(2, it2)
            self.ui.tableWidget.setHorizontalHeaderItem(3, it3)
            self.ui.tableWidget.setHorizontalHeaderItem(4, it4)
            self.ui.tableWidget.setHorizontalHeaderItem(5, it5)

        #_id = int(_id)
        #_id -= 1

        #print(_id)


    def reloadOrder(self):
        countTour = Tb.seeTableID()
        #print(countTour)

        itemTourName = QtWidgets.QTableWidgetItem(str(""))
        itemName = QtWidgets.QTableWidgetItem(str(""))
        itemSurName = QtWidgets.QTableWidgetItem(str(""))
        itemThirdName = QtWidgets.QTableWidgetItem(str(""))
        itemDocType = QtWidgets.QTableWidgetItem(str(""))
        itemDocNum = QtWidgets.QTableWidgetItem(str(""))
        itemPhoneNum = QtWidgets.QTableWidgetItem(str(""))
        itemEmail = QtWidgets.QTableWidgetItem(str(""))
        itemDdate = QtWidgets.QTableWidgetItem(str(""))
        itemRdate = QtWidgets.QTableWidgetItem(str(""))
        itemPrice = QtWidgets.QTableWidgetItem(str(""))

        for i in range(0, countTour):
            columCount = 10
            self.ui.tableWidget_2.setColumnCount(columCount)
            rowCount = self.ui.tableWidget_2.rowCount()

            data = Tb.get_table(i)
            #print(data)

            bl = True
            index = 1
            for tm in data:
                if index == 1:
                    if tm == "":
                        bl = False
                    index += 1
                elif index == 2:
                    if tm == "":
                        bl = False
                    index += 1
                elif index == 3:
                    if tm == "":
                        bl = False
                    index += 1

            tournm = ""
            if bl:
                rowCount += 1
                self.ui.tableWidget_2.setRowCount(rowCount)
                index = 0
                for tm in data:
                    self.ui.tableWidget_2.setItem(i,index,QtWidgets.QTableWidgetItem(str(tm)))
                    index+=1

            self.ui.tableWidget_2.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem(str("Tour Name")))
            self.ui.tableWidget_2.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem(str("Name")))
            self.ui.tableWidget_2.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem(str("Surname")))
            self.ui.tableWidget_2.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem(str("Thirdname")))
            self.ui.tableWidget_2.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem(str("Document Type")))
            self.ui.tableWidget_2.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem(str("Document Number")))
            self.ui.tableWidget_2.setHorizontalHeaderItem(6, QtWidgets.QTableWidgetItem(str("Phone Number")))
            self.ui.tableWidget_2.setHorizontalHeaderItem(7, QtWidgets.QTableWidgetItem(str("Email")))
            self.ui.tableWidget_2.setHorizontalHeaderItem(8, QtWidgets.QTableWidgetItem(str("Departure Date")))
            self.ui.tableWidget_2.setHorizontalHeaderItem(9, QtWidgets.QTableWidgetItem(str("Return Date")))






    def reload(self):
        countTour = Tb.seeToursID()

        itemTourId = QtWidgets.QTableWidgetItem(str(""))
        itemTourName = QtWidgets.QTableWidgetItem(str(""))
        itemOperatorName = QtWidgets.QTableWidgetItem(str(""))
        itemProfit = QtWidgets.QTableWidgetItem(str(""))
        itemPrice = QtWidgets.QTableWidgetItem(str(""))
        itemDiscount = QtWidgets.QTableWidgetItem(str(""))

        for i in range(0, countTour):
            columCount = 6
            self.ui.tableWidget.setColumnCount(columCount)
            rowCount = self.ui.tableWidget.rowCount()

            data = Tb.get_tours(i)

            bl = True
            index = 1
            for tm in data:
                if index == 1:
                    if tm == "":
                        bl = False
                    index += 1
                elif index == 2:
                    if tm == "":
                        bl = False

                    index += 1

            tournm = ""
            if bl:
                rowCount += 1
                self.ui.tableWidget.setRowCount(rowCount)
                index = 1
                for tm in data:
                    # print(tm)
                    if index == 1:
                        tournm = tm
                        itemTourName = QtWidgets.QTableWidgetItem(str(tm))
                        # self.ui.tableWidget.setItem(rowCount - 1, 0, itemTourName)

                        index += 1
                    elif index == 2:
                        itemOperatorName = QtWidgets.QTableWidgetItem(str(tm))

                        index += 1
                    elif index == 3:
                        itemProfit = QtWidgets.QTableWidgetItem(str(tm))

                        index += 1
                    elif index == 4:
                        itemPrice = QtWidgets.QTableWidgetItem(str(tm))

                        index += 1
                    elif index == 5:
                        if (tm == True):
                            itemDiscount = QtWidgets.QTableWidgetItem(str("✓"))
                            index += 1
                        else:
                            itemDiscount = QtWidgets.QTableWidgetItem(str("-"))
                            index += 1

                tmpID = Tb.findTour(tournm)
                itemTourId = QtWidgets.QTableWidgetItem(str(tmpID))

                self.ui.tableWidget.setItem(rowCount - 1, 0, itemTourId)
                self.ui.tableWidget.setItem(rowCount - 1, 1, itemTourName)
                self.ui.tableWidget.setItem(rowCount - 1, 2, itemOperatorName)
                self.ui.tableWidget.setItem(rowCount - 1, 3, itemProfit)
                self.ui.tableWidget.setItem(rowCount - 1, 4, itemPrice)
                self.ui.tableWidget.setItem(rowCount - 1, 5, itemDiscount)

            it0 = QtWidgets.QTableWidgetItem(str("ID"))
            it1 = QtWidgets.QTableWidgetItem(str("Название тура"))
            it2 = QtWidgets.QTableWidgetItem(str("Название тур-оператора"))
            it3 = QtWidgets.QTableWidgetItem(str("Общий доход"))
            it4 = QtWidgets.QTableWidgetItem(str("Цена"))
            it5 = QtWidgets.QTableWidgetItem(str("Скидка"))

            self.ui.tableWidget.setHorizontalHeaderItem(0, it0)
            self.ui.tableWidget.setHorizontalHeaderItem(1, it1)
            self.ui.tableWidget.setHorizontalHeaderItem(2, it2)
            self.ui.tableWidget.setHorizontalHeaderItem(3, it3)
            self.ui.tableWidget.setHorizontalHeaderItem(4, it4)
            self.ui.tableWidget.setHorizontalHeaderItem(5, it5)







    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #self.preload()
        self.ui.pushButton.clicked.connect(self.createNewTour)
        self.ui.pushButton_2.clicked.connect(self.deleteTour)
        self.ui.pushButton_3.clicked.connect(self.createOrder)


        #print(Tb.findTour("Panama"))

        ind = 0
        tf = Tb.accounts()
        for tm in tf:
            self.ui.comboBox.addItem(str(tm))
            ind+=1
        #print(tf)

        self.reload()
        self.reloadOrder()
            #print(data)





        #print(countTour)


    def createNewTour(self):
        tourname = self.ui.lineEdit_2.text()
        operatorname = self.ui.lineEdit.text()
        profit = self.ui.lineEdit_4.text()
        price = self.ui.lineEdit_3.text()
        chek = self.ui.checkBox.isChecked()

        if (tourname == ""):
            return
        if (operatorname == ""):
            return
        if (profit == ""):
            return
        if (price == ""):
            return



        Tb.add_tour(str(tourname),str(operatorname),int(profit),int(price),chek)


        #print(chek)

        # self.ui.tableView.setRowCo
        #
        # a = self.ui.tableView.rowCount()
        # a+=1



        itemTourName = QtWidgets.QTableWidgetItem(str(tourname))
        itemOperatorName = QtWidgets.QTableWidgetItem(str(operatorname))
        itemProfit = QtWidgets.QTableWidgetItem(str(profit))
        itemPrice = QtWidgets.QTableWidgetItem(str(price))
        if(chek == True):
            itemDiscount = QtWidgets.QTableWidgetItem(str("✓"))
        else:
            itemDiscount = QtWidgets.QTableWidgetItem(str("-"))





        columCount = 6
        self.ui.tableWidget.setColumnCount(columCount)
        rowCount = self.ui.tableWidget.rowCount()
        print(rowCount)
        #print(MaxID)
        #print(MaxID = 1)
        #MaxID = 0
        if rowCount > 0:
            self.MaxID = int(self.ui.tableWidget.item(rowCount-1,0).text())
        self.MaxID+=1
        #print(MaxID)
        itemID = QtWidgets.QTableWidgetItem(str(self.MaxID))

        rowCount+= 1
        self.ui.tableWidget.setRowCount(rowCount)

        self.ui.tableWidget.setItem(rowCount-1, 0, itemID)
        self.ui.tableWidget.setItem(rowCount-1, 1, itemTourName)
        self.ui.tableWidget.setItem(rowCount-1, 2, itemOperatorName)
        self.ui.tableWidget.setItem(rowCount-1, 3, itemProfit)
        self.ui.tableWidget.setItem(rowCount-1, 4, itemPrice)
        self.ui.tableWidget.setItem(rowCount-1, 5, itemDiscount)

        it0 = QtWidgets.QTableWidgetItem(str("ID"))
        it1 = QtWidgets.QTableWidgetItem(str("Название тура"))
        it2 = QtWidgets.QTableWidgetItem(str("Название тур-оператора"))
        it3 = QtWidgets.QTableWidgetItem(str("Общий доход"))
        it4 = QtWidgets.QTableWidgetItem(str("Цена"))
        it5 = QtWidgets.QTableWidgetItem(str("Скидка"))

        self.ui.tableWidget.setHorizontalHeaderItem(0, it0)
        self.ui.tableWidget.setHorizontalHeaderItem(1, it1)
        self.ui.tableWidget.setHorizontalHeaderItem(2, it2)
        self.ui.tableWidget.setHorizontalHeaderItem(3, it3)
        self.ui.tableWidget.setHorizontalHeaderItem(4, it4)
        self.ui.tableWidget.setHorizontalHeaderItem(5, it5)


        # if(chek == False):
        #     it5 = QtWidgets.QTableWidgetItem(str("-"))
        #     self.ui.tableWidget.setHorizontalHeaderItem(4, it5)
        # else:
        #     it5 = QtWidgets.QTableWidgetItem(str("✓"))
        #     self.ui.tableWidget.setHorizontalHeaderItem(4, it5)

        #self.ui.tableWidget.setItem(0, 0, item)

       #self.ui.tableWidget.setText()

        #self.ui.tableWidget.setData(0,0,"LOL")
        #self.ui.tableWidget.setItem(1,1,)
        #self.ui.tableWidget.setCellWidget(rowCount,0,tourname)
        #self.ui.tableWidget.setItem(rowCount, 1, tourname)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Main()
    myapp.show()
    sys.exit(app.exec_())