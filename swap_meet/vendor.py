from swap_meet import item

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
    
    def get_by_id(self, id):
        for item in self.inventory:   
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        for item in self.inventory:
            if my_item in self.inventory and their_item in other_vendor.inventory:                
                self.inventory.remove(my_item)
                other_vendor.inventory.append(my_item)
                other_vendor.inventory.remove(their_item)
                self.inventory.append(their_item)
                return True
        return False     
    
    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        
        first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]
        
        self.inventory[0] = their_first_item
        other_vendor.inventory[0] = first_item
        return True
    
    def get_by_category(self, category):
        items_in_category = []
        
        for item in self.inventory:
            if item.get_category() == category:
                items_in_category.append(item)
        return items_in_category
        

    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)
        
        if not items_in_category:
            return None
        best_item = max(items_in_category, key=lambda item: item.condition)
        return best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):

        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        return self.swap_items(other_vendor, my_best_item, their_best_item)
