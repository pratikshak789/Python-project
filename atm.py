class Atm:
    def _init_(self):
        self.pin = ''
        self.balence = 0
        self.menu()
    
        
    def menu(self):
        user_input = input("""
        Hi how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. press 3 to check balance
        4. press 4 to withdraw
        5. Anything else to exit
        """)
        
        if user_input == '1':
          #pin
          self.creat_pin()
        elif user_input == '2':
            #cange pin
          self.change_pin()
        elif user_input == '3':
            self.check_balence()
            #check balence
        elif user_input == '4':
            self.withdraw()
        else:
            exit()
         
    def  creat_pin(self):
        user_pin = input("enter your pin :")
        self.pin =user_pin
        
        user_balence = int(input("enter balence :"))
        self.balence = user_balence
        
        print("pin created successfully")
        self.menu()
    
    def  change_pin(self):
        old_pin = input("enter old pin : ")
        
        if old_pin == self.pin:
            new_pin = input("enter new pin :")
            self.pin = new_pin
            print("pin change successful")
            self.menu()
        else:
            print("you entered wrong pin")
    
    def check_balence(self):
        user_pin = input("Enter your pin :")
        if user_pin == self.pin:
            print("your balence is", self.balence)
        else:
            print("you entered wrong pin")
            
    def withdraw(self):
        user_pin = input("enter the pin :")
        if user_pin == self.pin:
            amount = int(input("enter the amount :"))
            if amount <= self.balence:
                self.balence = self.balence - amount
                print("withdraw successful balence is", self.balence)
            else:
                print("No enough balence")
        else:
            print("your pin is incorrect")
        
p=Atm()
p.menu()
p.menu()



        
        
        
        
        
        
        




