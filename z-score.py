from cv2 import mean
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random 
import pandas as pd

df = pd.read_csv("data1.csv")
lst = df["math_score"].tolist()

popmean = st.mean(lst)
popstDev = st.stdev(lst)


def random_set_of_means(counter):
    meanlst = []
    for i in range(0,counter):
        rand = random.randint(0,len(lst)-1)
        val = lst[rand]
        meanlst.append(val)
    rand_means = st.mean(meanlst)
    return rand_means

mean_lst2 = []
for i in range(0,1000):
    set_of_mean = random_set_of_means(100)
    mean_lst2.append(set_of_mean)

st_dev = st.stdev(mean_lst2)
samplmean = st.mean(mean_lst2)
print("the sample distribution for standard deviation",st_dev)
print("the sample distribution for mean",samplmean)

first_standard_dev_start,first_standard_dev_end = rand_means + 
second_standard_dev_start,second_standard_dev_end = rand_means
third_standard_dev_start,third_standard_dev_end = rand_means

