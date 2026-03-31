def main():
    print("=== Simple AI Test Program ===")
    
    name = input("Nhập tên của bạn: ")
    age = int(input("Nhập tuổi của bạn: "))
    
    print(f"Xin chào {name}!")
    
    if age < 18:
        print("Bạn còn trẻ, cứ học thật chắc nền tảng.")
    elif age < 23:
        print("Đây là giai đoạn vàng để build skill và đi thực tập.")
    else:
        print("Tập trung tạo giá trị và kiếm tiền.")

    # mini logic AI giả lập
    score = int(input("Nhập điểm của bạn (0-10): "))
    
    if score >= 8:
        print("Bạn đang làm rất tốt.")
    elif score >= 5:
        print("Ổn, nhưng chưa đủ. Đẩy thêm.")
    else:
        print("Thẳng thắn: bạn đang yếu. Phải cày lại.")


if __name__ == "__main__":
    main()