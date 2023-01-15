import web3
import json

class Table():
    geth_url = "HTTP://127.0.0.1:8545"
    w3 = web3.Web3(web3.HTTPProvider(geth_url))

    #w3.eth.defaultAccount = w3.eth.accounts[1]

    #buyerAddr = '0xF8A82CDA541EA9f8C3C1F1fA0c72F2Ba41c080C6'
    buyerAddr = w3.eth.accounts[1]
    #owner = '0xC85830A911Aae5E382D1D4A41a314495de6dCD08'
    owner = w3.eth.accounts[0]
    #add = w3.eth.rfr
    address_contract = '0x1Aa29aE6c283874675829c59Db92692ba6130F56'
    #address_contract = web3.Web3.toChecksumAddress('0x074eF1e70Ce1cEC79984ca3F5cce957CE6432999')


    with open("ABI.json", "r") as file:
        abi = json.load(file)


    contract = w3.eth.contract(address=address_contract, abi= abi)

    def __init__(self):
        pass

    def accounts(self):
        return self.w3.eth.accounts


    def seeToursID(self):
        return self.contract.functions.seeToursID().call()


    def seeTableID(self):
        return self.contract.functions.seeTableID().call()

    def getBalance(self, address):
        address = web3.Web3.toChecksumAddress(address)
        return self.w3.eth.getBalance(address)

    def get_tours(self, id):
        return self.contract.functions.tours(id).call()

    def get_table(self,id):
        return self.contract.functions.tbl(id).call()

    def findTour(self,Name):
        return self.contract.functions.findTour(Name).call()
        #self.w3.eth.waitForTransactionReceipt(tx)
        #return tx


    def setNewEmail(self,id, DpDate):
        tx = self.contract.functions.setNewEmail(id,DpDate).transact({'from': self.owner})
        self.w3.eth.waitForTransactionReceipt(tx)


    def setNewReturnDate(self,id, DpDate):
        tx = self.contract.functions.setNewReturnDate(id,DpDate).transact({'from': self.owner})
        self.w3.eth.waitForTransactionReceipt(tx)


    def setNewDepartureDate(self,id, DpDate):
        tx = self.contract.functions.setNewDepartureDate(id,DpDate).transact({'from': self.owner})
        self.w3.eth.waitForTransactionReceipt(tx)

    def increaseProfit(self, Name, plus):
        tx = self.contract.functions.IncreaseProfit(Name,plus).transact({'from': self.owner})
        self.w3.eth.waitForTransactionReceipt(tx)


    def delete_tour(self,nm):
        nm = int(nm)
        tx = self.contract.functions.delete_tour(nm).transact({'from': self.owner})
        self.w3.eth.waitForTransactionReceipt(tx)

    def add_tour(self,NameTour,NameOperator,Profit,prf,ch):
        tx = self.contract.functions.add_tour(NameTour,NameOperator,Profit,prf,ch).transact({'from': self.owner})
        self.w3.eth.waitForTransactionReceipt(tx)


    def create_order(self,NameTour, Name, Surname, Thirdname, DocType, DocNum, PhoneNum, Email, DepartureDate, ReturnDate, price):
        tx = self.contract.functions.createOrder(NameTour, Name, Surname, Thirdname, DocType, DocNum, PhoneNum, Email, DepartureDate, ReturnDate).transact({'from': self.buyerAddr, 'value': int(price)})
        self.w3.eth.waitForTransactionReceipt(tx)


#Tb = Table()
#print(Tb.get_table(0))
#Tb.create_order("Port","Kirill","Kuzmenko","Serg","Passport",15678,"+791888","kkuz@sfed.ru","15.08.2003","23.08.2003",1234)


# print(Tb.get_tours(0))
# Tb.increaseProfit('Panama', 25000)
# print(Tb.get_tours(0))
#Tb.get_tours(0);
#print (Tb.getBalance(0xe4Ade3e21c7591435b6f83Dc4B644068b20f5D00))

