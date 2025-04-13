# Qa_test_task - Folder Synchronization Tool
A simple Python script that performs **one-way synchronization** between two folders (`source` ➝ `replica`) with support for periodic syncing, file hashing, logging, and basic testing.

---

## 📂 Features

- 🔄 One-way folder sync (source → replica)
- ⏱ Periodic syncing with customizable interval
- 🧠 Uses file hashing (`blake2b`, `md5`, etc.) to detect changes
- 📄 Logs operations (created, deleted, updated files)
- 📦 CLI interface via `argparse`
- ✅ Includes unit tests (via `pytest`)
- 🧪 Fake test data generator using `Faker`

---
  
## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Run Tests](#run-tests)
4. [Project Structure](#project-structure)
5. [License](#license)

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



### Examples
#### Run once (no interval, just sync immediately):

```bash
python main.py source replica log.txt 0 --once
```

#### Run every 10 seconds:

```bash
python main.py source replica log.txt 10
```
#### Use a different hashing algorithm (e.g., md5):

```bash
python main.py source replica log.txt 5 --algo md5
```

---
## Run Tests

### All tests are in `test/`
- `conftest.py` defines a **fixture** that:
  - creates test folders/files using `Faker`
  - cleans them up after tests complete
- Tests are marked with `@pytest.mark.sync` for targeted execution
  
#### Example test command
```bash
pytest -m sync -s
```
This will:

 - use the setup_test_data fixture from conftest.py

 - run only tests marked @pytest.mark.sync

 - show all logging output from your sync logic

---

## Project Structure
```bash

├── main.py               # Entry point: starts sync process
├── requirements.txt      # Project dependencies
├── pytest.ini            # Pytest configuration (markers, logging)
├── conftest.py           # Pytest fixture to init logging for tests
├── README.md             # Project documentation
├── .gitignore            # Files to ignore in Git
├── sync_tool/            # Core functionality
│   ├── __init__.py
│   ├── arg_parse.py      # CLI argument parser
│   ├── cashe_utils.py    # Cache for file hashes
│   ├── hash_utils.py     # File hashing logic
│   ├── logger.py         # Logging setup
│   └── sync_logic.py     # Folder synchronization logic
├── test/                 # Unit tests with Pytest
│   ├── test_sync.py      # Test for syncing logic
│   ├── utils.py          # Fake file/folder generator (Faker)
│   └── conftest.py       # Test data fixture

```

---

## License

This project is distributed under the terms of the [MIT License](LICENSE).



   
