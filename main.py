def evaluate_hours(hours):
    if hours < 2:
        return "Quá ít. Bạn đang không nghiêm túc."
    elif hours <= 5:
        return "Ổn. Nhưng chưa đủ để vượt người khác."
    else:
        return "Tốt. Giữ kỷ luật này."


def main():
    print("=== DK AI Starter ===")
    
    name = input("Tên của bạn: ")
    goal = input("Mục tiêu của bạn là gì: ")
    
    print(f"\nChào {name}.")
    print(f"Mục tiêu của bạn: {goal}")
    
    hours = int(input("Bạn học AI bao nhiêu giờ mỗi ngày: "))
    result = evaluate_hours(hours)
    
    print(result)
    print("\nCommit mỗi ngày. Không excuse.")


if __name__ == "__main__":
    main()