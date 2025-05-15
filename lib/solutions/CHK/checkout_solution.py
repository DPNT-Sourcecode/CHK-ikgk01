
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
        }
        multibuys = {
            "A": {3: 130, 5: 200},
            "B": {2: 45}
        }
        bogoff = {
            "E": {"quantity": 2, "offer": "B", "number": 1},
            "F": {"quantity": 2, "offer": "F", "number": 1}
        }
        allowed_characters = list(prices.keys()) #+ [",", " "]
        if len(set(skus) - set(allowed_characters)) != 0:
            return -1
        total = 0
        skus_dict = {}
        for sku in skus:
            skus_dict[sku]=skus_dict.setdefault(sku, 0)+1
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
            count = skus.count(sku)
            if quantity != 0:
                if sku in multibuys:
                    #if count >= multibuys[sku][0]:
                    multibuy_counter = quantity
                    remainder = 0
                    for offer, value in sorted(multibuys[sku].items(), reverse=True):
                        multiple = multibuy_counter // offer
                        multibuy_counter = multibuy_counter - multiple * offer
                        total += multiple * value
                        remainder = quantity % offer
                    total += multibuy_counter * prices[sku]
                else:
                    total += quantity * prices[sku]
        return total


print(CheckoutSolution().checkout("AAAAABBBEEFFFF"))