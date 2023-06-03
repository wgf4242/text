
import os
import pandas as pd

# 遍历文件夹中的 CSV 文件，并将它们读入到一个列表中
csv_list = []
for file_name in os.listdir('your_dir'):
    if file_name.endswith('.csv'):
        csv_path = os.path.join('your_files', file_name)
        df = pd.read_csv(csv_path)
        df['source'] = file_name
        csv_list.append(df)

# 将列表中的所有 DataFrame 合并成一个
merged_df = pd.concat(csv_list, ignore_index=True, sort=False)

# 定义 original_cols 变量，并初始化为合并后 DataFrame 的列名列表
original_cols = merged_df.columns.tolist()

# 遍历合并后的 DataFrame 中的所有列名，并将新的列名添加到 DataFrame 中
for col in merged_df.columns:
    if col not in original_cols:
        merged_df = merged_df.reindex(columns=original_cols + [col])

# 将合并后的 DataFrame 写入到一个新的 CSV 文件中
merged_df.to_csv('leaked.csv', index=False)