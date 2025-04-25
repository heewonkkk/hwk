import streamlit as st
from datetime import datetime

# 페이지 제목 및 설명
st.title("간단한 챗봇")
st.write("질문을 입력하면 답변을 제공합니다")

# 채팅 응답 함수
def respond(message):
    # 간단한 응답 로직
    if "안녕" in message:
        return "안녕하세요! 무엇을 도와드릴까요?"
    elif "날씨" in message:
        return "오늘은 맑은 날씨입니다."
    elif "시간" in message:
        return "현재 시간은 오후 2시입니다."
    else:
        return "죄송합니다, 이해하지 못했어요. 다른 질문을 해주세요."

# 세션 상태에 대화 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 예시 질문 버튼들
st.write("예시 질문:")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("안녕하세요"):
        st.session_state.messages.append({"role": "user", "content": "안녕하세요"})
        st.session_state.messages.append({"role": "assistant", "content": respond("안녕하세요")})

with col2:
    if st.button("오늘 날씨 어때?"):
        st.session_state.messages.append({"role": "user", "content": "오늘 날씨 어때?"})
        st.session_state.messages.append({"role": "assistant", "content": respond("오늘 날씨 어때?")})

with col3:
    if st.button("지금 몇 시야?"):
        st.session_state.messages.append({"role": "user", "content": "지금 몇 시야?"})
        st.session_state.messages.append({"role": "assistant", "content": respond("지금 몇 시야?")})

# 이전 대화 내용 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 받기
if prompt := st.chat_input("질문을 입력하세요"):
    # 사용자 메시지 표시
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # 사용자 메시지 기록에 추가
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 응답 생성 및 표시
    response = respond(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # 응답 메시지 기록에 추가
    st.session_state.messages.append({"role": "assistant", "content": response})
