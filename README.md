# 블로그 링크 일괄 제출 자동화 프로그램

이 프로그램은 여러 개의 블로그 링크를 Google Form에 자동으로 제출하는 도구입니다. 이름, 날짜, 날씨는 한 번만 입력하고, 여러 블로그 링크를 동일한 정보로 제출할 수 있습니다.

## 주요 기능

- 한 번의 이름, 날짜, 날씨 입력으로 여러 블로그 링크 제출
- 자동화된 Google Form 작성
- 제출 결과 자동 로깅

## 설치 방법

1. 필수 프로그램 설치:
   - Python 3.x
   - Chrome 웹 브라우저

2. 패키지 설치:
```bash
pip install -r requirements.txt
```

## 사용 방법

1. 공통 정보와 블로그 링크들을 다음과 같이 준비합니다:

```python
# 모든 제출에 사용될 공통 정보
common_data = {
    'name': '홍길동',
    'til_date': '2024-12-30',
    'weather': '맑음'
}

# 제출할 블로그 링크 목록
blog_links = [
    'https://blog.example.com/post1',
    'https://blog.example.com/post2',
    'https://blog.example.com/post3'
]
```

2. 프로그램 실행:
```bash
python main.py
```

## 입력 데이터 형식

### 공통 정보 (한 번만 입력)
- `name`: 이름
- `til_date`: TIL 작성 날짜 (YYYY-MM-DD 형식)
- `weather`: 날씨 (옵션: '맑음', '흐림', '비', '천둥')

### 블로그 링크
- 여러 개의 블로그 URL을 리스트 형태로 입력

## 실행 결과

- 각 블로그 링크별 제출 결과가 `form_automation.log` 파일에 기록됩니다
- 콘솔에서 실시간으로 제출 진행 상황을 확인할 수 있습니다

## 주의사항

- 안정적인 인터넷 연결이 필요합니다
- Chrome 브라우저가 설치되어 있어야 합니다
- 한 번에 너무 많은 링크를 제출하면 Google Form에서 일시적으로 차단될 수 있습니다
