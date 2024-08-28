import pandas as pd


def generate_txt_files_from_excel(excel_file):
    # 读取Excel文件
    df = pd.read_excel(excel_file, header=None)  # header=None表示没有列标题，读取所有行

    # 遍历每一行数据
    for index, row in df.iterrows():
        # 获取数据内容
        data_content = row[0]  # 假设每一行只有一列数据

        # 生成文件名
        file_name = f'output_files/ESN_{data_content}.txt'

        # 写入TXT文件
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(str(data_content))  # 写入数据内容
        print(f"生成文件: {file_name}")


# 示例调用
excel_file_path = 'files/ESN.xlsx'  # 替换为你的Excel文件路径
generate_txt_files_from_excel(excel_file_path)