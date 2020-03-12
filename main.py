import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
import qdarkstyle
from controllerUI import Ui_MainWindow
import pyqtgraph as pg
from PyMCP2221A import PyMCP2221A

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # self.I2C_Setup()
        # self.Labels()
        self.Buttons()
        # self.CheckBoxes()

        self.timer = QtCore.QTimer()
        # self.timer.timeout.connect(self.Labels)
        self.timer.start(1000)


    def I2C_Setup(self):
        self.mcp2221 = PyMCP2221A.PyMCP2221A()
        self.mcp2221.Reset()
        self.mcp2221 = PyMCP2221A.PyMCP2221A()
        self.mcp2221.I2C_Init()


    def Read_I2C(self,addr,register,num_bytes):
        self.mcp2221.I2C_Write_No_Stop(addr, [0x00, register])
        read = list(device.I2C_Read_Repeated(addr, num_bytes))
        read.reverse()
        return read

    def Write_FPGA(self,addr,register,data):
        self.mcp2221.I2C_Write(addr, ([0x00, register] + data ))

    def Labels(self):

        self.mcp2221.I2C_Write(0x4C, [0x01, 0x1F])
        self.mcp2221.I2C_Write(0x4C, [0x02, 0x01])  # write to Trigger register

        # write no stop used when wanting to read back after writing with no delay
        # write to internal temperature MSB and read back two bytes ( this will return the LSB found at 0x05)
        self.mcp2221.I2C_Write_No_Stop(0x4C, [0x04])
        read = self.mcp2221.I2C_Read_Repeated(0x4C, 2)

        # bit shift MSB by 8 bits and add to create 16 bit number. use conversion values as found in datasheet
        Temp = ((((read[0] & 0x1F) << 8) + read[1]) * 0.0625)

        # access Vcc MSB and readback MSB and LSB
        self.mcp2221.I2C_Write_No_Stop(0x4C, [0x0E])
        read = self.mcp2221.I2C_Read_Repeated(0x4C, 2)
        Vcc = ((((read[0] & 0x7F) << 8) + read[1]) * 305.18e-6 + 2.5)

        # access V1 , read back MSB and LSB(0x07)
        self.mcp2221.I2C_Write_No_Stop(0x4C, [0x06])
        read = self.mcp2221.I2C_Read_Repeated(0x4C, 2)
        V1 = ((((read[0] & 0x7F) << 8) + read[1]) * 305.18e-6)*-10.

        # access V2 , read back MSB and LSB(0x09)
        self.mcp2221.I2C_Write_No_Stop(0x4C, [0x08])
        read = self.mcp2221.I2C_Read_Repeated(0x4C, 2)
        V2 = ((((read[0] & 0x7F) << 8) + read[1]) * 305.18e-6)*10.1

        # access V3 , read back MSB and LSB(0x0B)
        self.mcp2221.I2C_Write_No_Stop(0x4C, [0x0A])
        read = self.mcp2221.I2C_Read_Repeated(0x4C, 2)
        V3 = ((((read[0] & 0x7F) << 8) + read[1]) * 305.18e-6)*2

        # access V4 , read back MSB and LSB(0x0D)
        self.mcp2221.I2C_Write_No_Stop(0x4C, [0x0C])
        read = self.mcp2221.I2C_Read_Repeated(0x4C, 2)
        V4 = ((((read[0] & 0x7F) << 8) + read[1]) * 305.18e-6)*2


        self.V1_Label.setText('+24V Voltage: {:.2f}V'.format(V2))
        self.V2_Label.setText('-24V Voltage: {:.2f}V'.format(V1))
        self.V3_Label.setText('+5VA Voltage: {:.2f}V'.format(V4))
        self.V4_Label.setText('+5VD Voltage: {:.2f}V'.format(V3))
        self.Temperature_label.setText('Temperature: {:.2f}'.format(Temp))

    def Buttons(self):
        self.pushButton.clicked.connect(self.ADC)
        self.Pulse_Length_Button.clicked.connect(self.Send_Pulse_Length)
        self.Pulse_Delay_Button.clicked.connect(self.Send_Pulse_Delay)
        self.pushButton_2.clicked.connect(self.I2C_Setup)

    def ADC(self):
        self.curve1 = self.graphicsView.plot(
            pen=pg.mkPen('y', width=1), name='yellow plot')
        self.curve1.setData([1, 2, 3], [1, 2, 3])

    def CheckBoxes(self):
        self.checkBox.stateChanged.connect(self.Send_all_to_HB)
        self.checkBox_2.stateChanged.connect(self.Change_Load)

    def Send_all_to_HB(self, state):
        if state == Qt.Checked:
            self.Write_FPGA(addr = 0x40, register = 0x04, data =  [0xFF, 0xFF, 0xFF, 0xFF])

        else:
            self.Write_FPGA(addr = 0x40,register = 0x04, data = [0x00, 0x00, 0x00, 0x00])

    def Change_Load(self, state):
        if state == Qt.Checked:
            self.Write_FPGA(addr = 0x40, register = 0x05, data =  [0xFF, 0xFF, 0xFF, 0xFF])

        else:
            self.Write_FPGA(addr = 0x40,register = 0x05, data = [0x00, 0x00, 0x00, 0x00])


    def Send_Pulse_Length(self):
        value = self.Pulse_Length_lineEdit.text()

        if len(value)>0:
            if int(value) < 400 and int(value) > 0:
                pass #I2C Write etc

    def Send_Pulse_Delay(self):
        value = self.Pulse_Delay_lineEdit.text()
        if len(value)> 0:
            if int(value) < 200 and int(value) > 0:
                pass 

    def Update(self):
        print('hello')



def main():

    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.setStyle("plastique")

    file = 'G:/Users/j/jospence/Documents/Current Source/Interfacing_with_CS/Current_Source_GUI/Current_Source_GUI/'

    # app.setStyleSheet(open(file + 'QDarkOrangeStyleSheet.css').read())
    window = MainWindow()
    window.show()
    app.exec()
    # sys.exit(app.exec_())

if __name__ == '__main__':  # if we're running file directly and not importing it

    main()
