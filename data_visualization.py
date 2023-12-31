import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd 
import numpy as np 

score_data = pd.read_csv('diem_thi_thpt_2023_cleaned.csv', index_col='sbd')
# print(score_data)

def visualization_by_subject(dataframe, subject, fl=None):
    score_data = dataframe
    if fl==None:
        g = sns.histplot(data=score_data, x=score_data[subject], bins=30)
        g.set_title(f'{subject} score distribution')
        plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.show()
    else:
        g = sns.histplot(data=score_data[score_data['ma_ngoai_ngu']==fl], x=subject, bins=30)
        g.set_title(f'{subject} score distribution')
        plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.show()

def visualization_by_combination(dataframe, combination):
    score_data = dataframe
    g = sns.histplot(data=score_data, x=combination, bins=30)
    g.set_title(f'{combination} score distribution')
    plt.xticks([i for i in range(1,31)])
    plt.show()

def compare_two_subjects(dataframe, subject_1, subject_2):
    score_data = dataframe
    if subject_1!='ngoai_ngu' and subject_2!='ngoai_ngu':
        g = sns.scatterplot(data=score_data, x=subject_1, y=subject_2)
        g.set(xlabel=subject_1, ylabel=subject_2)
        plt.show()
    else:
        g = sns.scatterplot(data=score_data, x=subject_1, y=subject_2, hue='ma_ngoai_ngu')
        g.set(xlabel=subject_1, ylabel=subject_2)
        plt.show()

if __name__ == '__main__':
    pass
    # visualization_by_subject('ngoai_ngu', 'N2')
    # visualization_by_combination('A00_agg')
    # compare_two_subjects('toan', 'ngoai_ngu')