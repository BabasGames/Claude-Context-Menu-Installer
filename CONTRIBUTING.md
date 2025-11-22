# Contributing to Claude Context Menu Installer

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- Git
- Windows 10/11 (for testing)

### Setting Up Development Environment

1. **Fork the repository**
   ```bash
   # Click the "Fork" button on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/claude-context-menu.git
   cd claude-context-menu
   ```

3. **Install dependencies**
   ```bash
   pip install pyinstaller Pillow cairosvg
   ```

4. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📝 Development Guidelines

### Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and small

### Commit Messages

Use clear and descriptive commit messages:

- `feat: Add support for custom menu text`
- `fix: Resolve admin privilege detection issue`
- `docs: Update README with new screenshots`
- `refactor: Simplify icon embedding logic`

### Testing

Before submitting a PR:

1. **Test the installer**
   - Build the executable
   - Test installation on clean Windows system
   - Test all menu options
   - Test uninstallation

2. **Test both admin and non-admin scenarios**

3. **Test on Windows 10 and 11 if possible**

## 🔨 Building the Project

### Build the installer script

```bash
python build_installer.py
```

### Create the executable

```bash
pyinstaller --onefile --noconsole --icon=claude_icon.ico --name=InstallClaudeMenu --uac-admin install_claude_context_menu.py
```

### Test the executable

```bash
cd dist
# Right-click InstallClaudeMenu.exe -> Run as administrator
```

## 📋 Pull Request Process

1. **Update documentation**
   - Update README.md if you add features
   - Add comments to your code
   - Update CHANGELOG if present

2. **Test thoroughly**
   - Test installation
   - Test all menu options
   - Test uninstallation
   - Test on both Windows 10 and 11

3. **Create the PR**
   - Write a clear description of changes
   - Reference any related issues
   - Include screenshots if UI changed

4. **Respond to feedback**
   - Address review comments
   - Make requested changes
   - Be patient and respectful

## 🐛 Reporting Bugs

When reporting bugs, please include:

- **Windows version** (10 or 11, build number)
- **Steps to reproduce**
- **Expected behavior**
- **Actual behavior**
- **Screenshots** if applicable
- **Error messages** (exact text)

## 💡 Suggesting Features

When suggesting features:

- **Check existing issues** to avoid duplicates
- **Describe the use case** clearly
- **Explain why** it would be useful
- **Consider implementation** if possible

## 📁 Project Structure

```
claude-context-menu/
├── install_claude_context_menu.py  # Main installer script
├── claude_icon.ico                 # Claude icon
├── build_installer.py              # Build script
├── README.md                       # Main documentation
├── LICENSE                         # MIT License
├── CONTRIBUTING.md                 # This file
└── dist/                           # Distribution files
    ├── InstallClaudeMenu.exe       # Built executable
    └── README.txt                  # User guide
```

## 🔐 Security

- Never commit sensitive information
- Test code for security vulnerabilities
- Report security issues privately to maintainers

## 📜 Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Accept constructive criticism
- Focus on what's best for the community

## ❓ Questions?

- Open an issue for general questions
- Check existing issues first
- Be specific and provide context

## 🎉 Recognition

Contributors will be recognized in:
- GitHub contributors page
- Release notes (for significant contributions)
- README acknowledgments (for major features)

Thank you for contributing! 🙏
