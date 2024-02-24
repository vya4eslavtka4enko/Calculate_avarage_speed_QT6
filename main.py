import sys
from PyQt6.QtWidgets import (QApplication,QWidget,QLabel,QGridLayout,
                             QLineEdit,QPushButton,QComboBox)

class AvarageSpeed(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Avarage Speed Calculator')
        grid = QGridLayout()

        #Create Widgets
        distance = QLabel('Distance')
        self.edit_distance = QLineEdit()
        self.comboBox = QComboBox()
        self.comboBox.addItems(['miles','km'])

        time_label = QLabel('Time(hours)')
        self.edit_time = QLineEdit()

        calculate_button = QPushButton('Calculate')
        calculate_button.clicked.connect(self.calculate_average_speed)
        self.output_label = QLabel("kkk")

        #Add widgets to the grid
        grid.addWidget(distance,0,0)
        grid.addWidget(self.edit_distance,0,1)
        grid.addWidget(self.comboBox,0,3)
        grid.addWidget(time_label,1,0)
        grid.addWidget(self.edit_time,1,1)
        grid.addWidget(calculate_button,3,0,1,4)
        grid.addWidget(self.output_label,4,2)

        self.setLayout(grid)

    def calculate_average_speed(self):
        unit = ''
        dist =  self.edit_distance.text()
        time_jor = self.edit_time.text()
        avarage_speed_num = float(dist) / float(time_jor)
        if self.comboBox.currentText() == 'miles':
            unit = 'mph'
        else:
            unit = 'km'
        self.output_label.setText(f"Average Speed : {avarage_speed_num}  {unit}")


app = QApplication(sys.argv)
calculator = AvarageSpeed()
calculator.show()
sys.exit(app.exec())