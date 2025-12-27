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

# Linux / macOS
source venv/bin/activate
```

### 3. 安裝相依套件
確保虛擬環境已啟用，然後安裝：
```bash
pip install -r requirements.txt
```

### 4. 選取 Python 解譯器 (VS Code)
若使用 VS Code，請務必將解譯器指向專案的虛擬環境，以確保執行與偵錯的正確性。

1.  開啟命令面板：
    *   **Windows/Linux**: `Ctrl+Shift+P`
    *   **macOS**: `Cmd+Shift+P`
2.  輸入並選擇 `Python: Select Interpreter`。
3.  在列表中選擇包含 `venv` 字樣的 Python 解譯器。VS Code 通常會自動偵測並推薦它。

選取後，VS Code 的整合終端機將會自動使用此虛擬環境。

### 5. 執行專案 
如何執行檔案：
```bash
python test_kepler_law.py
```
