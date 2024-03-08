from database_config import (get_database_config, connect_to_database, 
                             commit_transaction, close_cursor, close_connection)

# 主程式部分
db_config = get_database_config('config.ini')
cnxn = connect_to_database(db_config)
cursor = cnxn.cursor()

# 您的 DELETE 語句
delete_stmt = """
DELETE FROM dbo.Mobile_Contact
WHERE [HOME_ID] IN ('3685086')
"""

# DELETE FROM dbo.MOD_Contact
# WHERE MD_NUMBER IN ('M12345010', 'M12345011', 'M12345012');

# 執行 DELETE 語句
cursor.execute(delete_stmt)

# 提交事務
commit_transaction(cnxn)

# 關閉游標和連接
close_cursor(cursor)
close_connection(cnxn)
