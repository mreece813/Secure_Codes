class Bag:
    def __init__(self):
             self.__contents = {}
    def insert(self, item):
              self.__contents[item] = self.__contents.get(item, 0) + 1
    def erase_one(self, item):
               if item in self.__contents:
                    self.__contents[item] = self.__contents[item] - 1
                    if self.__contents[item] == 0:
                        del self.__contents[item]
    def count(self, item):
                if item in self.__contents:
                    return self.__contents[item]
                else:
                    return 0
    def items(self):
              return list(self.__contents.keys())
    def __str__(self):
        bag_str = ""
        for item in self.__contents:
            for i in range(self.__contents[item]):
                bag_str = bag_str + str(item) + ' '
        return bag_str

    def __repr__(self):
        return str(self)

    #from bag import Bag

    def remove_item(B, item):
        for i in range(B.count(item)):
            B.erase_one(item)

    def remove_repeats(B):
        for el in B.items():
            num_el = B.count(el)
            for k in range(num_el - 1):
                B.erase_one(el)

    def mode(B):
        Mlist = []
        mx = 0
        for el in B.items():
            if B.count(el) > mx:
                mx = B.count(el)
        for el in B.items():
            if B.count(el) == mx:
                Mlist.append(el)
        return Mlist

    def union(B1, B2):
        U = Bag()
        for el in B1.items():
            for i in range(B1.count(el)):
                U.insert(el)
        for el in B2.items():
            for i in range(B2.count(el)):
                U.insert(el)
        return U
        
    def intersection(B1, B2):
        I = Bag()
        for el in B1.items():
            common_count = min(B1.count(el), B2.count(el))
            for i in range(common_count):
                I.insert(el)
        return I
