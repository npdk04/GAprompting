import streamlit as st
import time
import random
def prompt_user(prompt):
    """
    Handles user messages and adds them to chat history.
    """
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

def generate_response(prompt):
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        response_text = f"Đây là phản hồi cho câu hỏi của bạn: {prompt}"
        for chunk in response_text.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

def reset_chat():
    """
    Resets chat history and session state.
    """
    st.session_state.messages = []
    st.session_state.messages.append({"role": "assistant", "content": "Hi! How can I help you?"})
    st.session_state.is_first_prompt = False
    st.session_state.show_level_up_prompt = True
    st.session_state.level_1_upgrade_applied = None
    if 'prompt_manager' in st.session_state:
        del st.session_state.prompt_manager # Deleting the class instance to reset it
    st.rerun()

class prompt_checking:
    def __init__(self):
        self.current_level = 0
        self.level_up_requested = False
        self.show_level_up = True
        self.level_guides = {
            1: [
                {
                    "name": "Instruction Prompting",
                    "guide": """Bạn hãy thử như sau:

Tôi có một vấn đề sau: [Vấn đề của bạn]. Hãy giải quyết nó bằng cách:
- Thứ nhất, tôi là [Thông tin về người dùng, ví dụ: học sinh lớp 7].
- Thứ hai, câu trả lời của bạn phải có 3 phần: [Liệt kê các phần, ví dụ: phân tích vấn đề, giải pháp, kiến thức nền tảng].
"""
                },
                {
                    "name": "Zero-shot Chain-of-Thought",
                    "guide": """Bạn hãy thử như sau: 
    
Hãy suy nghĩ từng bước để giải quyết vấn đề sau: [Vấn đề của bạn]."""
                }
            ],
            2: [
                {
                    "name": "Tree of Thoughts",
                    "guide": """Vấn đề: [Vấn đề của bạn].
Sau khi giải quyết xong, hãy tổng hợp tất cả kiến thức liên quan đến [Lĩnh vực, ví dụ: hình học]. Dưới đây là quy trình tư duy:
- [Bước 1: Phân tích vấn đề].
- [Bước 2: Đánh giá bằng kiến thức].
- [Bước 3: Đưa ra giải pháp].
"""
                },
                {
                    "name": "Chain of Verification",
                    "guide": """Hãy giải quyết vấn đề sau theo các bước:
1. Giải quyết vấn đề chi tiết: [Vấn đề của bạn].
2. Sau khi có đáp án, hãy tự đặt 3 câu hỏi để xác minh câu trả lời. Ví dụ: "[Câu hỏi ví dụ]".
3. Trả lời các câu hỏi xác minh đó.
4. Đưa ra một kết luận cuối cùng về câu trả lời."""
                },
                {
                    "name": "Graph of Thoughts",
                    "guide": """Hãy phân tích và suy nghĩ nhiều cách giải quyết cho vấn đề: [Vấn đề của bạn].
Sau đó, đánh giá các cách giải đó và chọn ra một cách tốt nhất để thực hiện."""
                }
            ],
            3: [
                {
                    "name": "Multiple Chain-of-Thoughts",
                    "guide": """Prompt 1: Hãy liệt kê tất cả các hướng giải quyết cho [Vấn đề của bạn] và các kiến thức liên quan.
Prompt 2: Dựa trên các hướng giải quyết trên, hãy chọn hướng tốt nhất cho [Đối tượng, ví dụ: học sinh lớp 7] và giải quyết nó."""
                },
                {
                    "name": "Structured Prompting",
                    "guide": """### Task instruction
[Mô tả yêu cầu của bạn]
### Task detail
[Chi tiết về nhiệm vụ]
### Output Format
[Định dạng đầu ra mong muốn]
### Examples
[Ví dụ minh họa]"""
                }
            ]
        }
    
    def show_level_up_options(self):
        # The logic to display UI elements
        with st.sidebar:
            st.write("Do you want to level up your prompting skill?")
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("Yes", key="yes_button"):
                    self.level_up_requested = True
                    self.current_level += 1
                    st.session_state.show_level_up= False
                    # Store message to be displayed after rerun
                    st.session_state.status_message = "Great! Let's level up your skill! 🚀"
                    st.rerun()

            with col2:
                if st.button("No", key="no_button"):
                    self.level_up_requested = False
                    st.session_state.show_level_up = False
                    # Store message to be displayed after rerun
                    st.session_state.status_message = "No you need to upgrade your skill! 😉"
                    st.rerun()

    def check_and_get_response(self, prompt):
        if self.current_level == 0:
            st.session_state.status_message = "You are at level 0. Please choose to level up."
            return f"Bạn đang ở level {self.current_level}. Vui lòng chọn để nâng cấp."
        elif self.current_level == 1:
            return f"Bạn đang ở level 1. Đây là các hướng dẫn nâng cao prompt cho '{prompt}'."
        elif self.current_level == 2:
            return f"Bạn đang ở level 2. Hãy thử các kỹ thuật nâng cao hơn cho '{prompt}'."
        # Thêm các level khác ở đây
        return f"Bạn đang ở level {self.current_level}. Đang phát triển hướng dẫn cho level này."

    def display_upgrade_guide(self, prompt):
        # Hiển thị hướng dẫn nâng cấp dựa trên level hiện tại
        if self.level_up_requested and self.current_level in self.level_guides:
            with st.expander(f"Hướng dẫn nâng cấp kỹ năng Prompting - Level {self.current_level}"):
                # Chọn ngẫu nhiên một hướng dẫn từ level hiện tại
                guide = random.choice(self.level_guides[self.current_level])
                try:
                    formatted_guide = guide['guide'].replace('[Vấn đề của bạn]', prompt or "vấn đề của bạn")
                    st.markdown(f"""
                    ### Hướng dẫn: {guide['name']}
                    {formatted_guide}
                    """)
                except Exception as e:
                    st.error(f"Lỗi khi hiển thị hướng dẫn: {str(e)}")