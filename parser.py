import sys


def read_dataset(path):
    with open(path) as file:
        test_cases = int(file.readline())

        for test in range(1, test_cases + 1):
            row = int(file.readline()) - 1
            cards = [file.readline() for _ in range(4)]
            selected = set(cards[row].split())

            row = int(file.readline()) - 1
            cards = [file.readline() for _ in range(4)]
            selected &= set(cards[row].split())

            result = "Volunteer cheated!"

            if len(selected) == 1:
                result = str(selected.pop())
            elif len(selected) > 1:
                result = "Bad magician!"

            print("Case #%d: %s" % (test, result))


if __name__ == "__main__":
    read_dataset("file.in")


    if len(sys.argv) != 2:
        print("Usage: python3 magic_trick.py input_file")
        sys.exit(1)

    #main(sys.argv[1])
