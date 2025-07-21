import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
import os

# 정확한 나눔고딕 폰트 파일 경로 지정
font_path = os.path.join(
    '/workspaces/blankapp20250721',
    'fonts', '나눔 글꼴', '나눔고딕', 'NanumFontSetup_TTF_GOTHIC', 'NanumGothic.ttf'
)

# 폰트가 존재하면 matplotlib에 등록 및 설정
if os.path.exists(font_path):
    fm.fontManager.addfont(font_path)
    fontprop = fm.FontProperties(fname=font_path)
    plt.rcParams['font.family'] = fontprop.get_name()
else:
    st.warning("⚠️ 지정한 경로에 NanumGothic.ttf 파일이 없습니다. 한글이 깨질 수 있습니다.")

plt.rcParams['axes.unicode_minus'] = False  # 마이너스(-) 깨짐 방지

st.title("📊 Matplotlib 데이터 시각화 예시")

# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y, label='사인 곡선')  # 한글 라벨
ax.set_title('한글이 포함된 사인 그래프')  # 한글 제목
ax.set_xlabel('X축 (시간)')  # 한글 X축
ax.set_ylabel('Y축 (진폭)')  # 한글 Y축
ax.legend()

st.pyplot(fig)
st.caption("matplotlib을 활용한 한글 그래프")