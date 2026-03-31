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

if __name__ == "__main__":
    main()