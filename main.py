import os

ENTRY = "By spring you will outgrow this pot, and your keeper will repot you — this windowsill has saved its best light for you."  # 119 chars, one line, kind fortune for the houseplant on the windowsill

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
