import pandas as pd

# hospital
# xlsx 파일읽기
file_path = 'C:/Users/USER-PC/Downloads/전국 병의원 및 약국 현황 2024.6/1.병원정보서비스 2024.6.xlsx'
df = pd.read_excel(file_path)

# 필요한 컬럼 추출
selected_columns = ['암호화요양기호', '요양기관명', '종별코드', '종별코드명', '우편번호', '주소', '전화번호', '병원홈페이지', '좌표(X)', '좌표(Y)']
df_selected = df[selected_columns]

# 컬럼명 변경
df_selected.columns = ['hospital_id', 'hospital_name', 'typecode', 'typecode_name', 'postalcode', 'address', 'call_number', 'site_url', 'longitude', 'latitude']

# CSV 파일로 저장
output_file_path = 'C:/Users/USER-PC/Downloads/hospital_selected.csv'
df_selected.to_csv(output_file_path, index=False)