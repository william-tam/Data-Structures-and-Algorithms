#Initialize the node class for any node initializations. 

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class print_left_view_of_tree:
    def left_view(self,level, result=[]):
        self = Node()
        # if the level of the node is at the max_level, the self data will be added into the result list. 
        max_level = 0 

        if(self == None): 
            return
        if(max_level < level): 
            result.add(self.value)
            max_level = level 
        left_view(self.left, level+1, result)
        left_view(self.right, level+1, result)

def main():
    #First 3 key values. 
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3)
    # root.right.right = Node(6)
    result = []
    instance = print_left_view_of_tree()
    instance.left_view(root, 1, result)

    for i in range(result): 
        print(i + " ")


if __name__ == '__main__': 
        main()