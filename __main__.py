from PySide2.QtWidgets import QApplication
from observatory import Observatory
import sys


def main() -> None:
    app = QApplication([])
    window: Observatory = Observatory()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()