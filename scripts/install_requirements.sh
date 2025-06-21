#!/bin/bash
# install_requirements.sh
# Installs the appropriate requirements for the current platform

set -e

echo "📦 Installing Atlas requirements for the current platform..."

# Detect platform
if [[ "$OSTYPE" == "darwin"* ]]; then
    PLATFORM="macOS"
    PLATFORM_FILE="requirements-macos.txt"
    PYTHON_VERSION="3.13"
else
    PLATFORM="Linux"
    PLATFORM_FILE="requirements-linux.txt"
    PYTHON_VERSION="3.12"
fi

echo "🔍 Detected platform: $PLATFORM"
echo "🐍 Expected Python version: $PYTHON_VERSION"

# Check Python version
CURRENT_PYTHON_VERSION=$(python --version | cut -d' ' -f2 | cut -d'.' -f1-2)
if [[ "$CURRENT_PYTHON_VERSION" != "$PYTHON_VERSION" ]]; then
    echo "⚠️  Warning: Current Python version ($CURRENT_PYTHON_VERSION) does not match expected version ($PYTHON_VERSION)"
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ Installation aborted"
        exit 1
    fi
fi

# Install options
echo "Select installation options:"
echo "1) Core requirements only"
echo "2) Core + development tools"
echo "3) Full installation (core + development + additional tools)"
read -p "Option (1-3): " option

case $option in
    1)
        echo "📦 Installing core requirements..."
        pip install -r "$PLATFORM_FILE"
        ;;
    2)
        echo "📦 Installing core requirements and development tools..."
        pip install -r "$PLATFORM_FILE" -r requirements-dev.txt
        ;;
    3)
        echo "📦 Installing all requirements..."
        pip install -r "$PLATFORM_FILE" -r requirements-dev.txt
        
        # Additional platform-specific tools
        if [[ "$PLATFORM" == "macOS" ]]; then
            echo "📦 Installing macOS-specific tools..."
            pip install py2app rumps
        elif [[ "$PLATFORM" == "Linux" ]]; then
            echo "📦 Installing Linux-specific tools..."
            pip install docker
        fi
        ;;
    *)
        echo "❌ Invalid option"
        exit 1
        ;;
esac

echo "✅ Installation complete"
echo ""
echo "To verify installation, run:"
echo "  ./scripts/sync_requirements.sh"