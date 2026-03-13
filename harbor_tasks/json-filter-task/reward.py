import os
import json

def grade(output_path, input_path):
    """
    Harbor reward function - grade the agent's performance.
    """
    try:
        # Read the agent's output
        output_file = os.path.join(output_path, "output.txt")
        if not os.path.exists(output_file):
            return 0.0
            
        with open(output_file, 'r') as f:
            output_content = f.read().strip()
        
        # Read the expected input to determine correct answer
        input_file = os.path.join(input_path, "input.json")
        with open(input_file, 'r') as f:
            users = json.load(f)
        
        # Calculate expected output (users age >= 18)
        expected_names = [user['name'] for user in users if user['age'] >= 18]
        expected_output = '\n'.join(expected_names)
        
        # Compare agent output with expected output
        if output_content.strip() == expected_output.strip():
            return 1.0
        else:
            return 0.0
            
    except Exception as e:
        print(f"Reward evaluation error: {e}")
        return 0.0

# Alternative function name
def reward(output_path, input_path):
    return grade(output_path, input_path)
