
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {
            "a": 50,
            "b": 30,
            "c": 20,
            "d": 15 
        }
        multibuys = {
            "a": (3, 130),
            "b": (2, 45)
        }
        allowed_characters = list(prices.keys()) + [",", " "]
        if len(set(skus.lower()) - set(allowed_characters)) != 0:
            return -1
        total = 0
        for sku in set(skus.lower()):
            count = skus.count(sku)
            if count != 0:
                if sku in multibuys.keys():
                    if count >= multibuys[sku][0]:
                        multiple = count // multibuys[sku][0]
                        total += multiple * multibuys[sku][1]
                        remainder = count % multibuys[sku][0]
                        total += remainder * prices[sku]
                    else:
                        total += count * prices[sku]
        return total

print(CheckoutSolution().checkout("aaa"))