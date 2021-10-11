import statistics as stats
import pandas as pd
import csv
df = pd.read_csv(r"C:/Users/Admin/Downloads/Project 109/StudentsPerformance.csv")
math = df["math"].tolist()
math_mean = stats.mean(math)
math_median = stats.median(math)
math_mode = stats.mode(math)
math_std = stats.stdev(math)
math_1std_start, math_1std_end = math_mean - math_std, math_mean + math_std
math_2std_start, math_2std_end = math_mean - (2*math_std), math_mean + (2*math_std)
math_3std_start, math_3std_end = math_mean - (3*math_std), math_mean + (3*math_std)
math_1std_list = [result for result in math if result > math_1std_start and result < math_1std_end]
math_2std_list = [result for result in math if result > math_2std_start and result < math_2std_end]
math_3std_list = [result for result in math if result > math_3std_start and result < math_3std_end]
print("{} % of math score data lies within first standard deviation".format(len(math_1std_list)*100/len(math)))
print("{} % of math score data lies within second standard deviation".format(len(math_2std_list)*100/len(math)))
print("{} % of math score data lies within third standard deviation".format(len(math_3std_list)*100/len(math)))