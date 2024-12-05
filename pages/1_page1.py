import streamlit as st

# 타이틀
st.title("스마일 :sunglasses:")

# 헤더
st.header("헤더 입니다.")

# 서브헤더
st.subheader("작은 헤더")

# 캡션
st.caption("캡션 입니다.")

# 코드
st.code("arr = []", language="python")

sample_code = """
def 함수():
    return 1 + 1
"""
st.code(sample_code, language="python")

# 텍스트
st.text("일반적으로 글 작성")

# 마크다운
st.markdown("웹개발은 **너무 너무** 쉽다")
st.markdown(":green[$\sqrt{x^2+y^2}=1$]")

# 라텍스
st.latex(r"\sqrt{x^2+y^2}=1")