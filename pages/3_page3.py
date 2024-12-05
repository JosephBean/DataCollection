import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

btn = st.button("누르면 아파요")

if btn:
    st.write(":blue[버튼] 아야!!")

#####

df = pd.DataFrame({
    "첫번째": [1,2,3,4],
    "두번째": [10,20,30,40]
})

st.download_button(
    label="CSV 다운로드",
    data=df.to_csv(),
    file_name="샘플.csv",
    mime="text/csv"
)

#####

box = st.checkbox("확인해주세요.")

if box:
    st.write("뒤로 돌아가세요.")

#####

radio = st.radio(
    label="식사는 하셨나요?",
    options=('먹었다', '안먹었다', '생각 중'),
    index=1
)

if radio == "먹었다":
    st.write("배부르다")
elif radio == "안먹었다":
    st.write("속이 더부르륵")
else :
    st.write("중식 한식 일식 ...")

#####

select = st.selectbox(
    label="중식 메뉴",
    options=("자장면", "짱뽕", "탕수육"),
    index=2
)

if select == "자장면":
    st.write("무조건 곱빼기")
elif select == "짱뽕":
    st.write("국물이 시원해요!!")
else :
    st.write("찍먹? 부먹?")

#####

multi = st.multiselect(
    "좋아하는 것은 무엇인가요?",
    ["#사과", "#배", "#망고"],
    ["#사과"]
)

st.write(f"당신의 선택은: :green[{multi}] 입니다.")

#####

sl = st.slider(
    "범위의 값을 지정하세요.",
    0.0, 100.0, (30.0, 65.0)
)

st.write("선택 범위:", sl)

#####

점심 = st.slider(
    "점심 시간은 언제 좋을까요?",
    min_value=dt(2024, 12, 5, 13, 20),
    max_value=dt(2024, 12, 5, 14, 30),
    value=dt(2024, 12, 5, 13, 30),
    step=datetime.timedelta(minutes=10),
    format="MM/DD/YY HH:mm"
)
st.write("선택한 시간:", 점심)

# 텍스트 입력
title = st.text_input(
    label='가고 싶은 여행지가 있나요?', 
    placeholder='여행지를 입력해 주세요'
)
st.write(f'당신이 선택한 여행지: :violet[{title}]')

# 숫자 입력
number = st.number_input(
    label='나이를 입력해 주세요.', 
    min_value=10, 
    max_value=100, 
    value=30,
    step=5
)
st.write('당신이 입력하신 나이는:  ', number)
