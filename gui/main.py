import sys

from PySide6.QtWidgets import QApplication
from shell.shellWindow import ShellWindow


def main() -> int:
    app = QApplication(sys.argv)
    app.setApplicationName("HG Shell")

    window = ShellWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
