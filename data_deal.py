import pandas as pd

class Data_Deal(object):
    def __init__(self, data_str):
        self.target = data_str
        self.time = ""
        self.flag = ""
        self.artery_pressure = 0
        self.vein_pressure = 0
        self.fresh_pressure = 0
        self.waste_pressure = 0
        self.fresh_flow = 0
        self.waste_flow = 0
        self.blood_flow = 0
        self.tmp = 0
        self.weight_1 = 0
        self.weight_2 = 0
        self.weight_3 = 0
        self.initial_temperature = 0
        self.process_temperature = 0
        self.ultra_filtration = 0

    # 解码各数据要素，便于显示和绘图
    def get_num(self):
        print('在数据解析函数中')
        # print(self.target[0:3])
        # print(self.target[3:10])
        # print(self.target[17:24])
        # print(self.target[24:31])
        # print(self.target[31:38])
        # print(self.target[38:45])
        # print(self.target[45:52])
        self.flag = self.target[0:3]
        self.artery_pressure = float(self.target[3:10])
        self.vein_pressure = float(self.target[10:17])
        self.fresh_pressure = float(self.target[17:24])
        self.waste_pressure = float(self.target[24:31])
        self.fresh_flow = float(self.target[31:38])
        self.waste_flow = float(self.target[38:45])
        self.blood_flow = float(self.target[45:52])
        self.tmp = float(self.target[52:59])
        self.weight_1 = float(self.target[59:66])
        self.weight_2 = float(self.target[66:73])
        self.weight_3 = float(self.target[73:80])
        self.initial_temperature = float(self.target[80:87])
        self.process_temperature = float(self.target[87:94])
        self.ultra_filtration = float(self.target[94:101])
        self.time = self.target[101:]
        return self.flag, self.artery_pressure, self.vein_pressure, self.fresh_pressure, self.waste_pressure, \
                    self.fresh_flow, self.waste_flow, self.blood_flow, self.tmp, self.weight_1, self.weight_2, \
                    self.weight_3, self.initial_temperature, self.process_temperature, self.ultra_filtration

    # def storage_to_txt(self):
    #     file = open("Data.txt", "a")
    #     file.write(self.target + "\n")
    #     file.close()

    def create_csv(self, file_name):
        df = pd.DataFrame(data={'Time': self.time,
                                'Artery_pressure': self.artery_pressure,
                                'Vein_pressure': self.vein_pressure,
                                'Fresh_pressure': self.fresh_pressure,
                                'Waste_pressure': self.waste_pressure,
                                'Fresh_flow': self.fresh_flow,
                                'Waste_flow': self.waste_flow,
                                'Blood_flow': self.blood_flow,
                                'Tmp': self.tmp,
                                'Weight_1': self.weight_1,
                                'Weight_2': self.weight_2,
                                'Weight_3': self.weight_3,
                                'Initial_temperature': self.initial_temperature,
                                'Process_temperature': self.process_temperature,
                                'Ultra_filtration': self.ultra_filtration}, index=[1])
        df.to_csv('./DataStore/' + file_name, index=False)

    def store_to_csv(self, file_name):
        data_buff = pd.DataFrame(data={'Time': self.time,
                                       'Artery_pressure': self.artery_pressure,
                                       'Vein_pressure': self.vein_pressure,
                                       'Fresh_pressure': self.fresh_pressure,
                                       'Waste_pressure': self.waste_pressure,
                                       'Fresh_flow': self.fresh_flow,
                                       'Waste_flow': self.waste_flow,
                                       'Blood_flow': self.blood_flow,
                                       'Tmp': self.tmp,
                                       'Weight_1': self.weight_1,
                                       'Weight_2': self.weight_2,
                                       'Weight_3': self.weight_3,
                                       'Initial_temperature': self.initial_temperature,
                                       'Process_temperature': self.process_temperature,
                                       'Ultra_filtration': self.ultra_filtration}, index=[1])
        data_buff.to_csv('./DataStore/' + file_name, mode='a', encoding='utf-8',
                         header=False, index=False)
