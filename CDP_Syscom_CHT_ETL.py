import subprocess

# 設定要執行的執行檔的路徑（假設它在當前資料夾中）
# exe_path = "hinet測試\Debug\Syscom_CHT_ETL.exe"

exe_path = "mobile測試\Debug\Syscom_CHT_ETL.exe"


# exe_path = "MOD測試\Debug\Syscom_CHT_ETL.exe"

# 使用subprocess模組執行執行檔
subprocess.run(exe_path, shell=True)
