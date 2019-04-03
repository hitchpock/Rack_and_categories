import copy
from TreeRack import rndrack
from Item import Item

def create_dict(lst):
    item_dict = {}
    for item in lst:
        if item.category in item_dict:
            item_dict[item.category].append(item)
        else:
            item_dict[item.category] = [item]
    return item_dict
    # for k, v in item_dict.items():
    #     print("{0}: {1}".format(k, ", ".join(str(item) for item in v)))


def check(lst, volume):
    for item in lst:
        if item.volume <= volume:
            return True
    return False


def control(item_dict, rack_list):
    item_bool, rack_bool = False, False
    for k, v in item_dict.items():
        if len(v) > 0:
            item_bool = True
    if len(rack_list) > 0:
        rack_bool = True
    return item_bool, rack_bool



def search(lst, rack):
    if check(lst, rack.volume) is True:
        state = Item(None, 100, 100)
        for item in lst:
            if item.term <= state.term and item.volume <= rack.volume and (item.category == rack.category or rack.category is None):
                state = item
        if state.category is None:
            return None
        rack.value = state
        rack.category = state.category
        rack.volume -= state.volume
        lst.remove(state)
        if rack.volume > 0:
            n = copy.copy(rack)
            rack.child = search(lst, n)
        return rack
    else:
        return None


def sort(item_list, rack_list):
    for rack in rack_list:
        rack = search(item_list, rack)
    return item_list, rack_list


rack_list, item_list = rndrack()
item_dict = create_dict(item_list)
for item in item_list:
    print(item)
for r in rack_list:
    print("Rack volume = ", r.volume)
print()

item_list, rack_list = sort(item_list, rack_list)

for rack in rack_list:
    print("Rack: cat({0}), st_vol({1}), lst(".format(rack.category, rack.volume_start), end='')
    print(rack)
for item in item_list:
    print(item)
