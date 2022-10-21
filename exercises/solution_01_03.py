import numpy as np
import pandas as pd

from pandas_profiling import ProfileReport

column_names = ['ID','clump_thickness','cell_size','cell_shape','adhesion','epithelial_size','bare_nuclei','bland_chromatin','norm_nucleoli','mitoses','class']
data = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data',names=column_names)
ProfileReport(data)