import streamlit as st
from utils.chat_functions import prompt_user, generate_response, reset_chat, prompt_checking

# Khởi tạo tiêu đề
st.markdown("<h1 style='text-align: center;'>GA Prompting Project</h1>", unsafe_allow_html=True)

# Khởi tạo trạng thái session
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "assistant", "content": "Hi! How can I help you?"})
if "prompt_checker" not in st.session_state:
    st.session_state.prompt_checker = prompt_checking()  # Khởi tạo instance của prompt_checking
if "show_level_up" not in st.session_state:
    st.session_state.show_level_up = False  # Kiểm soát hiển thị nút Yes/No
if "status_message" not in st.session_state:
    st.session_state.status_message = ""  # Lưu trữ thông điệp trạng thái

# Hiển thị lịch sử tin nhắn
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Sidebar
with st.sidebar:
    st.markdown("<h3 style='text-align: center;'>I'm here to help you</h3>", unsafe_allow_html=True)
    # Hiển thị nút Reset Chat
    # if st.button("Reset Chat"):
    #     reset_chat()  # Hàm reset_chat trong chat_functions.py sẽ xử lý
    #     st.session_state.show_level_up = False
    #     st.session_state.status_message = ""
    #     st.session_state.prompt_checker = prompt_checking()  # Reset prompt_checker
    #     st.rerun()
    
    # Hiển thị thông điệp trạng thái nếu có
    if st.session_state.status_message:
        st.write(st.session_state.status_message)
    
    # Hiển thị nút Yes/No nếu show_level_up là True
    if st.session_state.show_level_up:
        st.session_state.prompt_checker.show_level_up_options()

# Xử lý input từ người dùng
if prompt := st.chat_input("Say something..."):
    # Thêm tin nhắn người dùng vào lịch sử
    prompt_user(prompt)
    
    # Tạo phản hồi từ assistant
    try:
        # Gọi generate_response để hiển thị phản hồi chính
        generate_response(prompt)
        # Kiểm tra và lấy phản hồi từ prompt_checking
        checker_response = st.session_state.prompt_checker.check_and_get_response(prompt)
        # Thêm phản hồi của prompt_checking vào lịch sử
        # Kích hoạt hiển thị nút Yes/No
        st.session_state.show_level_up = True
        st.rerun()
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Hiển thị hướng dẫn nâng cấp nếu người dùng đã chọn Yes
st.session_state.prompt_checker.display_upgrade_guide(prompt if 'prompt' in locals() else "")