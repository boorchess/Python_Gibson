
dog = input('Doctor Mike says Fat Dog is overweight he weigs 100 pound. he should be 80 pounds,How much should you loose? 100 - 80 = ')
print(100 - 80) 
print('Is the amswer')
print('Lets compare to ais version')
import random
import pyttsx3

class Pet:
    def __init__(self, name, weight, weight_loss_goal, calorie_per_unit):
        self.name = name
        self.weight = weight
        self.weight_loss_goal = weight_loss_goal
        self.calorie_per_unit = calorie_per_unit

    def calculate_required_daily_intake(self):
        return (self.weight - self.weight_loss_goal) * self.calorie_per_unit

    def generate_problem(self):
        return f"Dr. Says {self.name} is overweight. {self.name} currently weighs {self.weight} pounds. Proper weight is {self.weight - self.weight_loss_goal} pounds. How many units should {self.name} eat daily to achieve the weight loss goal?"

def main():
    engine = pyttsx3.init()
    name = input("Enter your pet's name: ")
    weight = random.randint(30, 80)  # Random initial weight between 30 and 80 pounds
    weight_loss_goal = random.randint(5, 15)  # Random weight loss goal between 5 and 15 pounds
    calorie_per_unit = random.randint(200, 300)  # Random calorie per unit between 200 and 300 calories

    pet = Pet(name, weight, weight_loss_goal, calorie_per_unit)

    print("Welcome to the Calorie Intake & Weight Loss Math Game!")
    print(f"Your pet is {name}, a {weight} pound pet that needs to lose {weight_loss_goal} pounds.")
    print(f"Each unit of food contains {calorie_per_unit} calories.")

    while True:
        problem = pet.generate_problem()
        print("\n" + problem)
        engine.say(problem)
        engine.runAndWait()

        user_answer = input("Enter your answer: ")
        
        try:
            user_answer = float(user_answer)
            required_daily_intake = pet.calculate_required_daily_intake()
            if user_answer == required_daily_intake:
                print("Correct! Good job!")
                engine.say("Correct! Good job!")
            else:
                print(f"Incorrect. The correct answer is {required_daily_intake}. Try again.")
                engine.say(f"Incorrect. The correct answer is {required_daily_intake}. Try again.")
            engine.runAndWait()
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
