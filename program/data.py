import re

class Bid:
    def __init__(self, identifier, price, goods_list):
        self.__identifier = identifier
        self.__price = price
        self.__goods_list = goods_list

    @classmethod
    def parse_line(cls, line):
        splited_line = re.split('\s+', line)
        identifier = int(splited_line[0])
        price = float(splited_line[1])
        goods_list = map(lambda x: int(x), splited_line[2:-2])
        return cls(identifier, price, goods_list)
        
    def identifier(self):
        return self.__identifier

    def price(self):
        return self.__price

    def goods_identifiers(self):
        return self.__goods_list

    def __str__(self):
        return "Bid identifier: "+str(self.identifier())+"\n"+"\tprice: "+str(self.price())+"\n\tgoods_identifiers: "+str(self.goods_identifiers())+"\n"

    def is_avalible(self, used_goods):
        return reduce(lambda acc, i: acc and not used_goods[i], self.goods_identifiers(), True)


class CAInstance:
    def __init__(self, goods_count, dummies_count, bids_list):
        self.goods_count = goods_count
        self.dummies_count = dummies_count
        self.bids_list = bids_list

    @classmethod
    def from_file(cls, file_name):
        lines = cls.__read_lines(file_name)
        goods, bids, dummies = None, None, None
        bids_list = []
        for line in lines:
            if line[0] == 'g':
                goods = int(line.split(' ')[1])
            elif line[0] == 'b':
                bids = int(line.split(' ')[1])
            elif line[0] == 'd':
                dummies = int(line.split(' ')[1])
            elif line[0] <= '9' and line[0] >= '0':
                bids_list.append(Bid.parse_line(line))
        return CAInstance(goods, dummies, bids_list)

    @classmethod
    def __read_lines(cls, file_name):
        f = open(file_name, "r")
        lines = f.readlines()
        f.close()
        return lines

    def goods_count(self):
        return self.goods_count

    def all_goods_count(self):
        return self.goods_count + self.dummies_count 

    def solution_size(self):
        return len(self.bids_list)
   
    def __str__(self):
        return "%s\n%s\n%s" % (self.goods_count, self.dummies_count, [str(x) for x in self.bids_list])

    def evaluate(self, permutation):
        used_goods = [False] * self.all_goods_count()
        total_price = 0.0
        for p in permutation:
            bid = self.bids_list[p]
            if bid.is_avalible(used_goods):
                total_price += bid.price()
                # updates used goods
                for i in bid.goods_identifiers():
                    used_goods[i] = True
        return total_price


instance = CAInstance.from_file("0000.txt")
print instance.evaluate([12, 11, 2,1,3,4,5,6,7,8,9,10, 0])

# should be True
#bid = Bid(1, 20, [0, 1])
#print bid.is_avalible([False, False, False, True])

# should be False
#print bid.is_avalible([True, False, False, True])
