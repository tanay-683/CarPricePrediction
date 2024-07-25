import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.layers import Dense, Input
from keras import ops
import keras
from sklearn.preprocessing import PowerTransformer

class PreprocessData:
    def fit_transform(self,X=None, Y=None):
        LabelEncoder = LabelEncoder()
        df["Owner"] = LabelEncoder.fit_transform(df["Owner"])
