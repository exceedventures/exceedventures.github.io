def is_special_start(line):
    """라인이 알파벳 대문자, 아라비아 숫자, 또는 "로 시작하는지 확인."""
    return line and (line[0].isupper() or line[0].isdigit() or line[0] == '"')

# 1. ./input.txt 파일에서 한 라인을 읽어와서 버퍼에 저장한다.
with open('./input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

buffer = ""
with open('./final.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        line = line.strip()
        if is_special_start(line):
            # 버퍼에 저장된 내용을 final.txt에 한 라인으로 출력
            if buffer:
                file.write(buffer + '\n')
            # 현재 라인을 버퍼에 저장
            buffer = line
        else:
            # 버퍼에 현재 라인을 추가
            if buffer:
                buffer += ' ' + line
            else:
                buffer = line

    # 더이상 읽을 라인이 없으면 저장된 버퍼를 한 라인으로 final.txt 에 출력한다.
    if buffer:
        file.write(buffer + '\n')