import math
import matplotlib.pyplot as plt

def draw_fractal_tree(depth=5, length=1, scale=0.6, angle_change=0.1):
    """
    Draws a fractal tree using simple matplotlib plot calls.
    """
    # 1. Setup the plot
    plt.figure()
    
    # 2. Draw the initial trunk
    # We start at (0,0) and draw up to (0,1)
    plt.plot([0, 0], [0, 1], color='black')
    
    # 3. Initialize our "tips" list
    # Format: [x, y, current_angle]
    # We start at the top of the trunk: (0, 1), pointing up (angle 0)
    tips = [[0, 1, 0]]
    
    current_length = length

    # 4. Loop through generations
    for _ in range(depth):
        new_tips = []
        
        for x, y, angle in tips:
            # Calculate Left Branch logic
            angle_left = angle - angle_change
            x_left = x + current_length * math.sin(angle_left)
            y_left = y + current_length * math.cos(angle_left)
            
            # Calculate Right Branch logic
            angle_right = angle + angle_change
            x_right = x + current_length * math.sin(angle_right)
            y_right = y + current_length * math.cos(angle_right)
            
            # Plot Left Branch
            plt.plot([x, x_left], [y, y_left], color='green', alpha=0.6)
            
            # Plot Right Branch
            plt.plot([x, x_right], [y, y_right], color='green', alpha=0.6)
            
            # Save new tips for the next loop
            new_tips.append([x_left, y_left, angle_left])
            new_tips.append([x_right, y_right, angle_right])
        
        # Update the list of tips and shrink the length
        tips = new_tips
        current_length *= scale

    plt.savefig('tree.png')
    plt.show()

if __name__ == "__main__":
    draw_fractal_tree()