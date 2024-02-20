from GUI import *
from data import read_data


def main():
    file = "ExamResults.xlsx"
    data = read_data(file)
    # print(module_marks("CSE101", data))
    # print(exclusive_averages("CSE101", data))
    app = GUI(data)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()