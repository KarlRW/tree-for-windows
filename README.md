# Tree for Windows


## Overview
```text
In the land of folders wide and deep,
A script was born, to help you peep.
```
A recursive directory listing program that produces a depth-indented listing of files.
View your files and folders with options to filter specific file types. I find it helpful when I want to describe my project structure to openai. 



---
## Features
- Recursively lists directories and files.
- Options to display only directories.
- Filter out or include files based on their extensions.

---
## Usage
```bash
python tree.py [directory] [options]
```
Options:
- `-d`: Display only directories.
- `-fo / --filter_out`: Exclude files with specified extensions.
- `-f / --filter`: Include only files with specified extensions.

Example output
```text
test/
    simple_gui.py
    test0_output.txt
```

---
## Installation
Clone the repository and add the script location to your PATH.

---
## TODO
  - [ ] Add a depth limit
  - [ ] Add option for box drawing, e.g. `└──file.py`

---
## License
Distributed under the MIT License. See `LICENSE` for more information.



