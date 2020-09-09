# exercise sale

class sale:
    business = ''
    product = ''
    buyer = ''
    contract = ''

    def __init__(self, business, buyer, contract):
        self.business = business
        self.buyer = buyer
        self.contract = contract

    def sold(self, business='sold'):
        print(business)
    
    def agreement(self):
        print(self.contract + 'assinatura de contrato')