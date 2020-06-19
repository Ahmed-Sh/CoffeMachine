class Coffee:

    TOTAL = [[400, 540, 120, 9, 550], [250, 0, 16, 1, 4], [350, 75, 20, 1, 7], [200, 100, 12, 1, 6]]
    
    
    def machine_status(self):
        print("""The coffee machine has:
%s of water
%s of milk
%s of coffee beans
%s of disposable cups
%s of money""" % (self.TOTAL[0][0], self.TOTAL[0][1], self.TOTAL[0][2], self.TOTAL[0][3], self.TOTAL[0][4]))


    def action_needed(self):
        while True:
            action = input("Write action (buy, fill, take ,remaining, exit):\n> ")
            if action == "buy" or "fill" or "take" or "remaining" or "exit":
                if action == "buy":
                    self.buy()
                elif action == "fill":
                    self.fill()
                elif action == "take":
                    self.take()
                elif action == "remaining":
                    self.machine_status()
                elif action == "exit":
                    break


    def buy(self):
        avail = []
        ingredients = ["water", "milk", "beans", "cups"]
        while True:
            answer = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n> ")
            if answer == "back":
                break
            elif 0 < int(answer) < 4:
                for i in range(0, 4):
                    avail.append(self.TOTAL[0][i] - self.TOTAL[int(answer)][i])
                    if avail[i] < 0:
                        print("Sorry, not enough %s!" % ingredients[i])
                        return
                else:
                    print("I have enough resources, making you a coffee!")
                    self.TOTAL[0][0] -= self.TOTAL[int(answer)][0]
                    self.TOTAL[0][1] -= self.TOTAL[int(answer)][1]
                    self.TOTAL[0][2] -= self.TOTAL[int(answer)][2]
                    self.TOTAL[0][3] -= 1
                    self.TOTAL[0][4] += self.TOTAL[int(answer)][4]
                break



    def fill(self):
        try:
            self.TOTAL[0][0] += int(input("Write how many ml of water do you want to add:\n> "))
            self.TOTAL[0][1] += int(input("Write how many ml of milk do you want to add:\n> "))
            self.TOTAL[0][2] += int(input("Write how many grams of coffee beans do you want to add:\n> "))
            self.TOTAL[0][3] += int(input("Write how many disposable cups of coffee do you want to add:\n> "))
        except:
            print("Please enter a Number")
            self.fill()



    def take(self):
        print("I gave you $%s" % self.TOTAL[0][4])
        self.TOTAL[0][4] = 0

coffee_mc = Coffee()
coffee_mc.action_needed()

    
    
