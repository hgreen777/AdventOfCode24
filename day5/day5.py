from datetime import datetime

start_time = datetime.now()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class RulesList:
    def __init__(self):
        self.head = None

    def appendNode(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return new_node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        return new_node


rules = [RulesList() for i in range(100)]
page_orders = []

# Read all rules (into hash table) & Page numbers from input
count = 0 
readingRules = True
with open('input.txt', 'r') as file:
    for line in file:
        count += 1

        if count == 1177:
            readingRules = False
            continue
        
        if readingRules:
            line = line.strip()
            num1 = int(line[0:2])
            num2 = int(line[3:5])
            rules[num1].appendNode([num1,num2])
        else:
            page_orders.append([int(x) for x in line.strip().split(',')])



# Search each page in table O(1) (then O(n) with closed addressing))
middle_total = 0
for page_order in page_orders:
    valid = True
    for index,page in enumerate(page_order):
        if valid == False:
            break

        # Check if a rule exists for that page.
        if rules[page].head == None:
            continue
        else:
            node = rules[page].head

            # Traverse linked list checking if each rule is obeyed
            while node is not None and valid != False:
                # Search for node[1] in the is page_order before the current node -> if it appears it is incorrect
                for i in range(index):
                    if node.data[1] == page_order[i]:
                        # Incorrect, break
                        valid = False
                        break
                node = node.next

    # Pull the middle value and add
    if valid:
        middle_total += page_order[len(page_order) // 2]

print(f"Part 1 Total: {middle_total}")

end_time = datetime.now()
execution_time = (end_time - start_time).total_seconds()
print(f"Execution time: {execution_time} seconds")