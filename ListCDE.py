class CirularNod:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class ListCDE:
    def __init__(self):
        self.first = None
        self.last = None

    def empty(self):
        if self.first == None:
            return True

        else:
            return False

    def finalAdd(self, data):
        if self.empty():
            self.first = self.last = CirularNod(data)

        else:
            verifiyer = self.last
            self.last = verifiyer.next = CirularNod(data)
            self.last.prev = verifiyer
        
        self.joinNodes()

    def joinNodes(self):
        self.first.prev = self.last
        self.last.next = self.first


    def printing(self):
        print("Complete list of elements: ")
        partner = self.first
        while(partner != None):
            print(partner.data)
            if(partner.next == self.first):
                return
            partner = partner.next

    
    def search(self, dataS):
        partner = self.first
        while(partner != None):
            #self.joinNodes()
            if (partner.data == dataS):
                print("Previous Number: ",partner.prev.data)
                print("Current Number: ", partner.data)
                print("Next Number: ",partner.next.data)

            if (partner.next == self.first):
                return
            partner = partner.next

            

