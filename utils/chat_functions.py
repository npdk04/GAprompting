import streamlit as st
import time
def prompt_user(prompt):
    """
    Xử lý tin nhắn của người dùng và thêm vào lịch sử chat.
    """
    # Thêm tin nhắn của người dùng vào lịch sử
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Hiển thị tin nhắn ngay lập tức trong giao diện
    with st.chat_message("user"):
        st.markdown(prompt)


def handle_first_prompt(prompt):
   st.info("Đây là prompt đầu tiên của bạn! Chức năng đặc biệt đã được kích hoạt.")

def generate_response(prompt):
    with st.chat_message("assistant"):
            # Tạo một placeholder để hiển thị nội dung đang được gõ
            message_placeholder = st.empty()
            full_response = ""
            # Tạo phản hồi dựa trên prompt
            response_text = f"Đây là phản hồi cho câu hỏi của bạn: {prompt}"

            # Mô phỏng hiệu ứng trả lời theo luồng (streaming)
            for chunk in response_text.split():
                full_response += chunk + " "
                time.sleep(0.05)  # Điều chỉnh thời gian delay để thay đổi tốc độ
                message_placeholder.markdown(full_response + "▌") # Hiển thị hiệu ứng con trỏ nhấp nháy

            # Xóa con trỏ nhấp nháy khi kết thúc
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})