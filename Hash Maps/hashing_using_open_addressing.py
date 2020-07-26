class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [None] * size
        
    def hash(self, key, count_collisions = 0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions
    
    def compressor(self, hash_code):
        return hash_code % self.array_size
    
    def assign(self, key, value):
        chosen_index = self.compressor(self.hash(key))
        current_array_value = self.array[chosen_index]
        if not current_array_value:
            self.array[chosen_index] = [key, value]
        else:
            if current_array_value[0] == key:
                self.array[chosen_index][1] = value
            else:
                number_of_collisions = 1
                while current_array_value != key:
                    new_hash_code = self.hash(key, number_of_collisions)
                    new_array_index = self.compressor(new_hash_code)
                    new_array_value = self.array[new_array_index]
                    if not new_array_value:
                        self.array[new_array_index] = [key, value]
                        return
                    if new_array_value[0] == key:
                        new_array_value[1] = value
                        return
                    number_of_collisions += 1
                             
    def retrieve(self, key):
        potential_index = self.compressor(self.hash(key))
        possible_return_value = self.array[potential_index]
        if not possible_return_value:
            return None
        else:
            if possible_return_value[0] == key:
                return possible_return_value[1]
            else:
                retrieval_collisions = 1
                while possible_return_value[0] != key:
                    new_hash_code = self.hash(key, retrieval_collisions)
                    retrieving_array_index = self.compressor(new_hash_code)
                    possible_return_value = self.array[retrieving_array_index]
                    if not possible_return_value:
                        return None
                    if possible_return_value[0] == key:
                        return possible_return_value[1]
                    retrieval_collisions += 1



flower_definitions = [['begonia', 'cautiousness'], ['chrysanthemum', 'cheerfulness'], 
                      ['carnation', 'memories'], ['daisy', 'innocence'], 
                      ['hyacinth', 'playfulness'], ['lavender', 'devotion'], 
                      ['magnolia', 'dignity'], ['morning glory', 'unrequited love'], 
                      ['periwinkle', 'new friendship'], ['poppy', 'rest'], 
                      ['rose', 'love'], ['snapdragon', 'grace'], 
                      ['sunflower', 'longevity'], ['wisteria', 'good luck']]
    

h = HashMap(len(flower_definitions))

for i in flower_definitions:
    h.assign(i[0], i[1])
    
print(h.retrieve("daisy"))
print(h.retrieve("magnolia"))
print(h.retrieve("carnation"))
print(h.retrieve("morning glory"))
