# 半自動化測試程式

此專案是一個半自動化測試程式，用於手動輸入資料並執行測試，以檢查推送到 Azure 上的資料是否正確。

## 環境需求

Python 3.9
pyodbc
configparser

## 安裝指南

首先，確保您已經安裝了 Python 3.9。接著，您可以使用 pip 安裝所需的套件：

```bash
pip install pyodbc configparser
```

## 使用說明

設定資料庫連接：修改 config.ini 檔案，以設定資料庫連接資訊。

插入資料：執行 CDP_insert.py 以插入資料到資料庫中。

刪除資料：執行 CDP_delete.py 以刪除資料庫中的特定資料。

執行 ETL 程式：執行 CDP_Syscom_CHT_ETL.py 以執行 ETL 程式，並檢查資料是否正確推送到 Azure。 (這邊的ETL執行程式為主要推送資料的程式)CDP_Syscom_CHT_ETL是公司內部檔案 由其他同仁撰寫不便上傳

## 注意事項

請確保在執行程式前已正確設定資料庫連接資訊。
根據您的需求修改 SQL 語句。
