import pandas as pd

node_csv = './csv_make/node.csv'
node_df = pd.read_csv(node_csv)
link_csv = './csv_make/link.csv'
link_df = pd.read_csv(link_csv)

# 전처리과정. 필요없는 부분 삭제
node_df = node_df.drop(['Unnamed: 0', 'NODE_TYPE', 'TURN_P', 'REMARK', 'USER_ID', 'WORKSTATE', 'DEPT_CODE', 'STNL_REG',
                        'TMPID', 'UPLOAD_ID'], 1)
link_df = link_df.drop(['Unnamed: 0', 'ROAD_USE', 'LANES', 'ROAD_RANK', 'ROAD_NAME', 'MULTI_LINK', 'CONNECT',
                        'REST_VEH', 'REST_W', 'REST_H', 'REMARK', 'USER_ID', 'WORKSTATE', 'DEPT_CODE', 'STNL_REG',
                        'ROAD_TYPE', 'ROAD_NO', 'TMPID', 'UPLOAD_ID', 'SOSFNODEID', 'SOSTNODEID', 'SHAPE_STLe'], 1)

node_df.to_csv("./csv_make2/node.csv", mode='w')
link_df.to_csv("./csv_make2/link.csv", mode='w')
