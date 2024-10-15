from PyQt5.QtWidgets import QApplication
from gui import DNAAnalyzer
import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    analyzer = DNAAnalyzer()
    analyzer.show()
    sys.exit(app.exec_())