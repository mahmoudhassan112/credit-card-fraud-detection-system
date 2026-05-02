
# import packages that we need to build the database

import sqlite3


# run the database engine before starting create tables
# we will call the database `logging.db `

engine = sqlite3.connect('logging.db' ,check_same_thread=False)

# generate a cursor for calling logging.db

cursor = engine.cursor()

# create a table called inference_logs for tracking each input , output , errors and so on ... 

cursor.execute("""
CREATE TABLE IF NOT EXISTS inference_logs(
id INTEGER PRIMARY KEY AUTOINCREMENT,
request_id TEXT,
timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
probability_output REAL,
prediction INTEGER,
latency_ms REAL,
throughput_rps REAL,
cpu_percent REAL,
memory_percent REAL,
status TEXT,
error_message TEXT
     ) 
    """)


engine.commit()
