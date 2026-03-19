# ADDD_map_visualization
(PO님 과제)
(수정완료!)

ADDD 인턴 유성민


(파일 실행 전 라이브러리 import할 것들 여러 개 쌓아놓고 했는데, 필요한 것만 남기고 지우는 작업 진행 중)


ADDD_map_visualization: ipynb 코드, csv파일, 히트맵 html이 있는 리포짓


각 파일 및 폴더 설명


코드 짜면서 시각화를 확인하기 주피터 노트북(ipynb파일)을 이용해서 진행.


지도_시각화_웹페이지 : 서울 생활인구, 서울소득 지도, 지하철 승하차 인구를 구하는 웹페이지. 말씀하신 오류 전부 수정 및 서울 소득 지도, 지하철 승하차 인구 완성!

(리눅스 권한문제로 인해 실행 불가일 때 해결 법!

1. readme를 읽고 sudo가 붙은 부분을 터미널에 전부 붙여넣는다.

2. 리눅스 명령어 which python3 를 이용해가지고 
/home/addd/miniconda3/bin/python3  이런 형식의 파이썬 경로를 구하고, php파일에서 실행하는 경로를 변경해야 한다. 또한 xampp에서 웹페이지 쓸 때 임시로 사용되는 www-data계정이 내 리눅스 계정 폴더를 웹페이지로 가져오지 못할 수 있다. 이때  
sudo chown -R www-data:www-data /var/www/html/
sudo chmod -R 775 /var/www/html/
sudo usermod -a -G www-data addd
이 과정을 다른 py파일과 php파일에도 반복하면 웹페이지에 권한이 설정되어서 실행이 가능하다.
(여기서 /var/www/html/은 일반적인 xampp에서의 apache2 실행 시 php가져오는 디렉토리 폴더이다. apache2가 아닌 그냥 apache에 경우에서는 /opt/lampp/htdocs/에서 할 수도 있으니 apache 실행 할 때 어디서 php가져오는지 권한 확인하시고, 그래도 안 되시면 https://stackoverflow.com/questions/43144325/failed-to-open-stream-permission-denied-in-opt-lampp-htdocs 참조 하시고, 그래도 안 되시면 일단 알려주세요!)



서울생활인구: 서울 인구수를 시각화 하는 코드(문제 수정 완료. 수정 내용: 구리시 더미 데이터 빼기, 0세, 70세 변수 다뤄서 오류 수정.)



df_hangjungdong_code_data_2024.csv: 각 행정동 위경도 데이터가 담긴 csv코드. 꼭 CSV파일의 경로를 본인 컴퓨터에 맞게 바꿔서 입력해야 한다.



LOCAL_PEOPLE_DONG_202311.csv: 각 행정동 당 인구 수 데이터가 담긴 2023년 11월 기준 코드. 꼭 CSV파일의 경로를 본인 컴퓨터에 맞게 바꿔서 입력해야 한다. 특정 날짜(1달 간격)가 지나면 최신 데이터를 통계청(출처: https://data.seoul.go.kr/dataList/OA-14991/A/1/datasetView.do;jsessionid=352B86F9D55D154F919948EE35444433.new_portal-svr-11   )에서 받아야 함.
(2024년 1월 26일 변경사항. 출처경로에서 다운받으시면 됩니다.)

seoul_age_gender_html_folder: 실행 결과로 구해진 html파일이 담긴 폴더



지하철승하차인구 : 서울 지하철 승하차인구가 담겨있는 ipynb코드, 실행하기 위해선 특정한 지하철 승하차 유동인구 정보가 담겨있는 csv파일의 경로가 필요하다. 실행 전, 꼭 CSV파일의 경로를 본인 컴퓨터에 맞게 바꿔서 입력해야 한다



subway_csv: 위의 ipynb를 실행하기 위해 필요한 데이터, 특정 날짜(1달 간격)가 지나면 최신 데이터를 통계청(출처 : https://data.seoul.go.kr/dataList/OA-12914/S/1/datasetView.do ) 에서 다운받아야 한다.


subway_heatmap_html : 실행 결과로 구해진 html파일이 담긴 폴더

unique_df.csv:서울생활인구에 addd_seoul_population_data_visualization.ipynb를 실행해서 매 달 LOCAL_PEOPLE_DONG_202311.csv과 df_hangjungdong_code_data_2024.csv를 합쳐서 df를 새롭게 만들어야 한다.
서울소득지도: 서울 각 동의 소득 수준이 담긴 폴더(찾아보니까 행정동경계가 2021년 자료이고, 월 소득 통계가 2023년 11월 자료. 행정동경계 데이터 추가로 업데이트 필요)

서울상권지도: 서울시 상권지도 시각화 코드가 담긴 폴더, php파일, py파일, 데이터 담긴 csv파일, 데이터 담긴 json파일, 데이터가 담긴 json파일 만드는 ipynb파일로 구성되어있다. (csv파일은 주신 zip파일 푸니까 이름이 깨져있어서 이름을 임의로 재설정했습니다. 실행하실 때 수정해주세요.)(용량이 커서 못 올렸고 제 노션: https://www.notion.so/dalgo/PO-eb44eef1660243eb94cb375a44f20810?pvs=4 에 다운받으실 수 있고, 이미 zip파일 있으신데 이름 안 깨지면 압축 푸셔서 경로 설정 해주시면 됩니다.)
