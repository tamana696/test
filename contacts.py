from phnumber import PhoneNumber 
from addresses import Address
from relation import Relation
from social import SocialAddress


class Contact:
    def __init__(self,firstname,lastname,phone_numbers,email,avatar,addresses,relation,social_address):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone_numbers
        self.email = email
        self.avatar = avatar
        self.addresses = addresses
        self.relation = relation
        self.social_address = social_address


    def __str__(self):
        return f"Name:{self.firstname} {self.lastname}\nPhone numbers:{self.phone}\nEmail:{self.email}\nAvatar:{self.avatar}\nAddress:{self.addresses}\nRelation:{self.relation}\nSocial address:{self.social_address}"
        