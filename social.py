class SocialAddress:
    def __init__(self,platform,idaddress):
        self.platform = platform
        self.idaddress = idaddress

    def __str__(self):
        return f"social address:{self.platform}=>{self.idaddress}"