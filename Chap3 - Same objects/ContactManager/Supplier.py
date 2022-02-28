from Contact import Contact

class Supplier(Contact):

    def order(self, order: "Order") -> None:
        print(
            "If this was an order, we would send " 
            f"'{order}' order to '{self.name}'"
        )