import streamlit as st
import pandas as pd

st.title("데이터프레임 화면")

arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
df = pd.DataFrame(arr)

st.dataframe(df, use_container_width=True)

######

st.title("테이블 화면")

st.table(df)

######

st.metric(label="온도", value="8°C", delta="1.2°C")
st.metric(label="SKT", value="4,500 원", delta="200 원")

col1, col2, col3 = st.columns(3)
col1.metric(label="온도", value="8°C", delta="1.2°C")
col2.metric(label="SKT", value="4,500 원", delta="200 원")
col3.metric(label="서울", value="60,000 인구", delta="-200 인구")
