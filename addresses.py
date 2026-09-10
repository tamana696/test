class Address:
    def __init__(self,type_of_address,city,street,zip_code):
        self.type = type_of_address
        self.city = city
        self.street = street
        self.zip_code = zip_code

    def __str__(self):
        return f"address {self.type}:{self.city},{self.street},{self.zip_code}"
        