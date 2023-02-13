# import pandas as pd
# import numpy as np
# import os
# import sys
# 获取ppts文件夹中所有的文件名
# pptsfiles = []
# for file in os.listdir('ppts'):
#     pptsfiles.append(f'ppts/{file}')



# table = {
#         "ppts":pptsfiles,
#     }
# df = pd.DataFrame(table)
# print(df['ppts'])
# 获取ppts文件夹中所有的文件名 end

import pandas as pd
pd.read_excel('index.xlsx').to_html('index.html')