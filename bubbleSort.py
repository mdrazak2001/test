# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def bubbleSort(elements):
    n = len(elements)
    # 100 90 30 70
    for i in range(n):
        for j in range(0, n - i - 1):

            if elements[j + 1] < elements[j]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]

    return elements



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    elements = [-1000, 9, 20, 19, -10]
    res = bubbleSort(elements)
    for num in res:
        print(num)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
