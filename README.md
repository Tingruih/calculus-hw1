# 安裝
**需要 Python 3.8 或更高的版本**。

以下說明包含：如何安裝 Python（Windows / macOS / Linux）、建立與啟用虛擬環境，以及安裝專案相依套件。

### 0. 安裝 Python
如果你尚未安裝 Python，請依照你的作業系統選擇下列步驟。

- Windows
	1. 到官方下載頁面：https://www.python.org/downloads/windows/ 下載最新的 Python 3.x 安裝程式。
	2. 執行安裝程式時，務必勾選「Add Python to PATH」。
	3. 安裝完成後，可在 PowerShell 中驗證：
	```powershell
	python --version
	```

- macOS
	1. 建議使用 Homebrew（如果已安裝 Homebrew）：
	```bash
	brew install python
	```
	2. 或至 https://www.python.org/downloads/macos/ 下載安裝程式。
	3. 驗證安裝：
	```bash
	python3 --version
	```

- Linux (以 Ubuntu/Debian 為例)
	```bash
	sudo apt update; sudo apt install -y python3 python3-venv python3-pip
	python3 --version
	```

### 1. 下載專案
首先下載專案的原始碼：
```bash
git clone https://github.com/Tingruih/calculus-hw1.git
cd calculus-hw1
```

### 2. 建立與啟用虛擬環境（建議）
使用虛擬環境可以避免與系統或其他專案的套件衝突。

- 建立虛擬環境：
```bash
python -m venv venv
```

- 啟用虛擬環境：
```powershell
# Windows (PowerShell)
venv\Scripts\Activate.ps1

# 如果使用 cmd.exe
venv\Scripts\activate.bat

# Linux / macOS
source venv/bin/activate
```

注意：預設 PowerShell 可能會阻擋執行腳本（Execution Policy），若啟用時出現錯誤，可暫時允許本機執行：以系統管理員權限執行 PowerShell，然後執行：
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

啟用後，提示字首會顯示 (venv) 表示已啟用。

### 3. 安裝相依套件
確保虛擬環境已啟用，然後安裝：
```bash
pip install -r requirements.txt
```

若你需要將目前環境的套件版本鎖定成檔案（供他人使用）：
```bash
pip freeze > requirements.txt
```

### 4. 執行專案 (範例)
此專案主要範例檔案可能不同，下面只示範如何以 Python 執行模組：
```bash
python kepler_law.py
```

### 5. .gitignore 建議
建議把虛擬環境目錄與常見暫存檔加入 `.gitignore`，例如：
```
venv/
__pycache__/
*.pyc
.env
```

---

若你希望，我可以替你直接把 `venv/` 加入現有的 `.gitignore`，並（如果 venv 已被 commit）示範如何從 git 中移除。 