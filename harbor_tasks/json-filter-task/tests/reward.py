import os
import json

def score(output_dir, input_dir):
    """Harbor reward function - returns 1.0 if correct, 0.0 if incorrect"""
    try:
        # Read agent output
        output_file = os.path.join(output_dir, "output.txt")
        if not os.path.exists(output_file):
            return 0.0
            
        with open(output_file, 'r') as f:
            output_content = f.read().strip()
        
        # Read input to calculate expected result
        input_file = os.path.join(input_dir, "input.json")
        with open(input_file, 'r') as f:
            users = json.load(f)
        
        # Expected: users age >= 18
        expected_names = [user['name'] for user in users if user['age'] >= 18]
        expected_output = '\n'.join(expected_names)
        
        # Return 1.0 if correct, 0.0 if incorrect
        return 1.0 if output_content.strip() == expected_output.strip() else 0.0
        
    except Exception:
        return 0.0

# Alias for different possible function names
def reward(output_dir, input_dir):
    return score(output_dir, input_dir)

def grade(output_dir, input_dir):
    return score(output_dir, input_dir)
