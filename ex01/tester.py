from in_out import outer, square, pow


def main():
    """Main function to test the outer, square, pow functions."""

    try:
        my_counter = outer(3, square)
        print(my_counter())
        print(my_counter())
        print(my_counter())
        print("---")
        another_counter = outer(1.5, pow)
        print(another_counter())
        print(another_counter())
        print(another_counter())

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
