
class Monkey:
    def __init__(self, name, operation_type, operation_val, test_divisor, true_monkey, false_monkey, initial_items = None ):
        self.name = name
        self.operation_type   = operation_type
        self.operation_val    = operation_val
        self.test_divisor     = test_divisor
        self.true_monkey      = true_monkey
        self.false_monkey     = false_monkey
        self.inspection_count = 0

        if initial_items ==None:
            self.items = []
        else:
            self.items = initial_items

    def get_list(self):
        return self.items
    
    def operation(self, x):
        self.inspection_count +=1
        if self.operation_val == "old" and self.operation_type == "*":
            return x*x
        elif self.operation_val == "old":
            return 2*x
        elif self.operation_type == "*":
            return x* int(self.operation_val)
        else:
            return x + int(self.operation_val)
        
    def divisibility_test(self, input):
        if input % self.test_divisor == 0:
            return self.true_monkey
        else:
            return self.false_monkey
    
    def add_item(self, new_item):
        self.items.append(new_item)

    def pop_item(self):
        return self.items.pop(0)
    
    def get_inspection_count(self):
        return self.inspection_count
    
    def __repr__(self) -> str:
        return self.name

    def get_test_divisor(self):
        return self.test_divisor
    
def process_round(monkeys, gcd_version = False):
    gcd = 1
    for monkey in monkeys:
        #subtraction gcd from each item won't affect any of the modulo tests.
        #items won't be correct, but inspection counts will be.
        gcd = gcd * monkey.get_test_divisor()

    for monkey in monkeys:
        list_length = len(monkey.get_list())
        for val in range(list_length):
            item = monkey.pop_item()
            modified_item = monkey.operation(item)
            if gcd_version:
                modified_item = modified_item % gcd
            else:
                modified_item = modified_item // 3
            monkey_passed_to = monkey.divisibility_test(modified_item)
            monkeys[monkey_passed_to].add_item(modified_item)
    

def main(iterations, gcd_version = False):
    monkeys = []
    with open ("p11.txt", 'r') as file:
        lines = file.readlines()
    
    i = 0
    while i < len(lines):
            if lines[i][:6] == "Monkey":
                name = lines[i][:-2]
                
                items = lines[i+1].split()[2:]
                items = [int(x.strip(",")) for x in items]

                op = lines[i+2].split()
                operation_type = op[4]
                operation_val  = op[5]

                test_divisor = lines[i+3].split()[-1]
                test_divisor = int(test_divisor)

                true_monkey  = lines[i+4].split()[-1]
                true_monkey  = int(true_monkey)

                false_monkey  = lines[i+5].split()[-1]
                false_monkey  = int(false_monkey)

                monkeys.append(Monkey(name, operation_type, operation_val, test_divisor, true_monkey, false_monkey,items))
                i += 6

            else:
                i+=1

    for i in range(iterations):       
        process_round(monkeys, gcd_version)

    inspection_counts = []
    for monkey in monkeys:
        inspection_counts.append(monkey.get_inspection_count())
    
    inspection_counts.sort(reverse = True)
    return  inspection_counts[0]*inspection_counts[1]
    


if __name__ == "__main__":
    print("Solution to Pt 1 is: ", main(20))
    print("Solution to Pt 2 is: ", main(10000, gcd_version = True))

            
        
