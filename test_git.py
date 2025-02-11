def calculator():
    while True:
        try:
            num1 = float(input("1つ目の数を入力: "))
            operator = input("演算子を入力 (+, -, *, /): ")
            num2 = float(input("2つ目の数を入力: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("ゼロ除算エラー！")
                    continue
                result = num1 / num2
            else:
                print("無効な演算子です。")
                continue

            print(f"結果: {result}")
        except ValueError:
            print("数値を正しく入力してください。")
        
        again = input("続けますか？ (y/n): ").lower()
        if again != 'y':
            break

calculator()
#"追加1"
#"追加2"
#"追加3"
