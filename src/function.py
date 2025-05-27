def alien_to_int(s: str) -> int:
    # symbol_values: สร้าง dictionary เพื่อเก็บค่าของสัญลักษณ์แต่ละตัวในระบบตัวเลข Alien
    symbol_values = {
        'A': 1,      # สัญลักษณ์ A มีค่าเท่ากับ 1
        'B': 5,      # สัญลักษณ์ B มีค่าเท่ากับ 5
        'Z': 10,     # สัญลักษณ์ Z มีค่าเท่ากับ 10
        'L': 50,     # สัญลักษณ์ L มีค่าเท่ากับ 50
        'C': 100,    # สัญลักษณ์ C มีค่าเท่ากับ 100
        'D': 500,    # สัญลักษณ์ D มีค่าเท่ากับ 500
        'R': 1000    # สัญลักษณ์ R มีค่าเท่ากับ 1000
    }

    total = 0    # total: ตัวแปรสำหรับเก็บผลรวมของค่าตัวเลข
    i = 0        # i: ตัวชี้ (index) สำหรับวนลูปอ่านสัญลักษณ์ในสตริง input
    n = len(s)   # n: ความยาวของสตริง input (จำนวนสัญลักษณ์ทั้งหมด)

    # while i < n: วนลูปตราบใดที่ตัวชี้ i ยังไม่เกินความยาวของสตริง
    while i < n:
        # if i + 1 < n: ตรวจสอบว่ายังมีสัญลักษณ์ถัดไปให้พิจารณาหรือไม่ (เพื่อป้องกัน IndexError)
        if i + 1 < n:
            current_symbol = s[i]     # current_symbol: สัญลักษณ์ปัจจุบันที่กำลังพิจารณา
            next_symbol = s[i+1]      # next_symbol: สัญลักษณ์ถัดไปจากสัญลักษณ์ปัจจุบัน

            # ตรวจสอบกรณีการลบ:
            # - A วางหน้า B (AB = 4) หรือ Z (AZ = 9)
            # - Z วางหน้า L (ZL = 40) หรือ C (ZC = 90)
            # - C วางหน้า D (CD = 400) หรือ R (CR = 900)
            if (current_symbol == 'A' and next_symbol in ('B', 'Z')) or \
               (current_symbol == 'Z' and next_symbol in ('L', 'C')) or \
               (current_symbol == 'C' and next_symbol in ('D', 'R')):
                # หากเข้าเงื่อนไขการลบ: นำค่าของสัญลักษณ์ถัดไปลบด้วยค่าของสัญลักษณ์ปัจจุบัน แล้วบวกเข้า total
                total += symbol_values[next_symbol] - symbol_values[current_symbol]
                i += 2  # เลื่อนตัวชี้ไป 2 ตำแหน่ง เพราะเราได้ประมวลผลไปแล้ว 2 สัญลักษณ์
                continue # continue: ข้ามการทำงานที่เหลือในลูปนี้ แล้วเริ่มรอบใหม่ทันที
        
        # ถ้าไม่เข้าเงื่อนไขการลบ (เป็นกรณีบวกปกติ):
        # total += symbol_values[s[i]]: เพิ่มค่าของสัญลักษณ์ปัจจุบันเข้าไปในผลรวม
        total += symbol_values[s[i]]
        i += 1  # i += 1: เลื่อนตัวชี้ไป 1 ตำแหน่ง เพื่อพิจารณาสัญลักษณ์ถัดไป

    # return total: คืนค่าผลรวมสุดท้ายที่เป็นตัวเลข Integer
    return total

# --- ส่วนสำหรับ Input และ Output ที่จะทำงานเมื่อรันไฟล์นี้โดยตรง ---

# if __name__ == "__main__": บล็อกโค้ดนี้จะทำงานเมื่อไฟล์ Python ถูกรันโดยตรงเท่านั้น
if __name__ == "__main__":
    # print("\n--- Enter Your Alien Numeral ---"): พิมพ์ข้อความแนะนำสำหรับผู้ใช้
    print("\n--- Enter Your Alien Numeral ---")
    # while True: สร้างลูปไม่รู้จบเพื่อให้ผู้ใช้ป้อนข้อมูลได้หลายครั้ง
    while True:
        # input(...): รับสตริงจากผู้ใช้
        # .upper(): แปลงสตริงที่ได้รับให้เป็นตัวพิมพ์ใหญ่ทั้งหมด เพื่อให้ตรงกับ key ใน symbol_values
        user_input = input("Please enter an Alien numeral (or 'exit' to quit): ").upper()

        # if user_input == 'EXIT': ตรวจสอบว่าผู้ใช้ต้องการออกจากโปรแกรมหรือไม่
        if user_input == 'EXIT':
            break # break: ออกจากลูป while

        # is_valid_input = True: ตั้งค่าสถานะเริ่มต้นเป็น True เพื่อตรวจสอบความถูกต้องของ input
        is_valid_input = True
        # for char in user_input: วนลูปตรวจสอบแต่ละตัวอักษรใน input ของผู้ใช้
        for char in user_input:
            # if char not in [...]: ตรวจสอบว่าตัวอักษรปัจจุบันไม่อยู่ในชุดสัญลักษณ์ที่ถูกต้องหรือไม่
            if char not in ['A', 'B', 'Z', 'L', 'C', 'D', 'R']:
                is_valid_input = False # is_valid_input = False: ถ้าเจอตัวอักษรที่ไม่ถูกต้อง ให้ตั้งค่าสถานะเป็น False
                break                  # break: ออกจากลูป for (ไม่ต้องตรวจสอบตัวอักษรที่เหลือ)
        
        # if not is_valid_input: ถ้า input ไม่ถูกต้อง
        if not is_valid_input:
            # print(...): แจ้งเตือนผู้ใช้ถึงข้อผิดพลาดของ input
            print("Invalid character(s) in input. Please use only A, B, Z, L, C, D, R.")
            continue # continue: กลับไปเริ่มลูป while ใหม่ (ให้ผู้ใช้ป้อน input อีกครั้ง)

        # try: เริ่มบล็อก try-except สำหรับจัดการข้อผิดพลาด
        try:
            # result = alien_to_int(user_input): เรียกใช้ฟังก์ชัน alien_to_int เพื่อแปลง input
            result = alien_to_int(user_input)
            # print(f"..."): แสดงผลลัพธ์การแปลงตัวเลข
            print(f"The Alien numeral '{user_input}' is equal to: {result}\n")
        # except KeyError: จับข้อผิดพลาด KeyError ที่อาจเกิดขึ้นถ้าสัญลักษณ์ใน input ไม่ถูกต้อง (จากการเข้าถึง dictionary)
        except KeyError:
            print("Error: Invalid Alien numeral sequence or unsupported character. Please check your input.\n")
        # except Exception as e: จับข้อผิดพลาดอื่นๆ ที่ไม่คาดคิด
        except Exception as e:
            # print(...): แสดงข้อความผิดพลาดทั่วไปพร้อมรายละเอียด
            print(f"An unexpected error occurred: {e}\n")

    # print(...): แสดงข้อความลาเมื่อออกจากโปรแกรม
    print("Thank you for using the Alien Numeral Converter!")