class Relation:
    def __init__(self,relation_type):
        self.relation_type = relation_type

    def __str__(self):
        return f"relation:{self.relation_type}"
        