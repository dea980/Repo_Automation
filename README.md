# Google Form Automation (구글 폼 자동화)

TIL(Today I Learned) 제출을 자동화하는 프로그램입니다. 구글 폼에 이름, 블로그 링크, TIL 작성일자, 날씨 정보를 자동으로 제출합니다.

## 설치 방법

1. Chrome 브라우저 설치:
   - 프로그램이 Chrome 브라우저를 사용하므로 반드시 설치되어 있어야 합니다.
   - [Chrome 다운로드](https://www.google.com/chrome/)

2. Chrome WebDriver 설치:
   - Chrome 브라우저 버전과 일치하는 WebDriver가 필요합니다.
   - WebDriver는 프로그램이 자동으로 관리합니다.

3. Python 의존성 설치:
   ```bash
   pip install -r requirements.txt
   ```

## 사용 방법

### 단일 항목 제출
```python
from main import GoogleFormAutomation

# 자동화 클래스 초기화
form = GoogleFormAutomation()

# 단일 항목 제출
entry = {
    'name': '홍길동',
    'blog_link': 'https://blog.example.com/hong',
    'til_date': '2024-12-30',
    'weather': '맑음'  # 맑음, 흐림, 비, 천둥 중 선택
}

form.submit_form(entry)
```

### 여러 항목 일괄 제출
```python
# 여러 항목 준비
entries = [
    {
        'name': '김철수',
        'blog_link': 'https://blog.example.com/kim',
        'til_date': '2024-12-30',
        'weather': '흐림'
    },
    {
        'name': '이영희',
        'blog_link': 'https://blog.example.com/lee',
        'til_date': '2024-12-30',
        'weather': '비'
    }
]

# 일괄 제출
form.submit_multiple_entries(entries)
```

## 날씨 옵션

입력 가능한 날씨 옵션:
- `맑음`: 맑음 (기분 좋아요)
- `흐림`: 흐림 (그냥 그래요)
- `비`: 비 (힘들어요)
- `천둥`: 천둥/번개 (궂일이에요)

## 주요 기능

- 구글 폼 자동 입력 및 제출
- 단일/다중 항목 제출 지원
- 브라우저 자동화로 실제 폼 제출 과정 시뮬레이션
- 오류 처리 및 로깅
- 헤드리스 모드 지원 (옵션)

## 파일 구조

- `main.py`: 메인 자동화 클래스 및 로직
- `requirements.txt`: Python 의존성

## 로깅

모든 제출 과정은 `form_automation.log` 파일에 기록됩니다:
- 성공적인 제출
- 제출 실패 및 오류
- 디버깅 정보

## 주의사항

1. 안정적인 인터넷 연결이 필요합니다.
2. Chrome 브라우저가 설치되어 있어야 합니다.
3. 브라우저 자동화는 시스템 리소스를 사용하므로, 다른 작업에 영향을 줄 수 있습니다.
4. 대량의 자동 제출은 구글 폼의 정책에 위배될 수 있으므로 적절한 간격을 두고 사용하세요.
