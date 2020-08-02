# encoding: utf-8
import sys
import serial
import serial.tools.list_ports
from PySide2.QtCore import QTimer, QTime, QRegExp
from PySide2.QtGui import QIcon, QRegExpValidator
from PySide2.QtWidgets import QWidget, QApplication, QMainWindow, QMessageBox
import pyqtgraph as pg
from data_deal import Data_Deal
from MainWindow import Ui_MainWindow

class Data_App(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # 创建串口实例对象
        self.serial = serial.Serial()
        # 创建 QTimer 实例对象
        self.timer1 = QTimer()
        self.timer2 = QTimer()
        self.time = QTime()
        self.now_time = ''
        # 创建显示窗口
        self.main_window = QMainWindow()
        self.setupUi(self.main_window)
        self.retranslateUi(self.main_window)
        # 正则表达式相关
        bit_3_validator = QRegExpValidator()
        bit_3_validator.setRegExp(QRegExp('[0-9]{1,3}'))
        self.fresh_waste_edit.setValidator(bit_3_validator)
        self.fresh_edit.setValidator(bit_3_validator)
        self.waste_edit.setValidator(bit_3_validator)
        self.blood_edit.setValidator(bit_3_validator)
        self.ultrafiltration_edit.setValidator(bit_3_validator)
        self.debug_send_edit.setValidator(bit_3_validator)

        # 储存所有存在的串口 字典
        self.Com_Dict = {}
        # 创建新csv文件标志
        self.create_file_flag = True
        self.write_data_flag = False
        # 要保存的当前的文件名
        self.now_file_name = None
        # 串口接收的字符串
        self.received_bit_data = None
        self.received_data = None
        # 图像对象
        self.fresh_pressure_plot = None
        self.waste_pressure_plot = None
        self.fresh_flow_plot = None
        self.waste_flow_plot = None
        self.blood_flow_plot = None
        self.artery_pressure_plot = None
        self.vein_pressure_plot = None
        self.weight_1_plot = None
        self.weight_2_plot = None
        self.weight_3_plot = None
        self.tmp_plot = None
        # self.ph_plot = None
        # self.temperature_plot = None
        # 保存收到的数据 list
        self.x = 0
        self.list_fresh_pressure = [0] * 10
        self.list_waste_pressure = [0] * 10
        self.list_fresh_flow = [0]*10
        self.list_waste_flow = [0]*10
        self.list_blood_flow = [0]*10
        self.list_artery_pressure = [0]*10
        self.list_vein_pressure = [0]*10
        self.list_weight_1 = [0]*10
        self.list_weight_2 = [0]*10
        self.list_weight_3 = [0]*10
        self.list_tmp = [0]*10
        # self.list_ph = [0]*1000
        # 接收到的最新的数据
        self.flag = ""
        self.fresh_pressure_data = 0
        self.waste_pressure_data = 0
        self.fresh_flow_data = 0
        self.waste_flow_data = 0
        self.blood_flow_data = 0
        self.artery_pressure_data = 0
        self.vein_pressure_data = 0
        self.weight_1_data = 0
        self.weight_2_data = 0
        self.weight_3_data = 0
        # 跨膜压
        self.tmp_data = 0
        self.initial_temperature_data = 0
        self.process_temperature_data = 0
        # self.ph_data = 0
        self.ultra_filtration_data = 0
        # 判断是否为首次接收到数据
        self.times = 0
        # 数据为空次数
        self.count_err = 0

        self.num = 0
        self.start_stop_flag = False

        self.init()
        self.port_check()

    # 按键关联

    def init(self):
        # 串口开关按钮
        self.open_serial_button.clicked.connect(self.port_operation)
        # 数据接收按钮
        self.receive_button.clicked.connect(self.data_begin)
        self.start_stop_button.clicked.connect(lambda: self.send_data(self.start_stop_button))
        # 数据发送按钮
        self.fresh_waste_forward_button.clicked.connect(lambda: self.send_data(self.fresh_waste_forward_button))
        self.fresh_waste_reverse_button.clicked.connect(lambda: self.send_data(self.fresh_waste_reverse_button))
        self.fresh_forward_button.clicked.connect(lambda : self.send_data(self.fresh_forward_button))
        self.fresh_reverse_button.clicked.connect(lambda: self.send_data(self.fresh_reverse_button))
        self.waste_forward_button.clicked.connect(lambda: self.send_data(self.waste_forward_button))
        self.waste_reverse_button.clicked.connect(lambda: self.send_data(self.waste_reverse_button))
        self.blood_forward_button.clicked.connect(lambda: self.send_data(self.blood_forward_button))
        self.blood_reverse_button.clicked.connect(lambda: self.send_data(self.blood_reverse_button))
        self.ultrafiltration_forward_button.clicked.connect(lambda: self.send_data(self.ultrafiltration_forward_button))
        self.ultrafiltration_reverse_button.clicked.connect(lambda: self.send_data(self.ultrafiltration_reverse_button))
        self.debug_send_button.clicked.connect(lambda: self.send_data(self.debug_send_button))
        # 全部设置按钮
        self.all_send_button.clicked.connect(lambda: self.send_data(self.all_send_button))
        # 停止按钮信号与槽
        self.fresh_waste_stop_button.clicked.connect(lambda: self.send_data(self.fresh_waste_stop_button))
        self.fresh_stop_button.clicked.connect(lambda: self.send_data(self.fresh_stop_button))
        self.waste_stop_button.clicked.connect(lambda: self.send_data(self.waste_stop_button))
        self.blood_stop_button.clicked.connect(lambda: self.send_data(self.blood_stop_button))
        self.ultrafiltration_stop_button.clicked.connect(lambda: self.send_data(self.ultrafiltration_stop_button))

        # 退出程序
        self.quit_button.clicked.connect(self.app_close)
        # 串口检测按钮
        self.find_port_button.clicked.connect(self.port_check)
        # 定时器接收数据
        self.timer1.timeout.connect(self.receive_data)
        self.timer2.timeout.connect(self.write_data)
        # PlotWidget 实例初始化
        self.dialysis_pressure_plot_view_init()
        self.flow_plot_view_init()
        self.pulse_plot_view_init()
        self.weight_plot_view_init()
        self.tmp_plot_view_init()
        # self.ph_plot_view_init()

    # 透析液压力趋势
    def dialysis_pressure_plot_view_init(self):
        self.dialysis_pressure_plot_view.setTitle("透析液压力（red新鲜液；blue废液）",
                                 color='008080',
                                 size='12pt', font='黑体')
        # 设置上下左右的label
        self.dialysis_pressure_plot_view.setLabel("left", "压强")
        self.dialysis_pressure_plot_view.setLabel("bottom", "采样点")

        # 设置自适应刻度范围
        self.dialysis_pressure_plot_view.enableAutoRange()

        # 显示表格线
        self.dialysis_pressure_plot_view.showGrid(x=True, y=True)


        # 背景色改为黑色
        self.dialysis_pressure_plot_view.setBackground('000000')

        # 实时显示应该获取 plotItem， 调用setData，
        # 这样只重新plot该曲线，性能更高
        self.fresh_pressure_plot = self.dialysis_pressure_plot_view.getPlotItem().plot(pen=pg.mkPen('r', width=2))
        self.waste_pressure_plot = self.dialysis_pressure_plot_view.getPlotItem().plot(pen=pg.mkPen('b', width=2))

    # 透析液流量
    def flow_plot_view_init(self):
        self.dialysis_flow_plot_view.setTitle("透析液流量(red新鲜；green废液；blue血液)",
                                                color='008080',
                                                size='12pt')
        # 设置上下左右的label
        self.dialysis_flow_plot_view.setLabel("left", "流量")
        self.dialysis_flow_plot_view.setLabel("bottom", "采样点")

        # 设置自适应刻度范围
        self.dialysis_flow_plot_view.enableAutoRange()

        # 显示表格线
        self.dialysis_flow_plot_view.showGrid(x=True, y=True)

        # 背景色改为白色
        self.dialysis_flow_plot_view.setBackground('000000')

        # 实时显示应该获取 plotItem， 调用setData，
        # 这样只重新plot该曲线，性能更高
        self.fresh_flow_plot = self.dialysis_flow_plot_view.getPlotItem().plot(pen=pg.mkPen('r', width=2))
        self.waste_flow_plot = self.dialysis_flow_plot_view.getPlotItem().plot(pen=pg.mkPen('g', width=2))
        self.blood_flow_plot = self.dialysis_flow_plot_view.getPlotItem().plot(pen=pg.mkPen('b', width=2))
    # 动静脉压力
    def pulse_plot_view_init(self):
        self.pluse_plot_view.setTitle("动静脉压（red动脉；blue静脉）",
                                      color='008080',
                                      size='12pt')
        # 设置上下左右的label
        self.pluse_plot_view.setLabel("left", "压强")
        self.pluse_plot_view.setLabel("bottom", "采样点")

        # 设置自适应刻度范围
        self.pluse_plot_view.enableAutoRange()

        # 显示表格线
        self.pluse_plot_view.showGrid(x=True, y=True)

        # 背景色改为黑色
        self.pluse_plot_view.setBackground('000000')

        # 实时显示应该获取 plotItem， 调用setData，
        # 这样只重新plot该曲线，性能更高
        self.artery_pressure_plot = self.pluse_plot_view.getPlotItem().plot(pen=pg.mkPen('r', width=2))
        self.vein_pressure_plot = self.pluse_plot_view.getPlotItem().plot(pen=pg.mkPen('b', width=2))

    # 重量显示
    def weight_plot_view_init(self):
        self.weight_plot_view.setTitle("重量（red重量1；green重量2；blue重量3）",
                                 color='008080',
                                 size='12pt')
        # 设置上下左右的label
        self.weight_plot_view.setLabel("left", "重量")
        self.weight_plot_view.setLabel("bottom", "采样点")

        # 设置自适应刻度范围
        self.weight_plot_view.enableAutoRange()

        # 显示表格线
        self.weight_plot_view.showGrid(x=True, y=True)

        # 背景色改为黑色
        self.weight_plot_view.setBackground('000000')

        # 实时显示应该获取 plotItem， 调用setData，
        # 这样只重新plot该曲线，性能更高
        self.weight_1_plot = self.weight_plot_view.getPlotItem().plot(pen=pg.mkPen('r', width=2))
        self.weight_2_plot = self.weight_plot_view.getPlotItem().plot(pen=pg.mkPen('g', width=2))
        self.weight_3_plot = self.weight_plot_view.getPlotItem().plot(pen=pg.mkPen('b', width=2))

    # TMP显示
    def tmp_plot_view_init(self):
        self.tmp_plot_view.setTitle("跨膜压",
                                 color='008080',
                                 size='12pt')
        # 设置上下左右的label
        self.tmp_plot_view.setLabel("left", "压强")
        self.tmp_plot_view.setLabel("bottom", "采样点")

        # 设置自适应刻度范围
        self.tmp_plot_view.enableAutoRange()

        # 显示表格线
        self.tmp_plot_view.showGrid(x=True, y=True)

        # 背景色改为黑色
        self.tmp_plot_view.setBackground('000000')

        # 实时显示应该获取 plotItem， 调用setData，
        # 这样只重新plot该曲线，性能更高
        self.tmp_plot = self.tmp_plot_view.getPlotItem().plot(pen=pg.mkPen('r', width=2))

    # ph 值
    # def ph_plot_view_init(self):
    #     self.ph_plot_view.setTitle("PH",
    #                              color='008080',
    #                              size='12pt')
    #     # 设置上下左右的label
    #     self.ph_plot_view.setLabel("left", "PH值")
    #     self.ph_plot_view.setLabel("bottom", "采样点")
    #
    #     # 设置自适应刻度范围
    #     self.ph_plot_view.enableAutoRange()
    #
    #     # 显示表格线
    #     self.ph_plot_view.showGrid(x=True, y=True)
    #
    #     # 背景色改为白色
    #     self.ph_plot_view.setBackground('w')
    #
    #     # 实时显示应该获取 plotItem， 调用setData，
    #     # 这样只重新plot该曲线，性能更高
    #     self.ph_plot = self.ph_plot_view.getPlotItem().plot( pen=pg.mkPen('r', width=2))

    # 串口检测
    def port_check(self):
        # 检测所有存在的串口，将信息存储在字典中
        port_list = list(serial.tools.list_ports.comports())
        self.port_combo_box.clear()
        if len(port_list) == 0:
            self.port_combo_box.addItem("无串口")
            QMessageBox.information(self, "信息", "未检测到串口！")
        else:
            self.port_combo_box.clear()
            for port in port_list:
                self.Com_Dict["%s" % port[0]] = "%s" % port[1]
                self.port_combo_box.addItem(port[0])

    # 串口开关操作
    def port_operation(self):

        if self.serial.is_open:
            self.close_serial_port()
        else:
            self.open_serial_port()


    # 开始接收数据
    def data_begin(self):
        if self.serial.is_open:
            # 打开串口接收定时器，周期为100ms
            if not self.timer1.isActive():
                self.timer1.start(100)
                self.receive_button.setText("接收中")
            else:
                return None
        else:
            QMessageBox.information(self, 'Port', '串口未打开！')

    # 打开串口
    def open_serial_port(self):
        # 从QComboBox的当前值获取端口号
        self.serial.port = self.port_combo_box.currentText()
        # self.serial.port = "COM1"
        if not self.serial.port:
            QMessageBox.critical(self, '错误', '没有选择串口')
        # 设置串口通信参数
        self.serial.baudrate = 115200
        self.serial.bytesize = 8
        self.serial.stopbits = 1
        self.serial.parity = "N"
        # timeout默认为None，若不设置timeout，当使用read()时，一直会等到读取指定的字节数为止
        self.serial.timeout = 2
        self.serial.write_timeout = 2
        # 设置软件控制流开关
        self.serial.rtscts = True
        self.serial.dsrdtr = True
        try:
            self.serial.rts = True
            self.serial.dtr = True
            self.serial.open()
        except:
            QMessageBox.critical(self, "Port Error", "此串口不能被打开！")
            return None
        # 判断是否有串口打开
        if self.serial.is_open:
            # 打开串口接收定时器，周期为100ms
            self.statusbar.showMessage("打开串口成功")
            self.open_serial_button.setText("关闭串口")
            self.port_status_label.setStyleSheet("background-color:green")
            self.port_status_label.style().polish(self.port_status_label)  # 刷新样式

    # 关闭串口
    def close_serial_port(self):
        self.timer1.stop()
        self.timer2.stop()
        self.serial.close()

        if not self.serial.is_open:
            self.open_serial_button.setText("打开串口")
            self.port_status_label.setStyleSheet("background-color:gray")
            self.port_status_label.style().polish(self.port_status_label)  # 刷新样式
            self.receive_button.setText("接收")
            self.statusbar.showMessage("串口已关闭")

    def write_data(self):
        self.write_data_flag = True

    # 接收数据
    def receive_data(self):

        try:
            num = self.serial.inWaiting()
        except:
            self.close_serial_port()
            QMessageBox.critical(self, "Read Error", "读取输入缓存区数据的字节数失败！")
            return None
        print(self.serial.rts)
        print(num)
        self.received_bit_data = self.serial.read(101)
        print(self.received_bit_data)
        self.received_data = self.received_bit_data.decode('ascii')
        # 已经接收到信息说明系统已经开启，将系统状态改为开启
        if self.times == 0:
            self.system_status_button(self.start_stop_button)
            self.times += 1
        print(self.received_data)
        self.statusbar.showMessage("数据读取成功，准备处理数据")
        self.data_operation()

    # 处理接收的数据
    def data_operation(self):
        # 这里的received_data指的是发送端发送的字符串
        if len(self.received_data) == 101:
            self.count_err = 0
            try:
                # 使用获得的数据字符串创建一个对象
                self.now_time = self.time.currentTime().toString()
                data = Data_Deal(self.received_data + self.now_time)
                # 对数据进行分析处理，并获得一个元祖类型的返回值，以便后面更新显示
                self.flag, self.artery_pressure_data, self.vein_pressure_data, self.fresh_pressure_data,\
                    self.waste_pressure_data, self.fresh_flow_data, self.waste_flow_data, self.blood_flow_data,\
                    self.tmp_data, self.weight_1_data, self.weight_2_data, self.weight_3_data,\
                    self.initial_temperature_data, self.process_temperature_data,\
                    self.ultra_filtration_data = data.get_num()
            except ValueError:
                self.statusbar.showMessage('数据解析失败！准备重新接收')
                self.serial.reset_input_buffer()
                return None
            # 判断需要创建一个新的csv还是直接存入当前csv(每次数据接收成功都会为之创建一个csv文件)
            if self.create_file_flag:
                self.create_file_flag = False
                # 每一分钟保存一次数据
                self.timer2.start(300000)
                # 当前成功接收的数据所存放的文件名
                self.now_file_name = self.now_time[0:2] + "_" + self.now_time[3:5] + "_" + self.now_time[6:8] + ".csv"
                data.create_csv(self.now_file_name)
            else:
                if self.write_data_flag and self.flag == 'tmp':
                    self.write_data_flag = False
                    data.store_to_csv(self.now_file_name)

            if self.flag == 'tmp':
                print('数据格式没问题')
                self.show_update()
                self.statusbar.showMessage("数据格式正确，更新数据完毕")
                # print("更新数据完毕")
            else:
                self.statusbar.showMessage('数据格式不正确！准备重新接收')
                # QMessageBox.information(self, "信息", "数据格式不正确！准备重新接收")
                self.serial.reset_input_buffer()
                return None
        elif len(self.received_data) == 0:
            self.count_err += 1
            print(self.count_err)
            if self.count_err == 5:
                self.close_serial_port()
                QMessageBox.information(self, "信息", "没有读到数据！")
                return None
            return None
        else:
            self.count_err = 0
            self.statusbar.showMessage("读取的数据的字节数不对！准备重新接收")
            # QMessageBox.information(self, "信息", "读取的数据的字节数不对！准备重新接收")
            self.serial.reset_input_buffer()
            return None
            # pass #self.textBrowser.insertPlainText("Data Receive Error: Wrong Data Length!\r\n")
            # QMessageBox.critical(self, "Data Length Error", "从输入缓存区读取数据的字节数不对！")

    # 更新所有显示
    def show_update(self):
        # 更新文本显示区域的数据

        self.fresh_pressure_value.setText(str(self.fresh_pressure_data))
        self.waste_pressure_vlue.setText(str(self.waste_pressure_data))
        self.fresh_flow_value.setText(str(self.fresh_flow_data))
        self.waste_flow_value.setText(str(self.waste_flow_data))
        self.blood_flow_value.setText(str(self.blood_flow_data))
        self.artery_pressure_value.setText(str(self.artery_pressure_data))
        self.vein_pressure_value.setText(str(self.vein_pressure_data))
        # 电导值已经去掉，目前显示重量，未在右边显示
        # self.ph_value.setText(str(self.ph_data))
        self.initial_temperature_value.setText(str(self.initial_temperature_data))
        self.process_temperature_value.setText(str(self.process_temperature_data))
        self.ultrafiltration_show_value.setText(str(self.ultra_filtration_data))
        # 更新数据

        self.x += 1

        # self.list_fresh_pressure[:-1] = self.list_fresh_pressure[1:]
        # self.list_fresh_pressure[-1] = self.fresh_pressure_data
        # self.list_fresh_pressure.insert(0, 0)
        # self.list_waste_pressure[:-1] = self.list_waste_pressure[1:]
        # self.list_waste_pressure[-1] = self.waste_pressure_data
        # self.list_waste_pressure.insert(0, 0)
        # self.list_fresh_flow[:-1] = self.list_fresh_flow[1:]
        # self.list_fresh_flow[-1] = self.fresh_flow_data
        # self.list_waste_flow[:-1] = self.list_waste_flow[1:]
        # self.list_waste_flow[-1] = self.waste_flow_data
        # self.list_blood_flow[:-1] = self.list_blood_flow[1:]
        # self.list_blood_flow[-1] = self.blood_flow_data
        # self.list_artery_pressure[:-1] = self.list_artery_pressure[1:]
        # self.list_artery_pressure[-1] = self.artery_pressure_data
        # self.list_vein_pressure[:-1] = self.list_vein_pressure[1:]
        # self.list_vein_pressure[-1] = self.vein_pressure_data
        # self.list_weight_1[:-1] = self.list_weight_1[1:]
        # self.list_weight_1[-1] = self.weight_1_data
        # self.list_weight_2[:-1] = self.list_weight_2[1:]
        # self.list_weight_2[-1] = self.weight_2_data
        # self.list_weight_3[:-1] = self.list_weight_3[1:]
        # self.list_weight_3[-1] = self.weight_3_data
        # self.list_tmp[:-1] = self.list_tmp[1:]
        # self.list_tmp[-1] = self.tmp_data
        # self.list_ph[:-1] = self.list_ph[1:]
        # self.list_ph[-1] = self.ph_data
        self.list_fresh_pressure.append(self.fresh_pressure_data)
        self.list_waste_pressure.append(self.waste_pressure_data)
        self.list_fresh_flow.append(self.fresh_flow_data)
        self.list_waste_flow.append(self.waste_flow_data)
        self.list_blood_flow.append(self.blood_flow_data)
        self.list_artery_pressure.append(self.artery_pressure_data)
        self.list_vein_pressure.append(self.vein_pressure_data)
        self.list_weight_1.append(self.weight_1_data)
        self.list_weight_2.append(self.weight_2_data)
        self.list_weight_3.append(self.weight_3_data)
        self.list_tmp.append(self.tmp_data)

        # 更新图形
        self.fresh_pressure_plot.setData(self.list_fresh_pressure)
        # 给图形对象设置新坐标值，# 参数1：x 轴起点坐标 参数2：y 轴起点坐标
        self.fresh_pressure_plot.setPos(self.x, 0)
        self.waste_pressure_plot.setData(self.list_waste_pressure)
        self.waste_pressure_plot.setPos(self.x, 0)
        self.fresh_flow_plot.setData(self.list_fresh_flow)
        self.fresh_flow_plot.setPos(self.x, 0)
        self.waste_flow_plot.setData(self.list_waste_flow)
        self.waste_flow_plot.setPos(self.x, 0)
        self.blood_flow_plot.setData(self.list_blood_flow)
        self.blood_flow_plot.setPos(self.x, 0)
        self.artery_pressure_plot.setData(self.list_artery_pressure)
        self.artery_pressure_plot.setPos(self.x, 0)
        self.vein_pressure_plot.setData(self.list_vein_pressure)
        self.vein_pressure_plot.setPos(self.x, 0)
        self.weight_1_plot.setData(self.list_weight_1)
        self.weight_1_plot.setPos(self.x, 0)
        self.weight_2_plot.setData(self.list_weight_2)
        self.weight_2_plot.setPos(self.x, 0)
        self.weight_3_plot.setData(self.list_weight_3)
        self.weight_3_plot.setPos(self.x, 0)
        self.tmp_plot.setData(self.list_tmp)
        self.tmp_plot.setPos(self.x, 0)
        # self.ph_plot.setData(self.list_ph)
        # self.ph_plot.setPos(self.x, 0)

    # 发送数据
    def send_data(self, btn):

        if self.serial.is_open:
            bytes_data = self.button_effort(btn)
            if bytes_data != "" and len(bytes_data) > 5:
                self.serial.write(bytes_data)
                # QMessageBox.information(self, 'Send', '发送数据成功！')
            else:
                QMessageBox.critical(self, "Send Error", "发送数据不能为空！")
        else:
            QMessageBox.information(self, 'Port', '串口未打开')
            return None

    # 判断不同的按钮做出不同的响应
    def button_effort(self, btn):
        data = ""
        # 发送新鲜液废旧液数据
        if btn.objectName() == "fresh_waste_forward_button":
            data = "ffw" + self.fresh_waste_edit.text() + "\r\n"
            return data.encode('ascii')
        elif btn.objectName() == "fresh_waste_reverse_button":
            data = "rfw" + self.fresh_waste_edit.text() + "\r\n"
            return data.encode('ascii')
        elif btn.objectName() == "fresh_waste_stop_button":
            data = "fwaStop\r\n"
            return data.encode('ascii')
        elif btn.objectName() == "fresh_forward_button":
            data = "ffr" + self.fresh_edit.text() + "\r\n"
            return data.encode('ascii')
        elif btn.objectName() == "fresh_reverse_button":
            data = "rfr" + self.fresh_edit.text() + "\r\n"
            return data.encode('ascii')
        elif btn.objectName() == "fresh_stop_button":
            data = "freStop\r\n"
            return data.encode('ascii')
        elif btn.objectName() == "waste_forward_button":
            data = "fwa" + self.waste_edit.text() + "\r\n"
            return data.encode('ascii')
        elif btn.objectName() == "waste_reverse_button":
            data = "rwa" + self.waste_edit.text() + "\r\n"
            return data.encode('ascii')
        elif btn.objectName() == "waste_stop_button":
            data = "wasStop\r\n"
            return data.encode('ascii')
        elif btn.objectName() == "blood_forward_button":
            data = "fbl" + self.blood_edit.text() + "\r\n"
            return data.encode('ascii')
        elif btn.objectName() == "blood_reverse_button":
            data = "rbl" + self.blood_edit.text() + "\r\n"
            return data.encode('ascii')
        elif btn.objectName() == "blood_stop_button":
            data = "bloStop\r\n"
            return data.encode('ascii')
        elif btn.objectName() == "ultrafiltration_forward_button":
            data = "ful" + self.ultrafiltration_edit.text() + "\r\n"
            return data.encode('ascii')
        elif btn.objectName() == "ultrafiltration_reverse_button":
            data = "rul" + self.ultrafiltration_edit.text() + "\r\n"
            return data.encode('ascii')
        elif btn.objectName() == "ultrafiltration_stop_button":
            data = "ultStop\r\n"
            return data.encode('ascii')
        elif btn.objectName() == "debug_send_button":
            data = "cmd" + self.debug_send_edit.text() + "\r\n"
            return data.encode('ascii')
        # elif btn.objectName() == "all_send_button":
        #     data = self.get_all_cmd()
        #     if data != "":
        #         reply = QMessageBox.question(None, "检查命令", data, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        #         if reply == QMessageBox.Yes:
        #             data += "\r\n"
        elif btn.objectName() == "start_stop_button":
            self.system_status_button(btn)
            if self.start_stop_flag:
                data = "systemStart\r\n"
                return data.encode('ascii')
            elif not self.start_stop_flag:
                data = "systemStop\r\n"
                return data.encode('ascii')
        else:
            return data
        #
        # if data != '':
        #     return data.encode('ascii')


    # 发送所有命令的按钮指令(还有用吗？)
    # def get_all_cmd(self):
    #     data = ""
    #     if self.fresh_waste_edit.text() != "":
    #         data += "fwl" + self.fresh_waste_edit.text()
    #     if self.ultrafiltration_edit.text() != "":
    #         data += "ult" + self.ultrafiltration_edit.text()
    #     if self.blood_pump_edit.text() != "":
    #         data += "bpu" + self.blood_pump_edit.text()
    #     if self.debug_send_edit.text() != "":
    #         data += self.debug_send_edit.text()
    #
    #     if data == "":
    #         QMessageBox.critical(self, "警告", "未设置参数", QMessageBox.Yes)
    #     return data

    # 更改系统开启与停止按钮的样式
    def system_status_button(self, btn):
        if btn.text() == "开启":
            self.start_stop_flag = True
            btn.setText('停止')
            self.system_status_label.setStyleSheet('background-color:green')
            self.system_status_label.style().polish(self.system_status_label)
        elif btn.text() == "停止":
            self.start_stop_flag = False
            btn.setText('开启')
            self.system_status_label.setStyleSheet('background-color:gray')
            self.system_status_label.style().polish(self.system_status_label)

    # 关闭系统
    def app_close(self):
        self.close_serial_port()
        quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myShow = Data_App()
    myShow.main_window.show()
    sys.exit(app.exec_())
