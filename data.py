import math

import pandas as pd
from math import isnan


def _validate_module_name(module):
    """
    Checks if the string is a valid name for a module.
    -Raises TypeError for invalid inputs;
    -Raises ValueError for incorrect module names;
    :param module: (string) module name
    """
    if type(module) != str:
        raise TypeError
    if module not in ["CSE101", "CSE102", "CSE103", "CSE104", "CSE105", "CSE106", "CSE107", "CSE108", "CSE109",
                      "CSE110",
                      "CSE111", "CSE112", "CSE113", "CSE114", "CSE115", "CSE116", "CSE117", "CSE118", "CSE119",
                      "CSE120"]:
        raise ValueError


def read_data(fileName):
    """
    Reads student data from an Excel file.
    :param fileName: name of the file
    :return: (pandas dataframe) student marks (Student ID x Module name)
    """
    try:
        data = pd.read_excel(fileName, skiprows=2)
    except FileNotFoundError:
        print(f"The file {fileName} could not be found.")
    else:
        return data


def module_marks(module, dataset):
    """
    Gives marks obtained in the specified module for all students enrolled.
    :param module: (string) module name
    :param dataset: (pandas dataframe) dataset with student marks (Student ID x Module Name)
    :return: (pandas series) marks for that module
    """
    _validate_module_name(module)

    return dataset[module]


def exclusive_averages(module, dataset):
    """
    Gives the average marks of the students across all enrolled subjects EXCLUDING the specified module.
    :param module: (string) module name
    :param dataset: (pandas dataframe) dataset with student marks (Student ID x Module Name)
    :return: (pandas series) the averages for all students
    """
    _validate_module_name(module)

    def average(list):
        # Internal function that returns the average of non NaN values in a list.

        sum = 0
        count = 0
        for element in list:
            if not isnan(element):
                sum += element
                count += 1
        return sum / count

    result = dataset.apply(lambda row: average(row.drop([module, 'Student IDs'])), axis=1, result_type='reduce')
    return result
