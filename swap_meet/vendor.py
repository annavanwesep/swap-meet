class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory or []
    
    def add(self, one_item):
        if not one_item in self.inventory:
            self.inventory.append(one_item)
        return one_item
    
    def remove(self, one_item):
        if not one_item in self.inventory:
            return False
        elif one_item in self.inventory:
            self.inventory.remove(one_item)
            return one_item