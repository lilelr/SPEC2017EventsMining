
import os
import numpy as np
import pandas as pd
import pickle

class Evaluate(object):
    def __init__(self):
        self.a = None
        self.data_path = './'
        self.program= 'it-95-L2-norm'
        # self.algorithm_name = 'PregelOperation'
        self.result_data = 'result_'+self.program+'.pkl'

    def evaluate_fun(self):
        result_data_path = os.path.join(self.data_path, self.result_data)
        result = pickle.load(open(result_data_path, 'rb'))
        value = result['result']
        Err = value[0]
        Indices = value[1]
        Events_Name = value[2]
        Importances = value[3]

        Min_index = Err.index(min(Err))
        Min_indices = Indices[Min_index]
        Min_eventname = Events_Name[Min_index]
        Min_importances = Importances[Min_index]

        print(Err)

        df = pd.DataFrame()
        df['error'] = Err[Min_index]
        df['indices'] = Min_indices
        df['event name'] = Min_eventname
        df['importances'] = Min_importances
        # df.to_csv('result_'+self.algorithm_name+'.csv')


        writer = pd.ExcelWriter(self.result_data.replace('.pkl', '.xlsx'))
        Itera = 14
        for Min_index in range(Itera):
            Min_err = Err[Min_index]
            Min_indices = Indices[Min_index]
            Min_eventname = Events_Name[Min_index]
            Min_importances = Importances[Min_index]
            df['error'] = Min_err
            df['indices'] = Min_indices
            df['event name'] = Min_eventname
            df['importances'] = Min_importances
            df.to_excel(writer, 'Sheet'+str(Min_index))

    def build(self):
        self.evaluate_fun()

if __name__ == '__main__':
    evaluate = Evaluate()
    evaluate.__init__()
    evaluate.evaluate_fun()