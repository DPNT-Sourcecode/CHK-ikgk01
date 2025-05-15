
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
            "E": 40
        }
        multibuys = {
            "A": {3: 130, 5: 200},
            "B": {2: 45}
        }
        bogoff = {
            "E": {2: {"B": 2}} 
        }
        allowed_characters = list(prices.keys()) #+ [",", " "]
        if len(set(skus) - set(allowed_characters)) != 0:
            return -1
        total = 0
        for sku in set(skus):
            count = skus.count(sku)
            if count != 0:
                if sku in multibuys:
                    #if count >= multibuys[sku][0]:
                    for offer in sorted(multibuys[sku], reverse=True):
                        multiple = count // offer
                        count = count - multiple * offer[0]
                    total += multiple * multibuys[sku][1]
                    remainder = count % multibuys[sku][0]
                    total += remainder * prices[sku]
                else:
                    total += count * prices[sku]
        return total


print(CheckoutSolution().checkout("AAAABBB"))
