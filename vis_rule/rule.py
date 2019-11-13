# python version 3.5x
import datetime
import numpy as np
import pandas as pd
import sys
import csv

visType = ["heat map", "bar chart", "line chart", "tree map"]
colTypes = ["<class 'str'>", "<class 'char'>", "<class 'int'>", "<class 'float'>", "<class 'double'>", "<class 'bool'>", "<class 'NoneType'>", "<class 'datetime.datetime'>"]

filename = "./test.csv"
dataSummary = []

KEYS = []
KEYS_COUNT = []
VIS = []
DIMENSION = "D"
MEASURE = "M"

def decompositionDataset(_filename):
	_summary = []

	# read csv file
	csv_reader = pd.read_csv(_filename)
	# get numbers of row & col
	numberOfRow = csv_reader.shape[0]
	numberOfCol = csv_reader.shape[1]
	dataset = np.array(csv_reader)

	_summary.append(dataset)
	_summary.append(numberOfRow)
	_summary.append(numberOfCol)

	_types = []
	for i in range(0, numberOfCol):
		_types.append(str(type(dataset[0][i])))

	_summary.append(_types)
	return _summary

def typeDeterminant(_rowNum, _val):
	remove_dup = list(set(_val))
	if _rowNum == len(remove_dup) or len(remove_dup) > 30:
		return MEASURE
	else:
		return DIMENSION