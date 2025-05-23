from operator import itemgetter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        skus = list(skus)
        prices = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
            "E": 40,
            "F": 10,
            "G": 20,
            "H": 10,
            "I": 35,
            "J": 60,
            "K": 70,
            "L": 90,
            "M": 15,
            "N": 40,
            "O": 10,
            "P": 50,
            "Q": 30,
            "R": 50,
            "S": 20,
            "T": 20,
            "U": 40,
            "V": 50,
            "W": 20,
            "X": 17,
            "Y": 20,
            "Z": 21,
        }
        multibuys = {
            "A": {3: 130, 5: 200},
            "B": {2: 45},
            "H": {5: 45, 10: 80},
            "K": {2: 120},
            "P": {5: 200},
            "Q": {3: 80},
            "V": {2: 90, 3: 130},
        }
        bogoff = {
            "E": {"quantity": 2, "offer": "B", "number": 1},
            "F": {"quantity": 2, "offer": "F", "number": 1},
            "N": {"quantity": 3, "offer": "M", "number": 1},
            "R": {"quantity": 3, "offer": "Q", "number": 1},
            "U": {"quantity": 3, "offer": "U", "number": 1},
        }
        xfory = [
            {"quantity": 3, "list": ["S", "T", "X", "Y", "Z"], "price": 45}
        ]
        allowed_characters = list(prices.keys()) #+ [",", " "]
        if len(set(skus) - set(allowed_characters)) != 0:
            return -1
        total = 0
        skus_dict = {}
        for sku in skus:
            skus_dict[sku]=skus_dict.setdefault(sku, 0)+1
        for multibuy in xfory:
            multibuy_list = []
            for prod in multibuy["list"]:
                for sku in skus:
                    if sku == prod:
                        multibuy_list.append({"sku": sku, "cost": prices[sku]})
            multibuy_list.sort(key=itemgetter("cost"))
            while len(multibuy_list) >= multibuy["quantity"]:
                i = multibuy["quantity"]
                while i > 0:
                    itm = multibuy_list.pop()
                    skus_dict[itm["sku"]] -= 1
                    i -= 1
                total += multibuy["price"]
        for item, deal in bogoff.items():
            if item in skus_dict:
                num = skus_dict[item]
                cart_quantity = deal["quantity"] + 1 if item == deal["offer"] else deal["quantity"]

                if num >= cart_quantity:
                    offer_num = num
                    if deal["offer"] in skus_dict:
                        while offer_num >= cart_quantity:
                            skus_dict[deal["offer"]] = max(0, skus_dict[deal["offer"]] - deal["number"])
                            offer_num -= cart_quantity
        for sku, quantity in skus_dict.items():
            if quantity != 0:
                if sku in multibuys:
                    #if count >= multibuys[sku][0]:
                    multibuy_counter = quantity
                    for offer, value in sorted(multibuys[sku].items(), reverse=True):
                        multiple = multibuy_counter // offer
                        multibuy_counter = multibuy_counter - multiple * offer
                        total += multiple * value
                    total += multibuy_counter * prices[sku]
                else:
                    total += quantity * prices[sku]
        return total


print(CheckoutSolution().checkout("SSSTTS"))