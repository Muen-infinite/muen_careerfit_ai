# design-skill.md

# CareerFit AI UI Design Guide

> 취업·공모전 데이터 기반 AI 포트폴리오 코치  
> 대상 사용자: 대학생(취업 준비생)  
> 디자인 키워드: **전문성(Professional) + 친근함(Friendly) + 깔끔함(Clean)**

---

# 1. 컬러 팔레트

## Primary

- Blue-600
- Tailwind: `bg-blue-600`
- 용도
  - 주요 버튼
  - 강조 텍스트
  - 아이콘

Hover

- `hover:bg-blue-700`

---

## Secondary

- Emerald-500
- Tailwind: `bg-emerald-500`

용도

- 성공 메시지
- 추천 결과
- 긍정 피드백

---

## Background

페이지

```text
bg-slate-50
```

카드

```text
bg-white
```

---

## Text

제목

```text
text-slate-800
```

본문

```text
text-slate-600
```

보조 설명

```text
text-slate-400
```

---

## Border

```text
border-slate-200
```

카드 구분용으로만 사용한다.

굵은 Border는 사용하지 않는다.

---

## Error

배경

```text
bg-red-50
```

테두리

```text
border-red-200
```

텍스트

```text
text-red-700
```

---

# 2. 타이포그래피 규칙

## 제목(H1)

```text
text-3xl
font-bold
text-slate-800
```

예시

CareerFit AI

---

## 섹션 제목

```text
text-xl
font-semibold
```

---

## 일반 본문

```text
text-base
leading-7
text-slate-700
```

---

## 설명 문구

```text
text-sm
text-slate-500
```

---

## 버튼

```text
font-medium
text-white
```

---

# 3. 컴포넌트 구조

## App

역할

- 전체 레이아웃 관리
- API 호출
- 상태 관리
- InputForm 연결
- ResultCard 연결
- SourceCard 연결

---

## InputForm

포함 요소

- 전공 선택
- 기술 입력
- 희망 직무 입력
- 분석 버튼

원칙

- 입력 요소 간 간격 유지 (`space-y-4`)
- 버튼은 전체 너비(`w-full`)
- 로딩 시 버튼 비활성화

---

## ResultCard

표시 내용

- AI 분석 결과
- 추천 직무
- 부족한 역량
- confidence(신뢰도)

디자인

```text
rounded-xl
shadow-sm
border
bg-white
```

---

## SourceCard

표시 내용

- 참고한 공고
- 회사명
- 직무명
- 선택 이유

카드 여러 개를 세로로 표시한다.

---

# 4. 레이아웃 규칙

페이지

```text
max-w-2xl
mx-auto
py-10
px-4
```

카드 간격

```text
space-y-4
```

폼 내부

```text
space-y-4
```

결과 영역

```text
mt-8
```

모바일 우선(Mobile First)으로 설계한다.

---

# 5. 금지 사항

❌ 너무 많은 색상 사용

- Primary와 Secondary 중심으로 사용

---

❌ 진한 그림자

사용 금지

```text
shadow-2xl
```

권장

```text
shadow-sm
```

또는

```text
shadow
```

---

❌ 둥근 모서리 과도하게 사용

사용 금지

```text
rounded-full
```

권장

```text
rounded-lg
rounded-xl
```

---

❌ 긴 문단

AI 응답은 카드 형태로 구분한다.

---

❌ 한 화면에 너무 많은 정보 표시

ResultCard와 SourceCard를 분리하여 가독성을 높인다.

---

❌ API Key를 React 코드에 작성하지 않는다.

API Key는 반드시 FastAPI의 `.env`에서 관리한다.

---

# 디자인 원칙

- 전문적이지만 어렵지 않은 느낌
- 대학생이 처음 봐도 이해하기 쉬운 UI
- 흰색 배경 중심의 미니멀 디자인
- 일관된 여백과 카드 스타일 유지
- 모바일과 데스크톱 모두 자연스럽게 표시

— CareerFit AI UI 디자인 규칙



## 컬러 팔레트

- primary: #3B82F6 (파란색 — 신뢰, 전문성)

- secondary: #10B981 (초록색 — 성장, 추천)

- background: #F8FAFC (연한 회색)

- text-primary: #1E293B

- text-muted: #64748B

- border: #E2E8F0

- error: #EF4444



## 타이포그래피

- 제목: text-2xl font-bold text-slate-800

- 소제목: text-lg font-semibold text-slate-700

- 본문: text-base text-slate-600

- 설명: text-sm text-slate-500



## 컴포넌트 구조

- App.jsx: 최상위, 상태 관리, API 요청

- InputForm.jsx: 전공·스킬·직무 입력 폼

- ResultCard.jsx: AI 분석 답변 출력 (초록 왼쪽 테두리)

- SourceCard.jsx: 출처 공고 목록 출력



## 레이아웃 규칙

- 최대 너비: max-w-2xl mx-auto

- 카드 내부 여백: p-6

- 컴포넌트 간격: gap-4 / space-y-4

- 모서리: rounded-xl (카드), rounded-lg (버튼)



## 금지 사항

- API Key를 화면에 표시하거나 localStorage에 저장

- 다크 배경에 흰 텍스트 (가독성 우선)

- 아이콘 없이 버튼만 사용 (텍스트 레이블 필수)