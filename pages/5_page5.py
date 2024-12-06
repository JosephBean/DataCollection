import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mat
import seaborn as sb
import folium
from folium import plugins

st.set_page_config(layout="wide")

# 한글 깨짐 처리 설정
mat.rcParams['font.family'] = 'Malgun Gothic'

# 데이터프레임 생성
df = pd.DataFrame({
    '이름': ['홍길동','류관순','이황'],
    '나이': [19, 16, 100],
    '키': [145, 178, 165]
})

# 데이터프레임 데이터 출력
# st.dataframe(df, use_container_width=True)

# 바 차트 설정
# fig, ax = plt.subplots()
# ax.bar(df['이름'], df['나이'])
# st.pyplot(fig)

# seaborn
# bar2 = sb.barplot(x="이름", y="나이", data=df, ax=ax)
# fig = bar2.get_figure()
# st.pyplot(fig)

#######

df1 = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)
# st.map(df1)

df2 = pd.read_csv("data/data1.csv")
df2.columns = ["lat", "lon"]

# st.dataframe(df1, use_container_width=True)
# st.dataframe(df2.iloc[ : 10, : ], use_container_width=True)

# st.map(df2)

map_center = [37.5640076, 126.9586116]
m = folium.Map(location=map_center, zoom_start=16)

folium.Marker(map_center, popup='서대문구').add_to(m)

st.components.v1.html(m._repr_html_(), height=500)
