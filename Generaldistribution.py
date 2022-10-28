import numpy as np
class Distribution:
    
    def __init__(self, mu = 0, sigma =1):
        self.mean = mu
        self.stdev = sigma
        self.data = []
    
    def read_data_file(self, file_name):
        with open (file_name) as file:
            data_list = []
            while line := file.readline():
                data_list.append(int(line))
        self.data = data_list
    
