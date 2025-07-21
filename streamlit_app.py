import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import streamlit as st
import pandas as pd
import numpy as np


# 제목과 설명
st.title("🌟 Streamlit 요소 총집합 데모")
st.header("👨‍🏫 잘생긴 선생님의 멋진 앱")
st.subheader("🧪 이 페이지는 Streamlit의 거의 모든 주요 구성요소를 보여줍니다.")
st.caption("버전 1.0 | Made with ❤️ by 잘생긴 선생님")

# 텍스트
st.text("📌 간단한 텍스트")
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
subject = st.selectbox("4️⃣ 과목 선택", ["수학", "과학", "영어", "역사"])
st.write("선택된 과목:", subject)

# 멀티 셀렉트
hobbies = st.multiselect("5️⃣ 취미 선택", ["독서", "운동", "음악감상", "게임"])
st.write("선택된 취미:", hobbies)

# 텍스트 입력
name = st.text_input("6️⃣ 이름을 입력하세요")
st.write("입력한 이름:", name)

# 숫자 입력
age = st.number_input("7️⃣ 나이를 입력하세요", min_value=0, max_value=120)
st.write("입력한 나이:", age)

# 날짜 입력
date = st.date_input("8️⃣ 날짜 선택")
st.write("선택한 날짜:", date)

# 시간 입력
time = st.time_input("9️⃣ 시간 선택")
st.write("선택한 시간:", time)

# 파일 업로드
uploaded_file = st.file_uploader("🔟 파일 업로드 (예: CSV, 이미지 등)")
if uploaded_file is not None:
    st.write("업로드된 파일 이름:", uploaded_file.name)

# 데이터프레임 표시
st.write("📊 예시 데이터프레임:")
df = pd.DataFrame({
    '이름': ['민수', '지훈', '수연'],
    '점수': [85, 90, 95]
})
st.dataframe(df)



# 이미지 표시
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Giraffe_standing.jpg/320px-Giraffe_standing.jpg",
         caption="🦒 귀여운 기린", use_column_width=True)

# 버튼
if st.button("🎯 클릭하세요"):
    st.balloons()  # 풍선 애니메이션

# 컬럼 나누기
col1, col2 = st.columns(2)
with col1:
    st.write("📌 왼쪽 열")
with col2:
    st.write("📌 오른쪽 열")

# 사이드바 요소
st.sidebar.title("📚 사이드바 메뉴")
st.sidebar.radio("사이드바 옵션", ["옵션 1", "옵션 2"])

# 상태 메시지
st.success("✅ 작업이 성공적으로 완료되었습니다!")
st.warning("⚠️ 주의가 필요합니다.")
st.error("❌ 오류가 발생했습니다.")
st.info("ℹ️ 참고 정보입니다.")
# 프로그레스 바
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)
    st.sleep(0.05)  # 프로그레스 바 업데이트를 위한 지연    