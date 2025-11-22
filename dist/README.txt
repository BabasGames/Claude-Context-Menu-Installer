================================================================================
                    CLAUDE CONTEXT MENU INSTALLER
================================================================================

FILE: InstallClaudeMenu.exe (7.6 MB)

This file is COMPLETELY STANDALONE:
- No Python installation required
- Claude icon is embedded
- Works on Windows 10 & 11
- Automatically requests admin privileges


INSTALLATION (ULTRA SIMPLE!)
=============================

1. Double-click on "InstallClaudeMenu.exe"

2. Windows will ask:
   "Do you want to allow this app to make changes..."

   -> Click "Yes"

3. Follow the on-screen instructions:
   - The installer will check if Claude is installed
   - If not, you can install it during setup
   - It will also check if 'sudo' is available

4. Done!


WHAT GETS INSTALLED
====================

A "Claude" menu in Windows Explorer with 4 options:

  1. Open Claude here          -> Opens Claude in current folder
  2. Resume Claude here        -> Resumes last Claude session
  3. Open Claude here as admin -> Opens Claude with admin rights
  4. Resume Claude here as admin -> Resumes with admin rights


USAGE
=====

After installation:

1. Open File Explorer
2. Go to any folder
3. Right-click in an empty area of the folder
4. Select "Claude" to see all 4 options
5. Choose the option you want!


REQUIREMENTS
============

CLAUDE MUST BE INSTALLED:
  - The installer will offer to install Claude for you
  - Or install manually: https://claude.ai

FOR ADMIN OPTIONS (sudo):
  - Windows 11 (Build 26045+) required
  - Enable sudo: Settings > System > For developers > Enable 'Sudo'
  - Or run in PowerShell: sudo config --enable normal


UNINSTALL
=========

Double-click InstallClaudeMenu.exe again and run:

Method 1 (CMD/PowerShell):
   InstallClaudeMenu.exe uninstall

Method 2 (Create a shortcut):
   - Right-click on exe -> Create shortcut
   - Properties -> Add " uninstall" after path
   - Double-click the shortcut


IMPORTANT NOTES
===============

- You MUST click "Yes" when Windows asks for permission
- Claude icon appears in the context menu
- Compatible with Windows 10 & 11
- No internet connection needed (after Claude is installed)
- 100% standalone file


TROUBLESHOOTING
===============

Menu entry doesn't appear:
  -> Refresh Explorer (F5)
  -> Or restart File Explorer
  -> Or restart your computer

"Claude is not installed" error:
  -> Install Claude: https://claude.ai
  -> Or run the installer again and choose "Yes" when asked

Admin options don't work:
  -> Windows 11 (Build 26045+) required
  -> Enable sudo in Settings > System > For developers
  -> Or use regular "Open Claude here" instead


WHAT EACH OPTION DOES
======================

Open Claude here:
  - Opens a new Claude session in the selected folder
  - Command: claude

Resume Claude here:
  - Resumes your last Claude session in the selected folder
  - Command: claude -r
  - Useful for continuing previous work

Open Claude here as admin:
  - Opens Claude with administrator privileges
  - Command: sudo claude
  - Requires Windows 11 with sudo enabled

Resume Claude here as admin:
  - Resumes last session with administrator privileges
  - Command: sudo claude -r
  - Requires Windows 11 with sudo enabled


================================================================================
Free to distribute - No warranty provided
================================================================================
