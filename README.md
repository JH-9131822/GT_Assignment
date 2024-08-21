This is the code base for GT's assignment. Follow the instructions below to deploy and test on your local machine.

**Prerequisites**
- Python 3.12 installed

**Step 1: Install Required Modules for Python**
- Open Window's Command Prompt
- Enter the command to install FastAPI: "pip install fastapi"
- Enter the command to install nvicorn: "pip install uvicorn"
- Enter the command to install requests: "pip install requests"
- Enter the command to install pydantic: "pip install pydantic" 

**Step 2: Install MySQL**
- Setup MySQL server in your local machine
- Recommended tool: MySQL Workbench (https://dev.mysql.com/downloads/workbench/)

**Step 3: Download the codes to your machine**
- Download the codes and save into your local machine

**Step 4: Setup MySQL Connection and Database**
- Create a connection in MySQL, and record the username, password, and host.
- Create a new database (or schema) and remember the database name.

**Step 5: Enter the Database information**
- Navigate to the directory where you saved the code
- Open the "assignment/modules" directory
- Edit the file "db.py" with any text editor
- Enter the database information accordingly: Username, password, connection, and database name.
- Save and close the file

**Step 6: Setup Database and Tables Using the Provided Script**
- Open Window's Command Prompt
- Navigate to the directory where you saved the code
- Open the "assignment" directory
- Enter the command: "py setupdb.py" to run the setup script

**Step 7: Launch the Python Application**
- Open Window's Command Prompt
- Navigate to the directory where you saved the code
- Open the "assignment" directory
- Enter the command: "py main.py" to run the application

**Step 8: Start the API Server (Optional)**
- Open Window's Command Prompt
- Navigate to the directory where you saved the code
- Open the "assignment" directory
- Enter the command: "uvicorn api-server:app --host 127.0.0.1"

**Step 9: Start the API Testing Script (Optional)**
- Open Window's Command Prompt
- Navigate to the directory where you saved the code
- Open the "assignment" directory
- Enter the command: "py api-test.py"
