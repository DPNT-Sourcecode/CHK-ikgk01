
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        skus = list(skus)
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
            "E": {2: {"B": 1}} 
        }
        allowed_characters = list(prices.keys()) #+ [",", " "]
        if len(set(skus) - set(allowed_characters)) != 0:
            return -1
        total = 0
        skus_dict = {}
        for sku in skus:
            skus_dict[sku]=skus_dict.setdefault(sku, 0)+1
        for deal, value in bogoff.items():
            if deal in skus_dict:
                num = skus_dict[deal]
                if num >= value:
                    offer_num = num
                    while offer_num >= value:
                        a = skus_dict[value]
                        pass

                count = skus.count(offer)
                if count >= value:
                    multiple = count // value
                    while multiple > 0:
                        for sku in skus:
                            pass
                        multiple -= 1
                pass
        for sku in set(skus):
            count = skus.count(sku)
            if count != 0:
                if sku in multibuys:
                    #if count >= multibuys[sku][0]:
                    multibuy_counter = count
                    for offer, value in sorted(multibuys[sku].items(), reverse=True):
                        multiple = multibuy_counter // offer
                        multibuy_counter = multibuy_counter - multiple * offer
                        total += multiple * value
                        remainder = count % offer
                        total += remainder * prices[sku]
                else:
                    total += count * prices[sku]
                if sku in bogoff:
                    bogoff_counter = count
                    for offer, value in sorted(bogoff[sku].items(), reverse=True):
                        multiple = bogoff_counter // offer
                        bogoff_counter = bogoff_counter - multiple * offer
                        total
        return total


print(CheckoutSolution().checkout("AAAAABBBEE"))




