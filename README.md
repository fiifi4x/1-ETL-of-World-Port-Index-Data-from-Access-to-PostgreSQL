PROJECT DESCRIPTION
The project involves building a data pipeline to migrate data (known as World Port Index Data) from an old Access database to PostgreSQL (a modern relational database management system). 

 DATA DESCRIPTION
The World Port Index contains the location and physical characteristics of, and the facilities
and services offered by major ports and terminals world-wide.

HOW TO RUN THE CODE
To download the World Port Index Data (file is in .mdb format)

JNSTALLATION
This section shows how to install or set up the project. 
Dependencies = 
software, Python Libraries to install, python modules to import

SOFTWARE TO INSTALL
Microsoft Access - This database contains the World Port Index data to be migrated onto a postgres database.
PostgreSQL - 
VS CODE or any Python Supporting IDE (code was written in python)

SETTING UP MICROSOFT ACCESS CONNECTION TO PYTHON AND VICE VERSA
1. INSTALL REQUIRED PACKAGES; The pyodbc (python open database connectivity) is the python package to be installed, it enables python to recognize and establish connection wiith MS Access. To install 'pip install pyodbc' on your python IDE Terminal.
2. Set up ODBC Data Source: Before connecting to the Access database, you need to set up an ODBC data source. 
ODBC (Open Database Connectivity) data sources serve as a standardized interface for connecting applications to various types of databases. The purpose of ODBC data sources is to provide a uniform way for applications to communicate with databases, regardless of the specific database management system (DBMS) being used. To install, follow these steps;
a) On Windows, go to Control Panel > Administrative Tools > Data Sources (ODBC).
b) In the ODBC Data Source Administrator window, go to the System DSN tab (for system-wide data sources) or the User DSN tab (for user-specific data sources).
c) Click on "Add" and select the appropriate driver for your version of Access (e.g., "Microsoft Access Driver (*.mdb, *.accdb)").
d) Follow the prompts to configure the data source, providing the path to your Access database file (.mdb or .accdb) and any other necessary information.
e) Give your data source a name and save the configuration.

SETTING UP PGADMIN

  Usage: 
This section gives information on how to use the project. This could include code examples, API documentation, or command-line usage instructions.
Run the project from the main.py.


