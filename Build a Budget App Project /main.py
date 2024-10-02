import math

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
            
    def get_balance(self):          
        return sum(item["amount"] for item in self.ledger)
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False
        
    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def __str__(self):
        mid_asterik = math.ceil((30-len(self.name))/2)
        total = self.get_balance()
        title = f'{"*"*mid_asterik}{self.name}{"*"*(30-mid_asterik-len(self.name))}\n'
        items = ''
        for expense in self.ledger:
            amount = f'{expense["amount"]:.2f}'.rjust(7)
            description = f'{expense["description"]}{" "*(23-len(expense["description"]))}'[:23]
            items += f'{description}{amount}\n'
        
        totalvalue = f'Total: {total:.2f}'
        return title + items + totalvalue

def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    amount_spent_per_category = []
    total_sum = 0
    biggest_string = 0
    chart_result = []
    for category in categories:
        sum_result = [math.fabs(item['amount']) for item in category.ledger if item['amount'] < 0]
        total_sum += sum(sum_result)
        biggest_string = biggest_string if biggest_string > len(category.name) else len(category.name)
        amount_spent_per_category.append({'name': category.name, 'amount': sum(sum_result)})
    

    for category in amount_spent_per_category:
        total_percentage = int((math.floor((category["amount"]*100)/total_sum/10) * 10)/10) + 1
        # rounddown math.floor(amount/10) * 10
        chart_result.append(' '*(11 - total_percentage) + 'o'* (total_percentage + 1))
       
            
    ind = 0
    for index in range(10,-1, -1):
        bolitas = ''
        for i in range(len(chart_result)):
            bolitas += f'{chart_result[i][ind]}  '
        chart += (" " * (3-len(str(index * 10))))+str(index * 10) + "| " + bolitas +'\n'
        ind += 1
        
        
    chart += " " * 4 + "-" * (3*len(categories) + 1) +'\n'
    
    name_result = []
    for category in amount_spent_per_category:
        name_result.append(category['name'] +' '*(biggest_string - len(category['name'])))
    
    inde = 0
    name_string = ''
    for otro in range(biggest_string):
        name_string += " " * 5
        for index in range(len(name_result)):
            name_string += name_result[index][otro] + "  "
        name_string += "\n"
        
    chart += name_string
    
    return chart.rstrip("\n")
