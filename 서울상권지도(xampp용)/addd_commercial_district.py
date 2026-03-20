import traceback
import os
import pwd
import grp
import folium
import pandas as pd
from geopy.distance import geodesic
import sys
import os
import stat
import shutil
import getpass
pd.options.mode.chained_assignment = None  # 경고 메시지 무시

# (TODO! 이름이 깨져서 임의로 바꾼 이름입니다! 다운 받은 경로로 변경하시고 이름도 바꿔주세요!) CSV 파일 경로와 이름(경도와 위도에 대한 정보가 들어 있는 csv)
file_path = "/home/addd/Downloads/seoul_2023_09.csv"

df= pd.read_csv(file_path, low_memory=False)

def selected_middle_classification(low_classification, korea_area,radius):
    try:
        # '상권업종중분류명'이 입력값과 일치하고 '법정동명'이 입력한 지역구와 일치하는 행만 선택합니다
        df_selected = df[(df['상권업종소분류명'] == low_classification) & (df['법정동명'] == korea_area)]

        # '위도'와 '경도' 열에서 결측치가 있는 행을 제거합니다.
        df_selected = df_selected.dropna(subset=['위도', '경도'])

        # 선택된 데이터가 없는 경우 메시지를 출력하고 함수를 종료합니다.
        if df_selected.empty:
            print("선택된 데이터가 없습니다. 입력값을 확인해주세요.")
            return
        # 입력한 지역구의 중심 좌표를 가져옵니다
        center_latitude = df_selected['위도'].mean()
        center_longitude = df_selected['경도'].mean()
        
        # 지도를 생성합니다. 초기 위치는 입력한 지역구의 중심 좌표로 설정합니다
        m = folium.Map(location=[center_latitude, center_longitude], zoom_start=13, width='100%', height='800px')
        # 선택된 행들의 각 위도와 경도에 마커를 추가합니다
        for idx, row in df_selected.iterrows():
            # 입력한 반경 내에 있는 상호만 선택하여 마커를 추가합니다
            distance = geodesic((center_latitude, center_longitude), (row['위도'], row['경도'])).km
            if distance <= radius:
                # 팝업에 표시될 정보를 설정합니다
                popup_info = f"상호명: {row['상호명']}<br>법정동명: {row['법정동명']}<br>도로명주소: {row['도로명주소']}"
                folium.Marker([row['위도'], row['경도']], popup=folium.Popup(popup_info, max_width=750)).add_to(m)
        # (TODO! 반드시 저장할 경로로 경로 변경 해주세요!) HTML 파일을 임시 디렉토리에 저장합니다.
        file_path_2 = os.path.expanduser('/opt/lampp/htdocs/map_class.html')
        m.save(file_path_2)

        # 파일의 권한을 변경합니다. (644로 설정)
        os.chmod(file_path_2, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)

        # 'www-data' 사용자와 그룹의 ID를 알아냅니다.
        uid = pwd.getpwnam('daemon').pw_uid
        gid = grp.getgrnam('daemon').gr_gid

        # 파일의 소유자와 그룹을 변경합니다.
        os.chown(file_path_2, uid, gid)
        file_path_2 = file_path_2.replace('root ', '')  # 'root ' 문자열을 제거합니다.
        # 저장된 HTML 파일의 절대 경로를 출력합니다
        print(file_path_2)

    except Exception as e:
        print(f"오류 발생: {e}")
        print(traceback.format_exc())
# 함수 호출 예시
low_classification = sys.argv[1]
korea_area = sys.argv[2]
radius=int(sys.argv[3])
selected_middle_classification(low_classification, korea_area,radius)

