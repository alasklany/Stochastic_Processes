import  pandas as pd
from utilities import Utilities
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

def get_basic_stats(dfname):
    print("Shape of dataframe is " + str(dfname.shape))
    print("Below are datatypes of columns in DF")
    print(dfname.dtypes.sort_values())
    print("Below are missing values in each column")
    print(dfname.isna().sum().sort_values())
    print("Below are the number of unique values taken by a column")
    print(dfname.nunique().sort_values())
    print("Below are some records in DF")
    print("Below is distribution of numeric variables")
    print(dfname.describe())
    print(dfname.head())


class ChurnBL:
    def __init__(self, trainer_path, tester_path):
        self.mTrainer = pd.read_csv(trainer_path)
        self.mTester = pd.read_csv(tester_path)
        self.trainer = self.mTrainer.copy()
        self.tester = self.mTester.copy()
        self.trainer = self.trainer.drop(['Unnamed: 0'], axis=1)
        self.tester = self.tester.drop(['Unnamed: 0'], axis=1)

        self.TestRatio = self.mTester.shape[0] / self.mTrainer.shape[0]

    def get_test_ratio(self):
        return self.TestRatio

    def get_head(self):
        return self.mTrainer.head()

    def get_feature_datatypes(self):
        return self.mTrainer.dtypes

    def apply_eda(self):
        yes_no_vars = ['churn', 'international_plan', 'voice_mail_plan']

        for indexer, varname in enumerate(yes_no_vars):
            self.trainer = Utilities.cat_to_binary(self.trainer, varname)
            self.tester = Utilities.cat_to_binary(self.tester, varname)

        self.trainer = self.trainer.drop(yes_no_vars, axis=1)
        self.tester = self.tester.drop(yes_no_vars, axis=1)

    def feature_creation(self):
        charge_vars = [x for x in self.trainer.columns if 'charge' in x]
        minutes_vars = [x for x in self.trainer.columns if 'minutes' in x]
        self.trainer = Utilities.create_cpm(self.trainer, charge_vars, minutes_vars)

       # self.trainer.boxplot(column='charge_per_minute', figsize=(20, 10,))

