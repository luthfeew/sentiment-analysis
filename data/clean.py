import os


def main():
    # read all file in this directory
    for file in os.listdir():
        if file.endswith(".txt"):
            # remove empty lines
            with open(file, encoding="utf-8") as f:
                lines = [line for line in f if line.strip()]
            # remove spaces at the end of lines
            lines = [line.rstrip() + "\n" for line in lines]
            # write lines to file
            with open(file, "w", encoding="utf-8") as f:
                f.writelines(lines)


if __name__ == "__main__":
    main()
