import streamlit as st
import time
from utils.chat_functions import prompt_user, handle_first_prompt, generate_response
from sidebar import draw_sidebar
# Cấu hình trang Streamlit
st.markdown("<h1 style='text-align: center;'>GA Prompting Project</h1>", unsafe_allow_html=True)


sidebar_instance = draw_sidebar()
sidebar_instance.ui_sidebar()



# Khởi tạo lịch sử chat trong session_state nếu chưa có
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Thêm tin nhắn chào mừng chỉ một lần khi ứng dụng khởi động
    st.session_state.messages.append({"role": "assistant", "content": "Hi! How can I help you?"})
    st.session_state.is_first_prompt = False
    st.session_state.show_level_up_prompt = True
# Hiển thị tất cả tin nhắn từ lịch sử chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Xử lý input từ người dùng
if prompt := st.chat_input("Say something..."):
    # Thêm tin nhắn của người dùng vào lịch sử và hiển thị ngay lập tức
    prompt_user(prompt)

    # Tạo phản hồi từ assistant
    generate_response(prompt)
    # Kiểm tra nếu đây là prompt đầu tiên của người dùng
    st.session_state.is_first_prompt = len(st.session_state.messages) == 3

    print(st.session_state.is_first_prompt)
if st.session_state.is_first_prompt and st.session_state.show_level_up_prompt:
    sidebar_instance.logic_sidebar()

# Hiển thị trạng thái "level_checking" độc lập
if st.session_state.is_first_prompt:
    sidebar_instance.level_checking()
    # Thêm phản hồi hoàn chỉnh của assistant vào lịch sử chat
    

