
```
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        
        self.capacity = capacity
        # Example: [{"k1": "v1"}, {"k2": "v2"}]
        self.items = []
        

    def get(self, key):
        """
        :rtype: int
        """
        
        for i, kv in enumerate(self.items):
            if kv.keys()[0] == key:
                del(self.items[i])
                self.items.insert(0, kv)
                return kv.values()[0]
                
        # Return -1 if no match
        return -1
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        
        if len(self.items) == 0:
            self.items.insert(0, {key: value})
        
        for i, kv in enumerate(self.items):
            # If there is the key, just remove and insert in the head
            if kv.keys()[0] == key:
                del(self.items[i])
                self.items.insert(0, {key: value})
            # If there is no key and there's no capacity
            elif len(self.items) >= self.capacity:
                # Remove one
                self.items.pop()
            
                # Insert one
                self.items.insert(0, {key: value})
            # If there is no key and there is some capacity
            else:
                # Insert one
                self.items.insert(0, {key: value})
```
        