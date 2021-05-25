# This is a sample Python script.
import csv


# Press Shift+F10 to execute it or replace it withz your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def convert_csv():
    newRows = []
    totalRows = []
    with open('input.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        flip = False
        item_array = []
        total_array = []

        for row in csv_reader:

            if not flip:
                print('Date ' + row[0])
                print('Price ' + row[3])
                flip = not flip
                item_array.insert(len(item_array), row[0])
                item_array.insert(len(item_array), ',')
                item_array.insert(len(item_array), row[3])
            elif flip:
                print('Name ' + row[1])
                item_array.insert(len(item_array), ',')
                item_array.insert(len(item_array), row[1])
                item_array.insert(len(item_array), ',')

                total_array.insert(0, item_array.copy())
                item_array.clear()
                flip = not flip

            line_count += 1

        with open('eggs.csv', 'w', newline='') as newFile:
            spamwriter = csv.writer(newFile, delimiter=' ')
            spamwriter.writerows(total_array)

        print(f'Processed {line_count} lines.')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Davin')
    convert_csv()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
