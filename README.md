# Claude Context Menu Installer

A beautiful Windows installer that adds Claude AI to your File Explorer context menu with multiple options.

![Windows](https://img.shields.io/badge/Windows-10%20%7C%2011-blue)
![Python](https://img.shields.io/badge/Python-3.6%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- **🎨 Beautiful GUI** - Modern, user-friendly graphical interface
- **🎯 Multiple Options** - Choose which menu items to install:
  - Open Claude here
  - Resume Claude here
  - Open Claude here as admin (Windows 11 + sudo)
  - Resume Claude here as admin (Windows 11 + sudo)
- **🔍 Auto-Detection** - Automatically checks if Claude and sudo are installed
- **🎨 Custom Icon** - Uses the official Claude icon in the context menu
- **🚀 One-Click Install** - Simple installation with admin privilege request
- **📦 Standalone** - Single executable with no dependencies

## 🖼️ Screenshots

The installer features a clean, modern interface with:
- Header with Claude branding
- Checkbox selection for each menu option
- Real-time system status (Claude installed, sudo available)
- Progress bar during installation
- Clear success/error messages

## 📋 Requirements

### For Using the Installer
- Windows 10 or Windows 11
- Administrator privileges (automatically requested)

### For Admin Options (Optional)
- Windows 11 (Build 26045+)
- Sudo enabled in Windows settings

### For Menu to Work
- Claude AI CLI installed ([Download](https://claude.ai))

## 🚀 Quick Start

### Installation

1. **Download** `InstallClaudeMenu.exe` from the [Releases](../../releases) page

2. **Double-click** the executable
   - Windows will ask for administrator permission
   - Click "Yes" to continue

3. **Select options** you want to install using checkboxes

4. **Click "Install"**

5. **Done!** Right-click in any folder to see the "Claude" menu

### Usage

After installation:

1. Open Windows File Explorer
2. Navigate to any folder
3. **Right-click** in an empty area
4. Select **"Claude"** to see all installed options
5. Choose your desired option

## 📖 Menu Options Explained

| Option | Command | Description |
|--------|---------|-------------|
| **Open Claude here** | `claude` | Opens a new Claude session in the current folder |
| **Resume Claude here** | `claude -r` | Resumes your last Claude session in the current folder |
| **Open Claude here as admin** | `sudo claude` | Opens Claude with administrator privileges |
| **Resume Claude here as admin** | `sudo claude -r` | Resumes last session with admin privileges |

## 🔧 Advanced

### Uninstall

Run the installer again with the uninstall argument:

```powershell
InstallClaudeMenu.exe uninstall
```

Or create a shortcut and add `uninstall` to the target path.

### Installing Claude

If Claude is not installed, the installer will notify you. To install Claude:

**PowerShell:**
```powershell
curl -fsSL https://claude.ai/install.cmd -o install.cmd; .\install.cmd; Remove-Item install.cmd
```

### Enabling Sudo (Windows 11)

For the "as admin" options to work:

1. Open **Settings**
2. Go to **System** > **For developers**
3. Enable **"Sudo"**

Or via PowerShell:
```powershell
sudo config --enable normal
```

## 🛠️ Building from Source

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Build Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/claude-context-menu.git
   cd claude-context-menu
   ```

2. **Install dependencies**
   ```bash
   pip install pyinstaller Pillow cairosvg
   ```

3. **Build the script**
   ```bash
   python build_final_script.py
   ```

4. **Create the executable**
   ```bash
   pyinstaller --onefile --noconsole --icon=claude_icon.ico --name="InstallClaudeMenu" --uac-admin install_claude_context_menu.py
   ```

5. **Find your executable**
   - Located in `dist/InstallClaudeMenu.exe`

## 📁 Project Structure

```
claude-context-menu/
├── dist/
│   ├── InstallClaudeMenu.exe     # Main executable
│   └── README.txt                # User guide
├── backup/                        # Backup files
├── claude_icon.ico                # Claude icon
├── install_claude_context_menu.py # Main installer script
└── README.md                      # This file
```

## 🔒 Security

- The installer requires **administrator privileges** to modify Windows Registry
- It only modifies registry keys under `HKEY_CLASSES_ROOT\Directory\Background\shell\Claude`
- Icon is stored in `C:\ProgramData\ClaudeMenu\claude_icon.ico`
- No telemetry, no data collection, completely offline after Claude is installed

## ⚠️ Troubleshooting

### Menu doesn't appear
- Refresh File Explorer (F5)
- Restart File Explorer via Task Manager
- Restart your computer

### "Claude is not installed" error
- Install Claude from [claude.ai](https://claude.ai)
- Or run the installer again and follow the installation prompt

### Admin options don't work
- Windows 11 (Build 26045+) required
- Enable sudo in Settings > System > For developers
- Or use regular "Open Claude here" instead

### Permission denied errors
- Make sure you're running as administrator
- Right-click the EXE → "Run as administrator"

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see below for details.

```
MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🙏 Acknowledgments

- [Claude AI](https://claude.ai) - The amazing AI assistant
- [Anthropic](https://anthropic.com) - For creating Claude
- Claude icon and branding belong to Anthropic

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Search existing [Issues](../../issues)
3. Open a new [Issue](../../issues/new) if needed

## 🗺️ Roadmap

- [ ] Add support for opening Claude in specific subdirectories
- [ ] Option to customize menu text
- [ ] Multi-language support
- [ ] Dark mode for installer UI
- [ ] Portable version (no admin required)

---

**Made with ❤️ for the Claude community**
