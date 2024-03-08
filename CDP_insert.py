import os
from database_config import (get_database_config, connect_to_database, 
                             commit_transaction, close_cursor, close_connection)

print(os.getcwd())
# 主程式部分
db_config = get_database_config('config.ini')
cnxn = connect_to_database(db_config)
cursor = cnxn.cursor()

# 您的 INSERT 語句
insert_stmt = """
INSERT [dbo].[Mobile_Contact] ([HOME_ID],[Mobile_Renter_Phone],[NAME], [Sex], [SSN],[Mobile_Contact_Email],[END_DATE]) 
VALUES (3685098,  N'919971020',N'A-15', N'女性', N'A987654328',N'testA15@gmail.com',CAST(N'2023-11-17' AS Date))

"""


# 執行 INSERT 語句
cursor.execute(insert_stmt)

# 提交事務
commit_transaction(cnxn)

# 關閉游標和連接
close_cursor(cursor)
close_connection(cnxn)