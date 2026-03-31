def main():
    print("=== DK AI Starter ===")
    
    name = input("Tên của bạn: ")
    goal = input("Mục tiêu của bạn là gì: ")
    
    print(f"\nChào {name}.")
    print(f"Mục tiêu của bạn: {goal}")
    
    if "AI" in goal.upper():
        print("Tốt. Bạn đang đi đúng hướng.")
    else:
        print("Sai hướng rồi. Quay lại học AI.")

    print("\nCommit mỗi ngày. Không excuse.")
    
    hours = int(input("Bạn học AI bao nhiêu giờ mỗi ngày: "))

    if hours < 2:
        print("Quá ít. Bạn đang không nghiêm túc.")
    elif hours <= 5:
        print("Ổn. Nhưng chưa đủ để vượt người khác.")
    else:
        print("Tốt. Giữ kỷ luật này.")

if __name__ == "__main__":
    main()