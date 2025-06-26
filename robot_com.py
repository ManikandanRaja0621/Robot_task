class Robot:
    def __init__(self, robot_id, matrix):
        self.robot_id = robot_id
        self.x = 0  
        self.y = 0  
        self.matrix = matrix
        self.matrix[self.x][self.y] = self.robot_id  

    def move(self, direction):
        direction_map = {
            'N': (-1, 0),  
            'S': (1, 0),   
            'E': (0, 1),   
            'W': (0, -1)   
        }

        
        direction_letter = direction[0].upper()
        steps = int(direction[1])

        dx, dy = direction_map.get(direction_letter, (0, 0))

        for _ in range(steps):
            new_x = self.x + dx
            new_y = self.y + dy

            
            if not (0 <= new_x < len(self.matrix) and 0 <= new_y < len(self.matrix[0])):
                break  
            if self.matrix[new_x][new_y] is not None:
                break  

            
            self.matrix[self.x][self.y] = None  
            self.x, self.y = new_x, new_y
            self.matrix[self.x][self.y] = self.robot_id  

    def get_position(self):
        return self.x, self.y


class RobotManager:
    def __init__(self, grid_size):
        self.matrix = [[None for _ in range(grid_size[1])] for _ in range(grid_size[0])]
        self.robots = {}
        self.next_id = 1

    def create_robot(self):
        robot = Robot(self.next_id, self.matrix)
        self.robots[self.next_id] = robot
        self.next_id += 1
        return robot

    def move_robot(self, robot_id, direction):
        if robot_id in self.robots:
            self.robots[robot_id].move(direction)

    def get_robot_position(self, robot_id):
        if robot_id in self.robots:
            return self.robots[robot_id].get_position()
        return None

    def print_matrix(self):
        for row in self.matrix:
            print(row)



def main():
    grid_size = (5, 5) 
    manager = RobotManager(grid_size)

    print(" the Robot Start ")
    print("Commands: \nC - Create Robot \nM - Move Robot \nQ - Quit")

    while True:
        
        command = input("\nEnter command: ").strip().upper()

        if command == 'C':
            robot = manager.create_robot()
            print(f"Robot {robot.robot_id} created at position (0, 0).")

        elif command == 'M':
            robot_id = int(input("Enter robot ID to move: "))
            if robot_id in manager.robots:
                direction = input("Enter movement (e.g., N3, E2, S1, W4): ").strip()
                manager.move_robot(robot_id, direction)
                print(f"Robot {robot_id} moved.")
            else:
                print(f"Robot {robot_id} not found!")

        elif command == 'Q':
            print("Exiting simulation.")
            break

        else:
            print("Invalid command. Please use C, M, or Q.")
        
        
        manager.print_matrix()



if __name__ == "__main__":
    main()
