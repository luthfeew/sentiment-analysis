import os
import re
from cleantext import clean


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
                # remove emojis
                lines = [clean(line, no_line_breaks=True, no_urls=True, no_emails=True, no_phone_numbers=True, no_numbers=True, no_digits=True, no_currency_symbols=True, no_punct=True, replace_with_url="", replace_with_email="", replace_with_phone_number="", replace_with_number="", replace_with_digit="", replace_with_currency_symbol="", lang="id") for line in lines]

            # write lines to file
            with open(file, "w", encoding="utf-8") as f:
                f.writelines(lines)


if __name__ == "__main__":
    main()
