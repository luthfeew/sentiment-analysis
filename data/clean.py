import os
import re
import demoji


def main():
    # read all file in this directory
    for file in os.listdir():
        if file.endswith(".txt"):
            with open(file, encoding="utf-8") as f:
                # remove empty lines
                lines = [line for line in f if line.strip()]
                # remove spaces at the end of lines
                lines = [line.rstrip() + "\n" for line in lines]
                # remove spaces at the beginning of lines
                lines = [line.lstrip() for line in lines]
                # lowercase
                lines = [line.lower() for line in lines]
                # remove hashtags and mentions
                lines = [re.sub(r"@[a-z0-9_]+", "", line) for line in lines]
                lines = [re.sub(r"#[a-z0-9_]+", "", line) for line in lines]
                # remove urls
                lines = [re.sub(r"https?://[a-z0-9./]+", "", line) for line in lines]
                # remove double spaces
                lines = [re.sub(r"  +", " ", line) for line in lines]
                # remove emojis
                lines = [demoji.replace(line, "") for line in lines]
                # remove punctuation
                lines = [re.sub(r"[()!?]", " ", line) for line in lines]
                lines = [re.sub(r"[.,;:]", " ", line) for line in lines]
                # remove numbers
                lines = [re.sub(r"[0-9]", " ", line) for line in lines]
                # remove quotes and apostrophes
                lines = [re.sub(r"['\"]", "", line) for line in lines]
                lines = [re.sub(r"[“”]", "", line) for line in lines]
                # remove plus minus equals signs
                lines = [re.sub(r"[+=-]", " ", line) for line in lines]
                # remove slashes
                lines = [re.sub(r"[\\/]", " ", line) for line in lines]
                # remove @ and # symbols
                lines = [re.sub(r"[@#]", " ", line) for line in lines]

            # write lines to file
            with open(file, "w", encoding="utf-8") as f:
                f.writelines(lines)


if __name__ == "__main__":
    main()
