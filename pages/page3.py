import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from datetime import date, timedelta
import os
import io

# -------------------------------
# 한글 폰트 설정
font_path = "./fonts/NanumGothic.ttf"
if os.path.exists(font_path):
    fm.fontManager.addfont(font_path)
    plt.rcParams['font.family'] = fm.FontProperties(fname=font_path).get_name()
else:
    st.warning("⚠️ NanumGothic.ttf 파일이 없습니다. 한글이 깨질 수 있습니다.")

plt.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지

# -------------------------------
# 초기 설정
st.set_page_config(page_title="음식물 쓰레기 줄이기 실천 앱", layout="centered")
st.title("🍽️ 오늘도 음식 다 먹었나요?")
st.subheader("음식물 쓰레기 줄이기 실천 기록장")

# -------------------------------
# 사용자 입력
st.markdown("**1. 오늘 남긴 음식 종류와 양을 입력해보세요.**")
밥 = st.slider("밥", 0.0, 1.0, 0.0, 0.1)
국 = st.slider("국/찌개", 0.0, 1.0, 0.0, 0.1)
반찬 = st.slider("반찬", 0.0, 1.0, 0.0, 0.1)
과일 = st.slider("과일/디저트", 0.0, 1.0, 0.0, 0.1)

총_남긴_양 = 밥 + 국 + 반찬 + 과일

# -------------------------------
# 결과 출력
st.markdown("---")
st.markdown("**2. 오늘 남긴 음식 총량 요약**")
st.metric(label="🍛 오늘 남긴 총 음식량 (단위: 공기)", value=f"{총_남긴_양:.2f} 공기")

if 총_남긴_양 == 0:
    st.success("👏 훌륭해요! 오늘 음식물 쓰레기를 하나도 남기지 않았어요.")
elif 총_남긴_양 < 1:
    st.info("😊 꽤 잘했어요. 내일은 더 줄여볼까요?")
else:
    st.warning("⚠️ 음식물 쓰레기를 줄이기 위한 노력이 더 필요해요.")

# -------------------------------
# 데이터 저장
st.markdown("---")
st.markdown("**3. 오늘 기록 저장 및 시각화**")

today = pd.Timestamp(date.today())  # ← 오류 수정된 부분
save_path = "./food_waste_log.csv"
new_row = {'날짜': today, '남긴 음식량(공기)': 총_남긴_양}

# 기존 파일 불러와 추가
if os.path.exists(save_path):
    df_csv = pd.read_csv(save_path)
    df_csv['날짜'] = pd.to_datetime(df_csv['날짜'])  # ← 날짜 형식 변환 필수
    df_csv = pd.concat([df_csv, pd.DataFrame([new_row])], ignore_index=True)
else:
    df_csv = pd.DataFrame([new_row])

df_csv.to_csv(save_path, index=False)
st.success("✅ 오늘의 기록이 저장되었습니다.")

# -------------------------------
# 1주일 실천 그래프
last_7 = df_csv[df_csv['날짜'] >= (today - timedelta(days=6))]

fig1, ax1 = plt.subplots()
ax1.plot(last_7['날짜'], last_7['남긴 음식량(공기)'], marker='o')
ax1.set_title("📉 최근 7일간 실천 그래프")
ax1.set_ylabel("공기 수")
plt.xticks(rotation=45)
st.pyplot(fig1)

# -------------------------------
# 30일 실천 그래프
st.markdown("**4. 최근 30일 실천 기록 그래프**")

last_30 = df_csv[df_csv['날짜'] >= (today - timedelta(days=30))]

fig2, ax2 = plt.subplots()
ax2.plot(last_30['날짜'], last_30['남긴 음식량(공기)'], marker='o', color='green')
ax2.set_title("📅 최근 30일간 음식물 쓰레기 실천 그래프")
ax2.set_ylabel("공기 수")
plt.xticks(rotation=45)
st.pyplot(fig2)

# -------------------------------
# 엑셀 다운로드
st.markdown("**5. 기록 다운로드**")

if st.button("📥 엑셀로 다운로드"):
    towrite = io.BytesIO()
    df_csv.to_excel(towrite, index=False, sheet_name='기록')
    towrite.seek(0)
    st.download_button(
        label="엑셀 파일 다운로드",
        data=towrite,
        file_name="food_waste_log.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
