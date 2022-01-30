def main():
    with open(file="users.txt", mode="w", encoding="utf-8") as f:
        # 書き込み(上書き)　-> w  ,追加  -> a
        f.write("Bob,79\n")

        f.write("Tom,59")
    #     print("withの中:", f.closed)
    # print("withの外:", f.closed)  ->


if __name__ == '__main__':
    main()
