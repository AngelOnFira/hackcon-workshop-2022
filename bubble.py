def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list


def main():
    arr = [8, 3, 6, 1, 9]
    print(bubble_sort(arr))


if __name__ == "__main__":
    main()
