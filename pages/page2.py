import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
import os

st.title("📑 학생 성적 분석 앱")

# matplotlib 한글 폰트 설정
font_path = "/workspaces/blankapp20250721/fonts/나눔 글꼴/나눔고딕/NanumFontSetup_TTF_GOTHIC/NanumGothic.ttf"
if os.path.exists(font_path):
    fm.fontManager.addfont(font_path)
    plt.rcParams['font.family'] = fm.FontProperties(fname=font_path).get_name()
else:
    st.warning("⚠️ 지정한 경로에 NanumGothic.ttf 파일이 없습니다. 한글이 깨질 수 있습니다.")
plt.rcParams['axes.unicode_minus'] = False  # 마이너스(-) 깨짐 방지

# openpyxl 설치 안내
try:
    import openpyxl
except ImportError:
    st.error("❗ 'openpyxl' 라이브러리가 설치되어 있지 않습니다. 터미널에서 'pip install openpyxl' 명령어로 설치해 주세요.")

# 파일 업로드
uploaded_file = st.file_uploader("엑셀 파일을 업로드하세요.", type=["xlsx"])

if uploaded_file is not None:
    try:
        # 데이터 읽기
        df = pd.read_excel(uploaded_file, engine="openpyxl")
        st.subheader("원본 데이터")
        st.dataframe(df)

        # 과목 컬럼만 추출 (이름 제외)
        subjects = [col for col in df.columns if col != "이름"]

        # 과목별 평균, 표준편차 계산
        mean_scores = df[subjects].mean()
        std_scores = df[subjects].std()

        # 결과 표시
        st.subheader("과목별 평균")
        st.write(mean_scores)

        st.subheader("과목별 표준편차")
        st.write(std_scores)

        # 차트 그리기
        st.subheader("과목별 성적 차트")
        fig, ax = plt.subplots()
        df.set_index("이름")[subjects].plot(kind="bar", ax=ax)
        ax.set_ylabel("점수")
        ax.set_title("학생별 과목 성적")
        st.pyplot(fig)

        # 평균/표준편차 차트
        st.subheader("과목별 평균 및 표준편차 차트")
        fig2, ax2 = plt.subplots()
        x = np.arange(len(subjects))
        ax2.bar(x - 0.2, mean_scores, width=0.4, label="평균")
        ax2.bar(x + 0.2, std_scores, width=0.4, label="표준편차")
        ax2.set_xticks(x)
        ax2.set_xticklabels(subjects)
        ax2.set_ylabel("점수")
        ax2.set_title("과목별 평균 및 표준편차")
        ax2.legend()
        st.pyplot(fig2)
    except Exception as e:
        st.error(f"엑셀 파일을 읽는 중 오류가 발생했습니다: {e}")
else:
    st.info("엑셀 파일(.xlsx)을 업로드하면 분석 결과가 표시됩니다.")