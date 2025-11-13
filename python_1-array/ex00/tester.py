from give_bmi import give_bmi, apply_limit


def main():
    print(give_bmi.__doc__)
    print(apply_limit.__doc__)
    try:
        print("Valid Values")
        height = [2.71, 25.3]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26), end="\n\n")

        # print("Division per 0")
        # height = [2.71, 0]
        # weight = [165.3, 38.4]
        # bmi = give_bmi(height, weight)
        # print(bmi, type(bmi))
        # print(apply_limit(bmi, 26), end = "\n\n")

        # print("Different lists size")
        # height = [2.71]
        # weight = [165.3, 38.4]
        # bmi = give_bmi(height, weight)
        # print(bmi, type(bmi))
        # print(apply_limit(bmi, 26), end = "\n\n")

        # print("Wrong type in list")
        # height = [2.71, "FSADFsd"]
        # weight = [165.3, 38.4]
        # bmi = give_bmi(height, weight)
        # print(bmi, type(bmi))
        # print(apply_limit(bmi, 26), end = "\n\n")

    except Exception as Error:
        print(Error)


if __name__ == "__main__":
    main()
