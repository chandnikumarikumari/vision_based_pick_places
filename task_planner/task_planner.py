class TaskPlanner:
    def generate_plan(self):
        plan = [
            "move_home",
            "move_pre_grasp",
            "pick_object",
            "move_pre_place",
            "place_object"
        ]
        return plan

if __name__ == "__main__":
    planner = TaskPlanner()
    plan = planner.generate_plan()
    print("Generated symbolic plan:")
    for step in plan:
        print(step)
