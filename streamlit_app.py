import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import pandas as pd
import numpy as np
import time  # 지연을 주기 위해 필요

# 제목과 설명
st.title("🌟 Streamlit 요소 총집합 데모")
st.header("👨‍🏫 잘생긴 선생님의 멋진 앱")
st.subheader("🧪 이 페이지는 Streamlit의 거의 모든 주요 구성요소를 보여줍니다.")
st.caption("버전 1.0 | Made with ❤️ by 잘생긴 선생님")

# 텍스트 관련 요소
st.text("📌 간단한 텍스트입니다.")
st.markdown("**✅ 굵은 글자**, _기울임_, `코드`, [링크](https://streamlit.io)")

# 코드 블록
code = '''def say_hello():
    print("Hello, 잘생긴 선생님!")'''
st.code(code, language='python')

# 라디오 버튼
option = st.radio("1️⃣ 당신의 역할은?", ["학생", "교사", "학부모"])
st.write("선택한 역할:", option)

# 체크박스
agree = st.checkbox("2️⃣ 동의합니다")
if agree:
    st.success("✅ 동의해 주셔서 감사합니다.")

# 슬라이더
level = st.slider("3️⃣ 난이도를 선택하세요", 1, 10, 5)
st.write("선택한 난이도:", level)

# 셀렉트 박스
subject = st.selectbox("4️⃣ 과목을 선택하세요", ["수학", "과학", "영어"])
st.write("선택한 과목:", subject)