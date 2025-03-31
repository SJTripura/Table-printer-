
def print_multiplication_table():
    try:
        table_number = int(input("Enter Table number: "))
        table_length = int(input("Enter Length of table: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    for i in range(1, table_length + 1):
        print(f"{table_number} x {i} = {table_number * i}")

if __name__ == "__main__":
    print_multiplication_table()
