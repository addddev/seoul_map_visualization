# 항상 import하는 라이브러리 들
import argparse
import pandas as pd
import numpy as np
import pwd
import grp
import os
import sys
import stat
import folium
from folium.plugins import HeatMap
def create_heatmap_detail(merged, start_age, end_age, hour, gender, exclude_coords=None):
    filtered_df = merged[merged['시간대구분'] == hour]
    # 성별과 나이 범위에 따라 필터링합니다.
    if start_age =='70':
        age_gender_column = f'{gender}{start_age}세이상생활인구수'
    else:
        age_gender_column = f'{gender}{start_age}세부터{end_age}세생활인구수'
    filtered_df = filtered_df[(filtered_df[age_gender_column] > 0)]
    # Remove rows with NaN in 'lat' and 'lng' columns
    filtered_df = filtered_df.dropna(subset=['lat', 'lng'])

    # 구리시 좌표를 제외할 경우 필터링 로직을 적용합니다.
    if exclude_coords:
        tolerance = 1e-3  # 예: 0.001의 허용 오차
        lat, lng = exclude_coords
        filtered_df = filtered_df[
            ~(
                np.isclose(filtered_df['lat'], lat, atol=tolerance) &
                np.isclose(filtered_df['lng'], lng, atol=tolerance)
            )
        ]

    average_lat = filtered_df['lat'].mean()
    average_lng = filtered_df['lng'].mean()

    m = folium.Map(location=[average_lat, average_lng], zoom_start=13)
    heat_data = [
        [row['lat'], row['lng'], row[age_gender_column]]
        for index, row in filtered_df.iterrows()
    ]
    HeatMap(heat_data, radius=30, min_opacity=0.5).add_to(m)
    # file path는 다운 받은 경로로 재설정
    if start_age == '70':
        file_path_2=f'/opt/lampp/htdocs/heatmap_{hour}_{gender}{start_age}세이상.html'
    else:
        file_path_2=f'/opt/lampp/htdocs/heatmap_{hour}_{gender}{start_age}세부터{end_age}세.html'
    m.save(file_path_2)
    # 파일 소유자 변경 코드
    os.chmod(file_path_2, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH)
    uid = pwd.getpwnam('daemon').pw_uid
    gid = grp.getgrnam('daemon').gr_gid
    os.chown(file_path_2, uid, gid)
    print(file_path_2)
                               
if __name__=="__main__":
    # Parse arguments
    hour = int(sys.argv[1])
    start_age =sys.argv[2]
    end_age = sys.argv[3]
    gender = sys.argv[4]
    # TODO 컴퓨터에 다운 받은 경로로 재설정!
    file_path = "/home/addd/Downloads/INTERN_YUSEONGMIN/EDA/unique_df.csv"
    df_unique = pd.read_csv(file_path)
    df_unique = df_unique.dropna(subset=['lat', 'lng'])

    # 구리시 좌표 설정(이전에 비어있던 값들 제거)
    exclude_coords = (37.5962736, 127.1419836)  # 구리시의 대략적인 좌표

    create_heatmap_detail(df_unique, start_age, end_age, hour, gender, exclude_coords=exclude_coords)



