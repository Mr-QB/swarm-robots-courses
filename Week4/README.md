Dưới đây là một số đoạn về lý thuyết để giải thích phương pháp Trường tiềm năng (Artificial Potential Field - APF) trong mô phỏng di chuyển robot:

---

## Lý thuyết

### 1. Phương pháp Trường tiềm năng (APF)

Phương pháp Trường tiềm năng (APF) là một phương pháp phổ biến trong điều khiển robot tự động, được sử dụng để tạo ra một trường lực ảo trong không gian làm việc của robot. Trong APF, robot cảm nhận và phản ứng với các lực hấp dẫn từ mục tiêu và các lực đẩy từ các chướng ngại vật. Mục tiêu của robot là di chuyển từ vị trí hiện tại đến mục tiêu mà không va chạm với các chướng ngại vật.

### 2. Cơ sở lý thuyết

- **Lực hấp dẫn từ mục tiêu**: Là lực hấp dẫn được tạo ra bởi mục tiêu và đưa robot đến gần mục tiêu. Cường độ của lực này phụ thuộc vào khoảng cách giữa robot và mục tiêu.

- **Lực đẩy từ các chướng ngại vật**: Là lực đẩy được tạo ra bởi các chướng ngại vật và đẩy robot ra xa các chướng ngại vật. Cường độ của lực này phụ thuộc vào khoảng cách giữa robot và chướng ngại vật.

### 3. Công thức tính lực

- **Lực hấp dẫn**: Được tính dựa trên khoảng cách giữa robot và mục tiêu. Càng gần mục tiêu, lực hấp dẫn càng mạnh.

- **Lực đẩy**: Được tính dựa trên khoảng cách giữa robot và các chướng ngại vật. Càng gần chướng ngại vật, lực đẩy càng mạnh.

### 4. Điều khiển robot

- Trong quá trình di chuyển, robot sẽ cảm nhận và tính toán lực hấp dẫn từ mục tiêu và các lực đẩy từ các chướng ngại vật.
- Dựa trên tổng hợp các lực này, robot sẽ di chuyển đến vị trí mới một cách an toàn và hiệu quả.

---

Những đoạn này cung cấp một cái nhìn tổng quan về lý thuyết và cơ sở của phương pháp APF trong điều khiển robot tự động.

## Demo

Chương trình cung cấp khả năng mô phỏng di chuyển của robot dựa trên phương pháp Trường tiềm năng (APF). Dưới đây là một số gif minh họa cho mô phỏng này:

1. **Mô phỏng di chuyển của 2 robot:**
   ![2_agent_demo](demo\2_agent.gif)

2. **Mô phỏng di chuyển của 4 robot:**
   ![2_agent_demo](demo\4_agent.gif)

3. **Mô phỏng di chuyển của 6 robot:**
   ![2_agent_demo](demo\6_agent.gif)

4. **Mô phỏng di chuyển của 8 robot:**
   ![2_agent_demo](demo\8_agent.gif)

5. **Mô phỏng di chuyển của 10 robot:**
   ![2_agent_demo](demo\10_agent.gif)

6. **Mô phỏng di chuyển của 20 robot:**
   ![2_agent_demo](demo\20_agent.gif)