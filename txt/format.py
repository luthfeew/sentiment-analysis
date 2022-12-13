def main():
    f = open("output_raw_id_4.txt", encoding="utf-8")
    
    # remove empty lines
    lines = [line for line in f if line.strip()]

    # write lines to file
    with open("output_raw_id_4_f.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
