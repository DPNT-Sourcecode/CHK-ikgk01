
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
                    offer_counter = count
                    for offer, value in sorted(multibuys[sku].items(), reverse=True):
                        multiple = offer_counter // offer
                        offer_counter = offer_counter - multiple * offer
                        total += multiple * value
                        remainder = count % offer
                        total += remainder * prices[sku]
                else:
                    total += count * prices[sku]
        return total


print(CheckoutSolution().checkout("AAAAABBB"))