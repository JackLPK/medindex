import sqlite3
from pathlib import Path

class MedStore:
    def __init__(self, db_path, table):
        if not Path(db_path).absolute().exists():
            print('Database does not exist!')
            return 
        
        self.conn = None
        self.cursor = None
        self.table = table
        # print(table)
        self.connect(db_path)
        
        def check_table():
            _sql = '''
            SELECT name FROM sqlite_master
            WHERE type='table'
            ORDER BY NAME
            '''
            self.cursor.execute(_sql)
            tables_inside = self.cursor.fetchall()
            tables_inside = [_[0] for _ in tables_inside]
            if self.table not in tables_inside:
                print('{} not in {}'.format(self.table, tables_inside))
                
                self.disconnect()
                print('Error: Invalid table name')
            
        check_table()
        # self.nrows = None
        
    @property
    def nrows(self):
        _sql = '''SELECT COUNT(*) FROM "tbl_meds"'''
        self.cursor.execute(_sql)
        return int(self.cursor.fetchall()[0][0])
        
    def connect(self, db_path):
        try:
            print('connecting to:', db_path)
            # self.conn = sqlite3.connect(db_path)
            self.conn = sqlite3.connect(str(db_path))
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(e)
            print('Error connecting to database!')
        
            
    def disconnect(self):
        self.cursor.close()
        self.conn.close()
            
    def get_everything(self):
        _sql = '''
            SELECT * FROM tbl_meds
        '''
        self.cursor.execute(_sql)
        return self.cursor.fetchall()
    
    def search(self, search_string):
        _sql = ' SELECT * FROM tbl_meds WHERE s_name like "{}"'.format(
            search_string + '%'
        )
        self.cursor.execute(_sql)
        
        _o = self.cursor.fetchall()
        
        if _o:
            return _o
        else:
            return [('', '', '', '', '')]
        
    def get_column_names(self):
        _sql = '''SELECT name FROM pragma_table_info('tbl_meds')'''
        self.cursor.execute(_sql)
        # print(self.cursor.fetchall())
        column_names = self.cursor.fetchall()
        column_names = [_[0] for _ in column_names]
        return column_names
    