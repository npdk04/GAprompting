def lv1_instrucstion_prompting():
    return """Bạn hãy thử như sau:

Tôi có một vấn đề sau: [Vấn đề của bạn]. Hãy giải quyết nó bằng cách:
- Thứ nhất, tôi là [Thông tin về người dùng, ví dụ: học sinh lớp 7].
- Thứ hai, câu trả lời của bạn phải có 3 phần: [Liệt kê các phần, ví dụ: phân tích vấn đề, giải pháp, kiến thức nền tảng].
    """

def lv1_zeroshot_cot():
    return """Bạn hãy thử như sau: 
    
Hãy suy nghĩ từng bước để giải quyết vấn đề sau: [Vấn đề của bạn]. """

def lv2_tot():
    return """Vấn đề: [Vấn đề của bạn].
Sau khi giải quyết xong, hãy tổng hợp tất cả kiến thức liên quan đến [Lĩnh vực, ví dụ: hình học]. Dưới đây là quy trình tư duy:
- [Bước 1: Phân tích vấn đề].
- [Bước 2: Đánh giá bằng kiến thức].
- [Bước 3: Đưa ra giải pháp].
"""

def lv2_cov():
    return """Hãy giải quyết vấn đề sau theo các bước:
1. Giải quyết vấn đề chi tiết: [Vấn đề của bạn].
2. Sau khi có đáp án, hãy tự đặt 3 câu hỏi để xác minh câu trả lời. Ví dụ: "[Câu hỏi ví dụ]".
3. Trả lời các câu hỏi xác minh đó.
4. Đưa ra một kết luận cuối cùng về câu trả lời."""

def lv2_got():
    return """Hãy phân tích và suy nghĩ nhiều cách giải quyết cho vấn đề: [Vấn đề của bạn].
Sau đó, đánh giá các cách giải đó và chọn ra một cách tốt nhất để thực hiện."""

def lv3_multiple_cots():
    return """Prompt 1: Hãy liệt kê tất cả các hướng giải quyết cho [Vấn đề của bạn] và các kiến thức liên quan.
Prompt 2: Dựa trên các hướng giải quyết trên, hãy chọn hướng tốt nhất cho [Đối tượng, ví dụ: học sinh lớp 7] và giải quyết nó."""

def lv3_structured_prompting():
    return """### Task instruction
[Mô tả yêu cầu của bạn]
### Task detail
[Chi tiết về nhiệm vụ]
### Output Format
[Định dạng đầu ra mong muốn]
### Examples
[Ví dụ minh họa]"""

PROMPTS = {
    "Instructional Prompting": lv1_instrucstion_prompting,
    "Zero-Shot CoT": lv1_zeroshot_cot,
    "Tree-of-Thought (ToT)": lv2_tot,
    "Chain-of-Verification (CoV)": lv2_cov,
    "Graph-of-Thought (GoT)": lv2_got,
    "Multiple CoTs": lv3_multiple_cots,
    "Structured Prompting": lv3_structured_prompting,
}