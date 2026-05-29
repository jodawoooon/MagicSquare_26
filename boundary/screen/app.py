"""PyQt application entry point."""

import sys

from PyQt6.QtWidgets import QApplication

from boundary.screen.main_window import MainWindow


def main() -> int:
    """Launch the MagicSquare GUI."""
    app = QApplication(sys.argv)
    app.setApplicationName("MagicSquare")
    app.setStyle("Fusion")

    window = MainWindow()
    window.show()

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
