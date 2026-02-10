
class MoveItInterface:
    def execute(self, action):
        print(f"Executing motion: {action}")

if __name__ == "__main__":
    executor = MoveItInterface()
    actions = [
        "move_home",
        "pre_grasp",
        "approach",
        "grasp",
        "lift",
        "place"
    ]
    for a in actions:
        executor.execute(a)
