from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('untitled.ui', self)

        self.console_opened = True
        self.progress_value = 0
        self.matrix = [[4, 1, 5, 6, 3, 6], [4, 1, 5, 6, 3, 6], [4, 1, 5, 6, 3, 6]]

        if not self.console_opened:
            self.consoleButton.setText('Закрыть консоль')
            self.consoleText.hide()
        self.resultsWidjet.hide()
        self.calibrationWidjet.hide()

        self.consoleButton.clicked.connect(self.open_close_console)
        self.startButton.clicked.connect(self.start_calibration)
        self.continueButton.clicked.connect(self.continue_calibration)
        self.transferButton.clicked.connect(self.transfer_data)
        self.transferPZUButton.clicked.connect(self.save_in_equipment)

        types = ['Тип 1', 'Тип 2']
        views = ['Вид 1', 'Вид 2', 'Вид 3']
        ports = ['Порт 1', 'Порт 2', 'Порт3', 'Порт 4', 'Порт 5']
        speeds = ['Скорость 1', 'Скорость 2']

        self.eqvType.addItems(types)
        self.eqvView.addItems(views)
        self.comPort.addItems(ports)
        self.speedMean.addItems(speeds)

        print(self)

    def open_close_console(self):
        self.console_opened = not self.console_opened

        if self.console_opened:
            self.consoleButton.setText('Закрыть консоль')
            self.consoleText.show()
            self.setGeometry(50, 50, 800, 600)
        else:
            self.consoleButton.setText('Открыть консоль')
            self.consoleText.hide()
            self.setGeometry(50, 50, 800, 330)

        print(self.consoleButton)

    def start_calibration(self):
        self.progressBar.setValue(self.progress_value)
        self.resultsWidjet.hide()
        self.progress_value = 0
        self.calibrationWidjet.show()

    def continue_calibration(self):
        self.progress_value += 25
        self.progressBar.setValue(self.progress_value)
        if self.progress_value == 100:
            self.calibrationWidjet.hide()
            self.resultsWidjet.show()
            self.show_calculated_matrix()

    def show_calculated_matrix(self):
        text = ''
        for mat_str in self.matrix:
            for elem in mat_str:
                text += str(elem) + '  '
            text += '\n\n'
        self.calculatedText.setText(text)

    def transfer_data(self):
        text = ''
        for mat_str in self.matrix:
            for elem in mat_str:
                text += str(elem) + '  '
            text += '\n\n'
        self.equipmentText.setText(text)

    def save_in_equipment(self):
        text = ''
        for mat_str in self.matrix:
            for elem in mat_str:
                text += str(elem) + '  '
            text += '\n\n'
        self.equipmentText.setText(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())
