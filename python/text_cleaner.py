import re

def read_file(file_path):
    """파일을 읽어 내용을 반환합니다."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def is_chapter_line(line):
    """라인이 챕터 목록 형식인지 확인합니다."""
    return re.match(r'^\s*[IVXLCDM]+\.', line.strip()) is not None

def clean_and_split_sentences(text):
    """텍스트를 정리하고 문장으로 나눕니다."""
    # 문장 끝을 나타내는 정규 표현식
    sentence_endings = re.compile(r'([.!?]["\']?)\s+')
    sentences = []
    start = 0

    for match in sentence_endings.finditer(text):
        end = match.end()
        sentence = text[start:end].strip()
        if len(sentence) >= 10:
            sentences.append(sentence)
        start = end

    # 마지막 문장 추가
    last_sentence = text[start:].strip()
    if len(last_sentence) >= 10:
        sentences.append(last_sentence)

    return sentences

def process_text(content):
    """텍스트를 처리하여 유효한 문장과 챕터 목록을 반환합니다."""
    # 큰따옴표로 시작하는 경우를 처리하기 위한 정규 표현식
    quote_start_pattern = re.compile(r'^\s*"([^"]+)')

    # 공백 라인 두 번 이상 연속된 부분을 기준으로 텍스트 분리
    paragraphs = re.split(r'\n\s*\n\s*\n', content)
    processed_sentences = []
    previous_sentence = ""

    for paragraph in paragraphs:
        lines = paragraph.split('\n')
        
        for line in lines:
            stripped_line = line.strip()

            # 큰따옴표로 시작하는 경우 처리
            if quote_start_pattern.match(stripped_line):
                if previous_sentence:
                    processed_sentences.append(previous_sentence)
                    previous_sentence = ""
                processed_sentences.append(stripped_line)
                continue
            
            # 큰따옴표로 끝나는 경우 처리
            if stripped_line.endswith('"'):
                if previous_sentence:
                    processed_sentences.append(previous_sentence + " " + stripped_line)
                    previous_sentence = ""
                else:
                    processed_sentences.append(stripped_line)
                continue

            # 챕터 목록 형식의 라인 처리
            if is_chapter_line(line):
                if previous_sentence:
                    processed_sentences.append(previous_sentence)
                    previous_sentence = ""
                processed_sentences.append(line.strip())
            else:
                if len(stripped_line) >= 10:
                    if previous_sentence:
                        processed_sentences.append(previous_sentence + " " + stripped_line)
                        previous_sentence = ""
                    else:
                        previous_sentence = stripped_line
                elif previous_sentence:
                    previous_sentence += " " + stripped_line

        if previous_sentence:
            processed_sentences.append(previous_sentence)
            previous_sentence = ""
    
    return processed_sentences

def write_file(file_path, sentences):
    """문장을 파일에 씁니다."""
    with open(file_path, 'w', encoding='utf-8') as file:
        for sentence in sentences:
            file.write(sentence + '\n')

def main(input_file_path, output_file_path):
    content = read_file(input_file_path)
    sentences = process_text(content)
    write_file(output_file_path, sentences)
    print(f"정리된 문장을 '{output_file_path}'에 저장했습니다.")

if __name__ == "__main__":
    input_file_path = 'input.txt'
    output_file_path = 'renew.txt'
    main(input_file_path, output_file_path)