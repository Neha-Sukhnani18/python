class Robot:
    """
    A class to represent a robot, demonstrating OOPS concepts.
    """
    population = 0
    def __init__(self, name, color, model):
        """
        Constructor method to initialize robot attributes.
        """
        self.name = name          
        self.color = color        
        self.model = model        
        Robot.population += 1     
    def introduce_self(self):
        """
        Method for the robot to introduce itself.
        """
        print(f"Hello! My name is {self.name}.")
        print(f"I am a {self.color} {self.model} model.")
        print(f"I am an instance of the Robot class, created using OOPS principles.")
    def perform_task(self):
        """
        Method to describe the robot's general task.
        """
        print(f"{self.name} is now performing a general task.")
my_robot = Robot(name="Circuit", color="silver", model="v3.1")
my_robot.introduce_self()
my_robot.perform_task()
print(f"\nTotal robots created: {Robot.population}")