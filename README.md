# CareerFit AI

> 취업·공모전 데이터 기반 맞춤형 AI 포트폴리오 코치

---

## 프로젝트 개요

CareerFit AI는 AI와 RAG(Retrieval-Augmented Generation) 기반 기술을 활용하여 사용자의 역량을 분석하고 적합한 채용 공고 및 공모전을 추천하는 커리어 지원 플랫폼입니다.

FastAPI와 Gemini API를 활용한 AI 분석 기능, Pandas 기반 데이터 전처리, ChromaDB 기반 벡터 검색(RAG), React UI를 통해 사용자 친화적인 커리어 분석 서비스를 제공합니다.

---

## 기술 스택

| 영역 | 기술 |
|------|------|
| Backend | Python, FastAPI |
| AI | Gemini 2.5 Flash-Lite |
| Data | Pandas, SQLite, ChromaDB |
| Frontend | React, Vite |
| Deployment | Docker (예정) |

---

## 실행 방법

### Backend

```bash
cd backend
uvicorn app.main:app --reload
```

Swagger

```
http://localhost:8000/docs
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

React

```
http://localhost:5173
```

---

## 주요 기능

- 사용자 역량 입력(Form)
- AI 기반 역량 분석
- RAG 기반 채용공고 검색
- 추천 프로젝트 제안
- 분석 근거(Source Card) 제공
- 분석 결과 UI(Result Card)

---

## 진행 현황

### 완료된 기능

- Python 가상환경 및 프로젝트 개발 환경 구성
- FastAPI 기반 `/health`, `/jobs`, `/analyze` API 구현
- Gemini 2.5 Flash-Lite API 연동
- 환경변수 기반 API Key 관리 및 MOCK_MODE 지원
- 채용·공모전 데이터 수집 및 `jobs.csv` 구성
- Pandas 기반 데이터 전처리 파이프라인 구축
- 결측치 제거 및 스킬 키워드 표준화
- SQLite 데이터 저장
- RAG 문서(JSON) 생성
- ChromaDB 기반 벡터 검색 구현
- Gemini + RAG 기반 답변 생성
- React + Vite 프론트엔드 구축
- InputForm, ResultCard, SourceCard 컴포넌트 구현
- `/analyze` API 연동
- 발표용 UI 개선

---

## 개발 일정

- [x] 1일차 : 프로젝트 기획 및 개발 환경 세팅
- [x] 2일차 : FastAPI 서버 구축 및 Gemini API 연동
- [x] 3일차 : 데이터 전처리 및 RAG 파이프라인 구축
- [x] 4일차 : RAG 기반 서비스 및 React UI 구현
- [ ] 5일차 : Docker 적용 및 포트폴리오 완성