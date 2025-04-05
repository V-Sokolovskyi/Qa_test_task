# Qa_test_task 
A simple Python script that performs **one-way synchronization** between two folders (`source` ➝ `replica`) with support for periodic syncing, file hashing, logging, and basic testing.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)


---

## Installation

1. **Clone the repo**

```bash
git clone https://github.com/V-Sokolovskyi/Qa_test_task.git
cd Qa_test_task
```

2. **Create a virtual environment (highly recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```
   
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

The script is launched via CLI and accepts the following **positional arguments**:

| Argument     | Description                           | Required |
|--------------|---------------------------------------|----------|
| `source`     | Path to the source folder             | ✅ yes    |
| `replica`    | Path to the replica folder            | ✅ yes    |
| `log_file`   | Path to the log file                  | ✅ yes    |
| `interval`   | Time in seconds between syncs         | ✅ yes    |

And these **optional arguments**:

| Flag         | Description                                          | Default   |
|--------------|------------------------------------------------------|-----------|
| `--algo`     | Hashing algorithm to compare files (`md5`, `blake2b`, etc.) | `blake2b` |
| `--once`     | If set, performs sync once and exits                 | `False`   |

---

## Examples

#### Run once (no interval, just sync immediately):

```bash
python main.py source replica log.txt 0 --once

#### Run every 10 seconds:
python main.py source replica log.txt 10

#### Use a different hashing algorithm (e.g., md5):
python main.py source replica log.txt 5 --algo md5








   
