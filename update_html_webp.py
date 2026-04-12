import re

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()

        # Replace all case-insensitive .jpg or .jpeg with .webp
        html = re.sub(r'(?i)\.jpeg', '.webp', html)
        html = re.sub(r'(?i)\.jpg', '.webp', html)

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Updated HTML successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
