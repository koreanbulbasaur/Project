import openpyxl # openpyxl 라이브러리를 임포트합니다
wb = openpyxl.Workbook() # 새로운 워크북(엑셀 파일)을 생성합니다
ws = wb.active # 현재 활성화된 워크시트를 선택합니다
data = [('01:24.3', '음 넌')] # 추가하고 싶은 데이터를 정의합니다
ws.append(data[0]) # 워크시트에 데이터를 추가합니다
wb.save('test.csv') # 워크북을 저장합니다