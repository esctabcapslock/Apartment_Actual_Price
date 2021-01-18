# Apartment_Actual_Price
아파트 매매가격 시각화

- <a href="https://rt.molit.go.kr/">국토부 실거래가 공개시스템</a>을 바탕으로 함
- 한 읍면동 안에서 1달동안 거래된 데이터를 바탕으로 면적당 매매가격의 중위값을 시각화
- 실제 체감과는 다를 수 있음.


## 보러가기
- <a href="https://esctabcapslock.github.io/Apartment_Actual_Price/1(%EC%8B%9C%EA%B5%B0%EA%B5%AC).html">시군구(클릭)</a>
- <a href="https://esctabcapslock.github.io/Apartment_Actual_Price/2(%EC%9D%8D%EB%A9%B4%EB%8F%99).html"> 읍면동(클릭) </a>

## 만든 법
### 시군구
- <a href="http://buking.kr/">부킹닷컴</a>에서 2020.07의 월 별 데이터를 자바스크립트로 크롤링한 뒤, 엑셀로 처리했음.
- 지도 데이터는 <a href="http://www.gisdeveloper.co.kr/?p=2332">여기</a>의 자료를 바탕으로 QGIS를 활용해 단순화시켜 geojson으로 변경함. 자바스크립트로 svg로 변경함.

### 읍면동
- 국토부 실거래가 시스템의 자료를 직접 처리함
- 아파트 데이터는 파이썬을 이용해 처리한 후(openpyxl 이용), 자바스크립트 함수 형태의 문자열로 저장.
- 지도 데이터는 같은 방식으로 처리함.
- 간단한 자바스크립트 이벤트를 활용해 지도를 움직일 수 있게 설정
- 행정구역을 클릭할 경우 Chart.js가 line 종류의 차트를 그려냄
- 재생 버튼을 클릭하면 알아서 변화함
- 파이어폭스 최적화 / 모바일 미지원
