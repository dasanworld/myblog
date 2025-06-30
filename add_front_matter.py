import os
import re

POSTS_DIR = "_posts"

def extract_date_from_filename(filename):
    # 예시: 20250622_1401_nbc_News.md
    match = re.match(r"(\d{8})_(\d{4})_", filename)
    if not match:
        return None
    yyyymmdd = match.group(1)
    hhmm = match.group(2)
    date_str = f"{yyyymmdd[:4]}-{yyyymmdd[4:6]}-{yyyymmdd[6:]} {hhmm[:2]}:{hhmm[2:]}:00 +0900"
    return date_str

for fname in os.listdir(POSTS_DIR):
    if not fname.endswith('.md'):
        continue
    fpath = os.path.join(POSTS_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    # 이미 front matter가 있으면 건너뜀
    if content.strip().startswith('---'):
        continue
    # title: 파일명에서 확장자 빼기
    title = fname.replace('.md','')
    date = extract_date_from_filename(fname)
    if not date:
        print(f"날짜 추출 실패: {fname}")
        continue
    front_matter = f"""---
title: "{title}"
date: {date}
---

"""
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(front_matter + content)
    print(f"Front matter 추가: {fname}")
