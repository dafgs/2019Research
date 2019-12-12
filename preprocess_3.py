import pandas as pd
from haversine import haversine, Unit

node_csv = './csv_make2/node.csv'
node_df = pd.read_csv(node_csv)
link_csv = './csv_make2/link.csv'
link_df = pd.read_csv(link_csv)

weight = []
Source_name = []
Source_coords = []
Target_name = []
Target_coords = []

for idx, row in link_df.iterrows():
    for in_idx, in_row in node_df.iterrows():
        if row.Source == in_row.Id:
            Source_name.append(in_row.NODE_NAME)
            Source_coords.append((in_row.latitude, in_row.longitude))
        if row.Target == in_row.Id:
            Target_name.append(in_row.NODE_NAME)
            Target_coords.append((in_row.latitude, in_row.longitude))

    weight.append(haversine(Source_coords[-1], Target_coords[-1], unit=Unit.KILOMETERS)/row.MAX_SPD)

link_df['weight'] = weight
link_df['Source_name'] = Source_name
link_df['Source_coords'] = Source_coords
link_df['Target_name'] = Target_name
link_df['']