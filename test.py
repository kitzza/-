import pandas as pd

file_path = r'D:\A线程组\data.xlsx' # r 对路径进行转义 后面是路径
raw_data = pd.read_excel(file_path,header=0)  # header = 0表示第一行是表头，就自动去除了
print(raw_data)

data = raw_data.values   # 只读表中信息
print(data)
