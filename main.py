
# 15. TaxiRide
class TaxiRide:
    def __init__(self, distance, price_per_km):
        self.distance = distance
        self.price_per_km = price_per_km

    def calculate_fare(self):
        total = self.distance * self.price_per_km
        print(f"Yo‘l narxi: {total} so'm")

    def apply_discount(self, percent):
        total = self.distance * self.price_per_km
        new = total - total * percent / 100
        print(f"Chegirmadan keyin: {int(new)} so'm")


tr = TaxiRide(10, 2500)
tr.calculate_fare()
tr.apply_discount(20)
