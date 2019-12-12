import shapefile
import pandas as pd
from pyproj import Proj, transform

shp_path_node = './New_Daegu/Node.shp'
sf_node = shapefile.Reader(shp_path_node, encoding='cp949')
shp_path_link = './New_Daegu/Link.shp'
sf_link = shapefile.Reader(shp_path_link, encoding='cp949')

# pandas dataframe 생성
# 열 이름만 따로 처리
# node
fields_node = [x[0] for x in sf_node.fields][1:]
records_node = sf_node.records()
shps = [s.points for s in sf_node.shapes()]  # 노드는 좌표정보가 있다
# link
fields_link = [x[0] for x in sf_link.fields][1:]
records_link = sf_link.records()

# pandas dataframe 에 정보 기록
# node
node_dataframe = pd.DataFrame(columns=fields_node, data=records_node)
# 좌표계(coords)를 나타내는 열 추가
node_dataframe = node_dataframe.assign(coords=shps)
# link
link_dataframe = pd.DataFrame(columns=fields_link, data=records_link)
# 한글로 노드 이름 바꾸기 (decode)
for idx, row in node_dataframe.iterrows():
    if type(row['NODE_NAME']) == bytes:
        row['NODE_NAME'] = row['NODE_NAME'].decode('cp949')

# 좌표계 변환
# korea 2000/central belt 2010 (epsg:5186) to wgs84(epsg:4326)
inProj = Proj(init='epsg:5186')
outProj = Proj(init='epsg:4326')
latitude = []
longitude = []
for idx, row in node_dataframe.iterrows():
    x, y = row.coords[0][0], row.coords[0][1]  # korea 2000 좌표계
    nx, ny = transform(inProj, outProj, x, y)  # 새로운 좌표계
    latitude.append(ny)
    longitude.append(nx)
node_dataframe['latitude'] = latitude
node_dataframe['longitude'] = longitude
del node_dataframe['coords']  # 기존의 coords 삭제

# Gephi에서 사용하기 위해 이름 변경
node_dataframe.rename(columns={'NODE_ID': 'Id'}, inplace=True)
link_dataframe.rename(columns={'F_NODE': 'Source', 'T_NODE': 'Target'}, inplace=True)

# 저장
node_dataframe.to_csv("./csv_make/node.csv", mode='w')
link_dataframe.to_csv("./csv_make/link.csv", mode='w')
