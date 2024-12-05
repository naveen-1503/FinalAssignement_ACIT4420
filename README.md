### README.md

# Optimal Route and Transportation Calculation System

This project is designed to calculate the most efficient route between multiple locations and determine the best transportation modes based on time, cost, and distance. Users can add locations, update transportation modes, and view optimized routes in a user-friendly tabular format.

---

## Features

- Manage and store relatives' location data.
- Manage available transportation modes (add, include, exclude).
- Calculate pairwise distances between locations using the **geopy** library.
- Determine the shortest path using heuristic algorithms.
- Optimize transportation modes for cost, time, and efficiency.
- Log program execution and function calls for debugging and auditing.

---

## Installation Instructions

### Prerequisites
1. **Python 3.8 or higher**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).
2. **pip**: The Python package manager, typically included with Python installations.

### Required Libraries
The project uses the following Python libraries:
- `geopy`
- `tabulate`


### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/naveen-1503/FinalAssignement_ACIT4420.git
   cd tarjanPlanner
   ```

2. **Run the Program**
   Start the program by running `main.py`:
   ```bash
   python main.py
   ```

---

## Project Structure

```
optimal-route-transport/
├── main.py                    # Entry point for the program
├── relatives.py               # Manages relatives and their locations
├── transportManager.py        # Manages transport modes
├── calculateDistance.py       # Calculates distances and shortest path
├── transportationCalculation.py # Optimizes transport modes and calculates costs/times
├── logger.py                  # Logs function calls and execution times
├── relatives.json             # JSON file storing relatives' location data
├── transportmodes.json        # JSON file storing transport modes
└── logger.txt                 # Log file for debugging

├── read.me       
└── setup.py                
```

---

## Usage

1. **Add Relatives**:
   - The program allows you to view, add, and manage relatives' location data.
   - You will be prompted to input details like latitude, longitude, street name, and district.

2. **Manage Transport Modes**:
   - View, add, or modify transport modes with speed, cost, and transfer time.

3. **Optimize Route**:
   - The program calculates the shortest path between all locations and selects the best transport mode for each segment based on time, cost, and transfer efficiency.

4. **View Results**:
   - Results are displayed in a tabular format, including total time, distance, and cost.

---

## Logging and Debugging

- Function calls and program execution times are logged in `logger.txt` for transparency and debugging.
- The log file is updated automatically during program execution.



# File Sorter

## Overview

File Sorter is a Python-based utility script designed to organize files in a specified directory by categorizing them into subdirectories based on their file types. It simplifies file management and ensures your directories remain neat and well-organized.

The script supports categorizing files into common types, such as images, documents, videos, music, and archives, with an additional default category for uncategorized files.

---

## Features

- Categorizes files into predefined groups like images, documents, videos, and more.
- Automatically creates subdirectories for each category.
- Moves files into their respective subdirectories without data loss.
- Handles missing directories, permission issues, and uncategorized files gracefully.
- Logs all file movements for easy tracking and debugging.

---

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system. You can download Python from [python.org](https://www.python.org/).

### Steps to Install

1. Clone the repository to your local machine:

   git clone https://github.com/naveen-1503/FinalAssignement_ACIT4420.git
   cd fileOrganizer


2. Install the package locally:

   pip install .


   This command will set up the script as a command-line utility.

---

## Usage

### Running the Script

Once installed, you can use the `fileOrganizer` command to run the script. Follow these steps:

1. Open a terminal or command prompt.
2. Run the following command:
   "
   fileOrganizer
   "
3. When prompted, enter the path to the directory you want to organize:
  "
   What Directory do you want to sort? /path/to/your/directory
  "

   The script will then organize the files in the specified directory into categorized subdirectories.

## Logging and Debugging

- All file movements are logged in a file named `message_log.txt` in the root directory of the project.
- Errors and runtime events are logged to the console for real-time monitoring.

---

## Directory Structure

The project structure is organized as follows:

fileOrganizer/
│
├── __init__.py           # Marks the directory as a Python package
├── main_script.py        # Contains the main logic for file sorting
├── sorFiles.py           # Sorts the file in to subdirectories
├── permissions.py        # Checks if the file has the correct permissions
├── logger.py             # Creates the logs 
├── message_log.txt       # Logs file movements

├── setup.py              # Script for packaging and installation
├── README.md             # Documentation for the project