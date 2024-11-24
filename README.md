# 🧬 Mendel's Law of Inheritance Simulator
โปรแกรมนี้ช่วยให้ผู้ใช้สามารถเข้าใจและจำลองการถ่ายทอดลักษณะทางพันธุกรรมได้อย่างง่ายดาย โดยใช้กฎของเมนเดลเป็นพื้นฐาน

## 🚀 ฟีเจอร์หลัก
- การเลือก genotype ของพ่อแม่ (AA, Aa, aa)
- แสดงผลด้วย Punnett Square แบบ interactive
- คำอธิบายแบบ animated text พร้อม hover effect
- กราฟ donut chart แสดงสัดส่วน dominant/recessive
- Dark mode UI ที่ทันสมัย
- Fullscreen mode พร้อมปุ่ม Escape เพื่อออก

## 💻 การติดตั้ง
1. ติดตั้ง Python 3.x
2. ติดตั้ง dependencies:
```bash
pip install tkinter
pip install matplotlib
pip install numpy
```

## 🎯 วิธีใช้งาน
1. รันโปรแกรม:
```bash
python inheritance_calculator.py
```
2. เลือก genotype ของ Parent 1 และ Parent 2
3. กดปุ่ม "Calculate Inheritance"
4. ดูผลลัพธ์จาก:
   - Punnett Square
   - คำอธิบายการถ่ายทอด
   - กราฟแสดงสัดส่วน

## 📋 Requirements
- Python 3.x
- tkinter
- matplotlib
- numpy

## 📦 โครงสร้างโปรเจค
```
Law_of_Inheri/
├── inheritance_calculator.py     # โค้ดหลัก
└── README.md                    # เอกสารอธิบาย
```

## 🔧 คลาสและเมธอดหลัก
- `ModernMendelGUI`: คลาสหลักของแอพพลิเคชัน
  - `create_layout()`: สร้าง UI หลัก
  - `create_input_section()`: สร้างส่วนเลือก genotype
  - `create_punnett_square()`: สร้างตาราง Punnett
  - `create_explanation_section()`: สร้างส่วนคำอธิบาย
  - `create_visualization_section()`: สร้างส่วนแสดงกราฟ
  - `calculate_inheritance()`: คำนวณผลการถ่ายทอด
  - `animate_explanation()`: สร้าง animation สำหรับคำอธิบาย

## 🎨 Color Scheme
```python
colors = {
    'bg_dark': '#1a1a1a',        # พื้นหลังหลัก
    'bg_darker': '#0d0d0d',      # พื้นหลังเข้ม
    'text': '#ffffff',           # ข้อความหลัก
    'text_secondary': '#b3b3b3', # ข้อความรอง
    'accent': '#00ffff',         # สีเน้น
    'border': '#333333',         # เส้นขอบ
    'dominant': '#4dff88',       # สีแสดง dominant
    'recessive': '#ff6b6b',      # สีแสดง recessive
}
```

## 🔄 การอัพเดทในอนาคต
- [ ] เพิ่มการจำลองกฎข้อที่ 2 ของเมนเดล
- [ ] เพิ่มการบันทึกและโหลดผลการคำนวณ
- [ ] เพิ่มภาษาไทย
- [ ] เพิ่มการ export ผลลัพธ์เป็น PDF
- [ ] เพิ่มแอนิเมชันการถ่ายทอด

## 👥 ผู้พัฒนา
- Thiraphat Chorakhe

## 📄 ลิขสิทธิ์
This project is licensed under the MIT License - see the LICENSE file for details

## 🙏 ขอบคุณ
- Tkinter สำหรับ GUI
- Matplotlib สำหรับการสร้างกราฟ
- NumPy สำหรับการคำนวณ

## 📞 การติดต่อ
หากมีคำถามหรือข้อเสนอแนะ สามารถติดต่อได้ที่:
- Email: teerayut.so@kkumail.com
- GitHub: https://github.com/OTRONTO-F
