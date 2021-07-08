Aarons-MBP:module1-introduction-to-sql aaron$ ls
README.md		rpg_db.sqlite3		rpg_db.sqlite3-journal
Aarons-MBP:module1-introduction-to-sql aaron$ python
Python 3.6.8 |Anaconda custom (64-bit)| (default, Dec 29 2018, 19:04:46) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sqlite3
>>> dir(sqlite3)
['Binary', 'Cache', 'Connection', 'Cursor', 'DataError', 'DatabaseError', 'Date', 'DateFromTicks', 'Error', 'IntegrityError', 'InterfaceError', 'InternalError', 'NotSupportedError', 'OperationalError', 'OptimizedUnicode', 'PARSE_COLNAMES', 'PARSE_DECLTYPES', 'PrepareProtocol', 'ProgrammingError', 'Row', 'SQLITE_ALTER_TABLE', 'SQLITE_ANALYZE', 'SQLITE_ATTACH', 'SQLITE_CREATE_INDEX', 'SQLITE_CREATE_TABLE', 'SQLITE_CREATE_TEMP_INDEX', 'SQLITE_CREATE_TEMP_TABLE', 'SQLITE_CREATE_TEMP_TRIGGER', 'SQLITE_CREATE_TEMP_VIEW', 'SQLITE_CREATE_TRIGGER', 'SQLITE_CREATE_VIEW', 'SQLITE_DELETE', 'SQLITE_DENY', 'SQLITE_DETACH', 'SQLITE_DROP_INDEX', 'SQLITE_DROP_TABLE', 'SQLITE_DROP_TEMP_INDEX', 'SQLITE_DROP_TEMP_TABLE', 'SQLITE_DROP_TEMP_TRIGGER', 'SQLITE_DROP_TEMP_VIEW', 'SQLITE_DROP_TRIGGER', 'SQLITE_DROP_VIEW', 'SQLITE_IGNORE', 'SQLITE_INSERT', 'SQLITE_OK', 'SQLITE_PRAGMA', 'SQLITE_READ', 'SQLITE_REINDEX', 'SQLITE_SELECT', 'SQLITE_TRANSACTION', 'SQLITE_UPDATE', 'Statement', 'Time', 'TimeFromTicks', 'Timestamp', 'TimestampFromTicks', 'Warning', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'adapt', 'adapters', 'apilevel', 'collections', 'complete_statement', 'connect', 'converters', 'datetime', 'dbapi2', 'enable_callback_tracebacks', 'enable_shared_cache', 'paramstyle', 'register_adapter', 'register_converter', 'sqlite_version', 'sqlite_version_info', 'threadsafety', 'time', 'version', 'version_info']
>>> conn = sqlite3.connect('rpg_db.sqlite3')
>>> dir(conn)
['DataError', 'DatabaseError', 'Error', 'IntegrityError', 'InterfaceError', 'InternalError', 'NotSupportedError', 'OperationalError', 'ProgrammingError', 'Warning', '__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'commit', 'create_aggregate', 'create_collation', 'create_function', 'cursor', 'enable_load_extension', 'execute', 'executemany', 'executescript', 'in_transaction', 'interrupt', 'isolation_level', 'iterdump', 'load_extension', 'rollback', 'row_factory', 'set_authorizer', 'set_progress_handler', 'set_trace_callback', 'text_factory', 'total_changes']
>>> help(conn.cursor)

>>> curs = conn.cursor()
>>> curs
<sqlite3.Cursor object at 0x109619dc0>
>>> dir(curs)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'arraysize', 'close', 'connection', 'description', 'execute', 'executemany', 'executescript', 'fetchall', 'fetchmany', 'fetchone', 'lastrowid', 'row_factory', 'rowcount', 'setinputsizes', 'setoutputsize']
>>> cleric_query = """SELECT character.character_id, character.name, cleric.using_shield
... FROM charactercreator_character AS character,
... charactercreator_cleric AS cleric
... WHERE character.character_id = cleric.character_ptr_id
... AND character.character_id = 166;"""
>>> cleric_query
'SELECT character.character_id, character.name, cleric.using_shield\nFROM charactercreator_character AS character,\ncharactercreator_cleric AS cleric\nWHERE character.character_id = cleric.character_ptr_id\nAND character.character_id = 166;'
>>> help(curs.execute)

>>> curs.execute(cleric_query)
<sqlite3.Cursor object at 0x109619dc0>
>>> curs.execute(cleric_query)
<sqlite3.Cursor object at 0x109619dc0>
>>> result = curs.execute(cleric_query)
>>> curs.fetchone()
(166, 'Deserunt', 0)
>>> curs = conn.cursor()
>>> curs
<sqlite3.Cursor object at 0x109a242d0>
>>> curs.execute(cleric_query)
<sqlite3.Cursor object at 0x109a242d0>
>>> curs.fetchall()
[(166, 'Deserunt', 0)]
>>> 
Aarons-MBP:module1-introduction-to-sql aaron$ python
Python 3.6.8 |Anaconda custom (64-bit)| (default, Dec 29 2018, 19:04:46) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sqlite3
>>> conn = sqlite3.connect('example.db')
>>> c = conn.cursor()
>>> 
>>> # Create table
... c.execute('''CREATE TABLE stocks
...              (date text, trans text, symbol text, qty real, price real)''')
<sqlite3.Cursor object at 0x100fc96c0>
>>> 
>>> # Insert a row of data
... c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
<sqlite3.Cursor object at 0x100fc96c0>
>>> 
>>> # Save (commit) the changes
... conn.commit()
>>> 
>>> # We can also close the connection if we are done with it.
... # Just be sure any changes have been committed or they will be lost.
... conn.close()
>>> exit()
Aarons-MBP:module1-introduction-to-sql aaron$ ls
README.md		rpg_db.sqlite3
example.db		rpg_db.sqlite3-journal
Aarons-MBP:module1-introduction-to-sql aaron$ ls -alh example.db 
-rw-r--r--  1 aaron  staff   8.0K Feb 18 10:34 example.db
Aarons-MBP:module1-introduction-to-sql aaron$ python
Python 3.6.8 |Anaconda custom (64-bit)| (default, Dec 29 2018, 19:04:46) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> import sqlite3
>>> conn = sqlite3.connect('example.db')
>>> c = conn.cursor()
>>> c.execute("SELECT * FROM stocks;")
<sqlite3.Cursor object at 0x10a7b16c0>
>>> c.fetchall()
[('2006-01-05', 'BUY', 'RHAT', 100.0, 35.14)]
>>> 