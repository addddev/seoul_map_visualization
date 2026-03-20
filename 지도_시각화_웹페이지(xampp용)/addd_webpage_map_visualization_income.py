import os, json
import pandas as pd
import plotly.express as px
#(csv파일 다운받은 경로 입력) 반드시 경로 변경!
file_path = "/opt/lampp/htdocs/seoul_income.csv"

# CSV 파일을 데이터프레임으로 읽어오기
merged_df = pd.read_csv(file_path)
column_names = merged_df.columns.tolist()
merged_df['행정동_전체_명'] = merged_df['시도명'] + ' ' + merged_df['시군구명'] + ' ' + merged_df['행정동_코드_명']

# 반드시 경로 변경!(다운받은 경로로!)
with open('/opt/lampp/htdocs/hangjeongdong_서울특별시.geojson', 'r') as f:
    seoul_geo = json.load(f)

    
mapbox_style = "carto-positron"
center = {"lat": 37.5665, "lon": 126.9780}
zoom = 10
opacity = 0.5

# 서울 행정동 경계 그리기
fig = px.choropleth_mapbox(merged_df, 
                           geojson=seoul_geo, 
                           locations='행정동_전체_명', 
                           color='월_평균_소득_금액',
                           featureidkey='properties.adm_nm',
                           center={"lat": 37.563383, "lon": 126.996039},
                           mapbox_style='carto-positron',
                           zoom=9.5,
                           # 소득 많은 순서대로 빨, 노, 초, 파
                           color_continuous_scale=[(0, 'black'), (0.01, 'blue'), (0.3, '#87CEEB'),(0.5, '#90EE90'),(0.7, 'yellow'), (1, 'red')],
                           opacity=0.5,
                           title='월 평균 소득 금액에 따른 서울시 행정동별 코로플레스 맵'
                          )


fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# HTML 파일로 저장(반드시 경로 변경!)
fig.write_html("/opt/lampp/htdocs/income_choropleth_map.html")
print("/opt/lampp/htdocs/income_choropleth_map.html")
