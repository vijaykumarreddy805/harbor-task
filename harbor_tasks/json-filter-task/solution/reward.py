import os
import json

def grade(output_path, input_path):
    """Harbor reward function"""
    try:
        output_file = os.path.join(output_path, "output.txt")
        if not os.path.exists(output_file):
            return 0.0
            
        with open(output_file, 'r') as f:
            output_content = f.read().strip()
        
        input_file = os.path.join(input_path, "input.json")
        with open(input_file, 'r') as f:
            users = json.load(f)
        
        expected_names = [user['name'] for user in users if user['age'] >= 18]
        expected_output = '\n'.join(expected_names)
        
        return 1.0 if output_content.strip() == expected_output.strip() else 0.0
            
    except Exception as e:
        return 0.0

def reward(output_path, input_path):
    return grade(output_path, input_path)
