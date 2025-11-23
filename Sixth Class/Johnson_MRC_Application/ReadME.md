# Prerequisites

- Python (3.x)
- MySQL Server
- mysql-connector-python package

## How to start

The `Starter_Code_Week_4+5.sql` file is not a database you connect to, it's a script that builds one.

## MySQL Workbench

1. Open **MySQL Workbench**
2. Connect to your MySQL server
3. Go to **File → Open SQL Script**
4. Select `Starter_Code_Week_4+5.sql`
5. Click the **⚡ Execute** button (or press Ctrl+Shift+Enter)
6. Wait for it to finish - you'll see "mrc" database created

## Connect to Workbench From Python

> [!IMPORTANT]
> Create a `config.py`in the root and replace them with yours e.g. below:

```python
config = {
    'username': 'root',
    'password': 'password',
    'database': 'mrc',   
    'host': 'localhost',
    'port': 3306
}
```

From the View File if your Visual Code press play ▶️ button.
It will ask for the information from your config file. If you have done the connections step your defaults are valid and you can just press enter through the connection information requests.

Information will display.
