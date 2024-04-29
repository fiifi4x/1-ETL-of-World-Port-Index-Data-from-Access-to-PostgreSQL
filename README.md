SOFTWARE TO INSTALL BEFORE RUNNING THE CODE
Microsoft Access
PgAdmin (for PostgreSQL)  
Visual Studio
Python


SETTING UP MICROSOFT ACCESS CONNECTION TO PYTHON AND VICE VERSA
1. INSTALL REQUIRED PACKAGES; The pyodbc (python open database connectivity) is the python package to be installed, it enables python to recognize and establish connection wiith MS Access.  'pip install pyodbc' to install on your python IDE Terminal to install pyodbc.

2. Set up ODBC Data Source: Before connecting to the Access database, you need to set up an ODBC data source. ODBC (Open Database Connectivity) data sources serve as a standardized interface for connecting applications to various types of databases. The purpose of ODBC data sources is to provide a uniform way for applications to communicate with databases, regardless of the specific database management system (DBMS) being used. To install, follow these steps;
a) On Windows, go to Control Panel > Administrative Tools > Data Sources (ODBC).
b) In the ODBC Data Source Administrator window, go to the System DSN tab (for system-wide data sources) or the User DSN tab (for user-specific data sources).
c) Click on "Add" and select the appropriate driver for your version of Access (e.g., "Microsoft Access Driver (*.mdb, *.accdb)").
d) Follow the prompts to configure the data source, providing the path to your Access database file (.mdb or .accdb) and any other necessary information.
e) Give your data source a name and save the configuration.

RUNNING THE CODE
1. Clone the repository.
2. Open the folder in VS code
3. Run the main.py file


