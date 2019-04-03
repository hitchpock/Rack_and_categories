import copy

class Node:
    def __init__(self, volume):
        self.volume = volume
        self.value = None
        self.child = None


    def __str__(self):
        if self.child is not None:
            return "{0} --> {1}".format(self.value, str(self.child))
        else:
            return "{0}".format(self.value)
        


# tpl = (volume, time)
tpl_list = [(4, 5), (1, 3), (3, 2), (2, 5), (3, 4)]
# n.value = [(3, 2), (1, 3), (2, 5)]
n = Node(6)

def check(lst, volume):
    for i in lst:
        if i[0] <= volume:
            return True
    return False

def search(lst, tree):
    if check(lst, tree.volume) is True:
        state = lst[0]
        for i in lst:
            if i[1] <= state[1] and i[0] <= tree.volume:
                state = i
        tree.value = state
        tree.volume -= state[0]
        lst.remove(state)
        if tree.volume > 0:
            n = copy.copy(tree)
            tree.child = search(lst, n)
        return tree
    else:
        return None
    
    
n = search(tpl_list, n)
print(n)
print (tpl_list)
