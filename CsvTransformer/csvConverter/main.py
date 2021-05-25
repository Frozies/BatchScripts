# This is a sample Python script.
import csv


# Press Shift+F10 to execute it or replace it withz your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def convert_csv():
    newRows = []
    with open('input.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # if line_count == 0:
            #     # Column Names
            #     print(f'Column names are {", ".join(row)}')
            #     #write first line to new file
            #     line_count += 1

            name = ''
            date = ''
            price = ''
            if line_count == 0:
                date = row[0]
                price = row[2]
            if line_count == 1:
                name = row[1]
            if line_count == 2:
                date = row[0]
                price = row[2]

            if line_count >= 3:
                if line_count % 2 != 1:
                    # Rows on index 1 line
                    # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                    # Write specific rows[1] + "," in the correct order
                    date = row[0]
                    price = row[2]
                    # 1=date,3=price
                if line_count % 2 == 1:
                    name = row[1]
                    # 2=itemname
            if date != '':
                newRows.insert(0, date)

            if name != '':
                newRows.insert(0, name)
            if price != '':
                newRows.insert(0, price)

            line_count += 1
            print("Row: " + newRows.__str__())


        with open('eggs.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ')
            spamwriter.writerows(newRows)

        print(f'Processed {line_count} lines.')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Davin')
    convert_csv()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
