import re
import random
import folium
import os
import pandas as pd
# 다운 받은 경로로 재설정 및 파일 가져오기
file_path = "/opt/lampp/htdocs/df_merged_202312.csv"

df_merged= pd.read_csv(file_path,header=0)
# 유니크한 노선명을 찾습니다.
line_names = df_merged['노선명'].unique()

# 더 진한 색상을 위해 색상 코드 범위를 조정합니다.
available_colors = ['#%06X' % random.randint(0, 0x7FFFFF) for _ in range(len(line_names))]
color_dict = dict(zip(line_names, random.sample(available_colors, len(line_names))))


m = folium.Map(location=[37.5665, 126.9780], zoom_start=10)

# 전체 '총승객수'의 평균을 계산합니다.
avg_total_passenger = df_merged['총승객수'].mean()

# 원의 크기를 정할 상수입니다.
size_factor = 8  # 원의 크기를 조절합니다.(너무 작으면 올립니다.)

for i in range(0, len(df_merged)):
    popup_text = "노선명: {}<br>역명: {}<br>승차총승객수: {}<br>하차총승객수: {}<br>총승객수: {}".format(
        df_merged.iloc[i]['노선명'],
        df_merged.iloc[i]['역명'],
        df_merged.iloc[i]['승차총승객수'],
        df_merged.iloc[i]['하차총승객수'],
        df_merged.iloc[i]['총승객수']
    )
    
    # 원의 크기를 '총승객수'에 따라 상대적으로 조정합니다.
    radius = (float(df_merged.iloc[i]['총승객수']) / avg_total_passenger) * size_factor

    # CircleMarker를 생성하고 맵에 추가합니다.
    folium.CircleMarker(
        location=[df_merged.iloc[i]['lat'], df_merged.iloc[i]['lng']],
        radius=radius,
        color=color_dict[df_merged.iloc[i]['노선명']], 
        fill=True,
        fill_color=color_dict[df_merged.iloc[i]['노선명']],
        fill_opacity=0.3,  # 원의 색상 투명도를 70%로 설정합니다.
        popup=folium.Popup(popup_text, max_width=300)
    ).add_to(m)

# 원하는 경로로 재설정!  지도를 로컬에 HTML 파일로 저장.
m.save('/opt/lampp/htdocs/subway_map.html')

# 원하는 경로로 재설정!
print(os.path.abspath('/opt/lampp/htdocs/subway_map.html'))

