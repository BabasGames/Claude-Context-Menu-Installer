"""
Build script for Claude Context Menu Installer
Embeds the Claude icon into the installer script

Usage:
    python build_installer.py

Requirements:
    - Python 3.6+
    - claude_icon.ico in the same directory
"""

import base64
import os
import sys

def build_installer():
    """Build the standalone installer script with embedded icon"""

    # Check if icon file exists
    if not os.path.exists('claude_icon.ico'):
        print("ERROR: claude_icon.ico not found!")
        print("Please make sure claude_icon.ico is in the same directory.")
        sys.exit(1)

    print("Building Claude Context Menu Installer...")
    print("-" * 60)

    # Read the icon file
    print("Reading icon file...")
    with open('claude_icon.ico', 'rb') as f:
        icon_data = f.read()

    # Encode to base64
    print("Encoding icon to base64...")
    icon_base64 = base64.b64encode(icon_data).decode('utf-8')

    # Split into lines of 76 characters (standard base64 line length)
    icon_base64_lines = [icon_base64[i:i+76] for i in range(0, len(icon_base64), 76)]
    icon_base64_formatted = '\\n'.join(icon_base64_lines)

    # Read the template script
    print("Reading installer template...")
    if os.path.exists('install_claude_context_menu.py'):
        with open('install_claude_context_menu.py', 'r', encoding='utf-8') as f:
            template = f.read()

        # Check if it already has the icon embedded
        if 'CLAUDE_ICON_BASE64 = """' in template and len(template) > 60000:
            print("✓ Installer script already has icon embedded!")
            print(f"  Script size: {len(template)} bytes")
            return True

    print("ERROR: install_claude_context_menu.py not found or invalid!")
    print("Please run this script from the project directory.")
    sys.exit(1)

if __name__ == "__main__":
    print("=" * 60)
    print("Claude Context Menu Installer - Build Script")
    print("=" * 60)
    print()

    build_installer()

    print()
    print("=" * 60)
    print("Build complete!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("  1. Install PyInstaller: pip install pyinstaller")
    print("  2. Build the executable:")
    print("     pyinstaller --onefile --noconsole --icon=claude_icon.ico \\")
    print("                 --name=InstallClaudeMenu --uac-admin \\")
    print("                 install_claude_context_menu.py")
    print("  3. Find your executable in: dist/InstallClaudeMenu.exe")
    print()
