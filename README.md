# ADDD Map Visualization

서울 공공데이터를 기반으로 행정동 단위 인구, 소득, 지하철 승하차 데이터를 시각화하는 프로젝트입니다.

본 프로젝트는 데이터 기반 도시 분석 및 시각화 예시를 제공하기 위한 목적으로 제작되었습니다.

---

## 📊 Features

- 서울 생활인구 Heatmap 시각화
- 행정동별 소득 수준 지도
- 지하철 승하차 인구 Heatmap
- 웹 기반 지도 시각화 (PHP + Python 연동)

---

## 📁 Repository Structure


ADDD_map_visualization/
├── notebooks/ # 데이터 전처리 및 시각화 Jupyter Notebook
├── web/ # 웹 페이지 (PHP 기반 지도 시각화)
├── data/ # 데이터 관련 설명 (데이터는 포함되지 않음)
├── output/
│ ├── population_heatmap/ # 생활인구 시각화 결과
│ ├── subway_heatmap/ # 지하철 Heatmap 결과
├── scripts/ # 데이터 가공 및 처리 코드
└── README.md


---

## ⚙️ Requirements

- Python 3.x
- Jupyter Notebook
- PHP (Apache 환경)
- 주요 라이브러리:
  - pandas
  - folium
  - numpy

---

## 🚀 How to Run

### 1. 데이터 준비
본 프로젝트는 공공데이터를 사용하며, 저장소에는 포함되어 있지 않습니다.  
아래 출처에서 데이터를 다운로드 후 `data/` 경로에 저장해야 합니다.

---

### 2. Jupyter Notebook 실행

notebooks/*.ipynb 실행


---

### 3. 웹 시각화 실행
- Apache 환경에서 `web/` 디렉토리 배포
- PHP에서 Python 스크립트를 호출하여 지도 생성

---

## 📦 Data Sources

본 프로젝트는 아래 공공데이터를 활용합니다.

- 서울 생활인구 데이터  
  https://data.seoul.go.kr/dataList/OA-14991/A/1/datasetView.do  

- 서울 지하철 승하차 데이터  
  https://data.seoul.go.kr/dataList/OA-12914/S/1/datasetView.do  

- 행정동 경계 및 좌표 데이터  
  (서울 열린데이터광장 및 공공데이터포털 기반)

- 서울 소득 데이터  
  (공공 통계자료 기반)

---

## ⚠️ Data License Notice

본 프로젝트에 사용된 데이터는 서울 열린데이터광장에서 제공하는 공공데이터를 기반으로 하며,  
각 데이터의 저작권 및 이용 조건은 원 제공기관의 정책을 따릅니다.

본 저장소는 데이터 자체를 포함하지 않으며,  
사용자는 반드시 공식 출처를 통해 데이터를 다운로드해야 합니다.

---

## 📄 License

This project is licensed under the Apache License 2.0.

---

## 💡 Notes

- 데이터는 주기적으로 업데이트되므로 최신 데이터를 사용해야 합니다.
- 행정동 경계 및 통계 시점이 다를 수 있어 일부 오차가 발생할 수 있습니다.
- 본 프로젝트는 연구 및 시각화 목적의 예제입니다.
