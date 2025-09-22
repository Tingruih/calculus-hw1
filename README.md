# 安裝
 **需要 Python 3.8 或更高的版本**

 ### 1. 下載專案
 首先下載專案的源代碼，可以使用以下的指令取得：
 ```bash
 git clone https://github.com/Tingruih/calculus-hw1.git
 cd caculus-hw1
 ```

 ### 2. 使用虛擬環境 (可選，但強烈建議使用)
 在安裝專案之前，建議使用虛擬環境來隔離專案的依賴套件，以避免和其他專案的依賴套件衝突。
 #### 使用 Python 內建的虛擬環境套件
 ```bash
 python -m venv venv
 ```
 #### 使用第三方虛擬環境管理工具
 ```bash
 pip install virtualenv

 virtualenv venv
 ```
 接著，啟用虛擬環境：
 ```bash
 # Windows
 venv\Scripts\activate

 # Linux/macOS
 source venv/bin/activate
 ```

 ### 3. 安裝套件
 下載專案所需要的依賴套件。
 ```bash
 pip install -r requirements.txt
 ```

 ### 4. 執行專案
 安裝套件並設定環境變數後，即可執行專案！
 ```bash
 python main.py
 ```