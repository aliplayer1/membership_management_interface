# Recreational Club Management System

## Overview
The Recreational Club Management System is designed to help manage the operations of a club, including membership handling, financial transactions, and attendance tracking. It provides both a command-line interface (CLI) and a graphical user interface (GUI), making it accessible for different user preferences.

## Files Description
- **`interface.py`**: A CLI for interacting with the club management system, including options to add members, record payments, view financial reports, and exit.
- **`interface_gui.py`**: A GUI built with Tkinter that mirrors the CLI functionalities for a more intuitive user experience.
- **`models.py`**: Defines data models using SQLAlchemy, setting up the database schema including members, payments, and expenses.
- **`service.py`**: Contains the core business logic for managing members, processing payments, and handling expenses.
- **`club_membership.db`**: An SQLite database that stores all the system data, with tables for members, payments, and expenses.

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install required packages:
`pip install sqlalchemy tkinter`
3. Clone this repository or download the files to your local machine.
4. Run `interface.py` for the CLI or `interface_gui.py` for the GUI.

## Usage
- **CLI**: Execute `python interface.py` and follow the on-screen prompts.
- **GUI**: Execute `python interface_gui.py`. The GUI will guide you through the various operations.

## Database Schema
- **Members**:
- `id`: Primary key, integer
- `name`: String
- `email`: String
- `username`: String
- `password`: String
- `unpaid_classes`: Integer
- `attendance`: Integer
- **Payments**:
- `id`: Primary key, integer
- `member_id`: Foreign key, integer
- `amount`: Float
- `date`: Date
- **Expenses**:
- `id`: Primary key, integer
- `description`: String
- `amount`: Float
- `date`: Date

## Contributing
If you encounter any issues or have suggestions for improvements, please feel free to contribute to the project or open an issue.

## License
This project is released under the MIT License.
