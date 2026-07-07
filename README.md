# CareerFit AI

> 취업·공모전 데이터 기반 맞춤형 AI 포트폴리오 코치

---

## 프로젝트 개요

취업을 준비하는 학생들은 관심 직무에 필요한 역량과 자신의 현재 역량을 객관적으로 파악하기 어렵습니다. 또한 채용 공고와 공모전 정보를 일일이 찾아 비교해야 해 취업 준비 방향을 설정하는 데 많은 시간과 노력이 필요합니다.

CareerFit AI는 RAG(Retrieval-Augmented Generation) 구조를 활용하여 채용 공고 데이터를 검색한 뒤, Gemini AI가 사용자의 전공, 보유 스킬, 관심 직무를 분석해 맞춤형 역량 분석과 추천 프로젝트, 공모전 준비 전략을 제공합니다.

---

## 🛠 기술 스택

| 영역 | 기술 |

|---|---|

| 백엔드 | Python 3.11, FastAPI |

| AI API | Gemini 2.5 Flash-Lite |

| 데이터 | Pandas, SQLite, ChromaDB |

| 프론트엔드 | React, Vite |

| 실행 환경 | Docker |

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

## ✨ 주요 기능

- RAG 기반 역량 분석: 취업 공고 데이터를 근거로 맞춤형 조언 제공

- 출처 표시: 어떤 공고 데이터를 참고했는지 sources로 함께 반환

- Mock Mode: API 한도 초과 시 MOCK_MODE=true 로 폴백 가능

---
## 📁 프로젝트 구조

```

careerfit-ai/

├── backend/ # FastAPI 서버

│ ├── main.py

│ ├── routers/

│ ├── services/

│ ├── data/

│ └── Dockerfile

├── frontend/ # React UI

└── docs/ # 하네스 파일 모음

```
## 📝 개발 과정

[본인이 가장 어려웠던 부분과 해결 과정 1~2문장]

```5일차 초반부분에 여러 디버깅 문제때문에 계속 수업에 따라가지 못하는 상태에서 도커 설정이 들어가서 이후에 혼자서 했을때 좀 애를 먹었다. 
Wsl2 이 제대로 설치되지 않아서 윈도우 파워쉘에서 윈도우 버전을 확인하고 그 이후에 설치해주니 이번엔 잘 설치 되었다. 

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
- [x] 5일차 : Docker 적용 및 포트폴리오 완성


## Demo

- Live Demo:https://muen-careerfit-ai.onrender.com/docs

## Developer

- Name: 권지윤

- Role: 컴퓨터공학과 학생

- Email: ebzmahs0306@gmail.com