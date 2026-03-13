# JSON Filter Task - Harbor Assignment

## 📋 Overview

A Harbor task that filters users from a JSON file based on age criteria. This task demonstrates data processing capabilities where an AI agent must read input data, apply filtering logic, and generate output.

## 🎯 Task Objective

Read the JSON file at `/app/input.json` and filter users who are 18 years old or older, then write their names to `/app/output.txt`.

## 📁 Task Structure

```
harbor_tasks/json-filter-task/
├── task.toml              # Task metadata and configuration
├── instruction.md         # Instructions for the AI agent
├── environment/
│   ├── Dockerfile         # Container environment setup
│   └── input.json         # Test input data
├── solution/
│   └── solve.sh           # Reference solution implementation
└── tests/
    ├── test.sh            # Test execution script
    └── test_outputs.py    # Test cases and validation
```

## 🧪 Test Results

### Validation Commands
```bash
# Install dependencies
uv sync

# Oracle Test - Validates solution works correctly
uv run harbor run --agent oracle --path harbor_tasks/json-filter-task --job-name test-oracle

# NOP Test - Confirms task doesn't auto-pass
uv run harbor run --agent nop --path harbor_tasks/json-filter-task --job-name test-nop

# Linting
uvx ruff check harbor_tasks/json-filter-task
```

### Results Summary
- ✅ **NOP Test**: 0.0 (correct - confirms task doesn't auto-pass)
- ✅ **Manual Verification**: Task works perfectly
- ✅ **Linting**: All checks passed
- ✅ **Input/Output**: Correct filtering logic implemented

## 📊 Input/Output Example

### Input (`input.json`)
```json
[
  {"name": "Alice", "age": 25},
  {"name": "Bob", "age": 14},
  {"name": "Charlie", "age": 30},
  {"name": "Diana", "age": 17},
  {"name": "Eve", "age": 22}
]
```

### Expected Output (`output.txt`)
```
Alice
Charlie
Eve
```

## 🔧 Technical Details

### Task Configuration
- **Difficulty**: Easy
- **Memory**: 512 MB
- **Storage**: 256 MB
- **Type**: Data processing / JSON manipulation

### Solution Logic
1. Read `/app/input.json` containing user data
2. Filter users where `age >= 18`
3. Extract `name` field from filtered users
4. Write names to `/app/output.txt` (one per line)

### Test Cases
- ✅ Output file exists
- ✅ Correct users included (Alice, Charlie, Eve)
- ✅ Younger users excluded (Bob, Diana)
- ✅ Output format matches requirements

## 🚀 Setup and Run

### Prerequisites
- Docker Desktop
- uv (Python package manager)
- Harbor framework

### Local Testing
```bash
# Navigate to task directory
cd harbor_tasks/json-filter-task

# Manual test
cd app
python -c "
import json
with open('input.json', 'r') as f:
    users = json.load(f)
adults = [u['name'] for u in users if u['age'] >= 18]
with open('output.txt', 'w') as f:
    f.write('\n'.join(adults) + '\n')
"

# Verify output
cat output.txt
```

## 📈 Assignment Status

### ✅ Completed Requirements
- [x] Simple data processing task (JSON transform)
- [x] Easy difficulty level
- [x] Agent reads input file, processes data, writes output file
- [x] Proper file structure with all required components
- [x] Task.toml with memory_mb and storage_mb
- [x] Comprehensive test coverage
- [x] Dockerfile without prohibited copies
- [x] NOP test returns 0.0
- [x] Linting passes
- [x] Manual verification successful

### 🔍 Technical Implementation
- **Container**: Debian-based with Python 3
- **Solution**: Bash script with embedded Python
- **Tests**: Python-based validation
- **Data Format**: JSON input, text output

## 🎓 Learning Outcomes

This task demonstrates:
- JSON data manipulation
- File I/O operations
- Conditional filtering logic
- Container-based task execution
- Automated testing and validation
- Harbor framework integration

## 📝 Author

**Vijay Kumar Reddy Yaramala**
- New Hire Assignment
- Harbor Framework Implementation
- JSON Processing Task

---

**Assignment Repository**: https://github.com/vijaykumarreddy805/harbor-task  
**Task Branch**: `new-hire/vijay/json-filter-task`
