import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if url := re.search(r"^<iframe.+https?://(?:www\.)?youtube\.com/embed/(.+)", s, re.IGNORECASE):
        url = url.group(1).split('"')

        return f"https://youtu.be/{url[0]}"

if __name__ == "__main__":
    main()