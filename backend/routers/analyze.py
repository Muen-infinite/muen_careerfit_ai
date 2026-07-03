# backend/routers/analyze.py

from fastapi import APIRouter

from pydantic import BaseModel

from typing import List

from services.llm_service import get_llm_response

router = APIRouter()

# 요청 본문(Request Body) 모델

# 손님이 제출하는 주문서 양식

class AnalyzeRequest(BaseModel):

    major: str          # 전공 (예: "통계학과")

    skills: List[str]      # 보유 스킬 목록 (예: ["Python", "SQL"])

    job_type: str        # 관심 직무 (예: "데이터 분석")
    experience_years: int = 0
    preferred_company_size: str = "무관"

# 응답 본문(Response Body) 모델

# 주방에서 손님에게 돌려주는 영수증 양식

class AnalyzeResponse(BaseModel):

    answer: str         # AI 분석 결과 텍스트

    sources: List[dict]     # 답변 근거 데이터 목록



@router.post("/analyze", response_model=AnalyzeResponse, tags=["Analyze"])
def analyze_career(request: AnalyzeRequest):

    query = (
        f"전공: {request.major}\n"
        f"보유 기술: {', '.join(request.skills)}\n"
        f"희망 직무: {request.job_type}\n"
        f"경력: {request.experience_years}년\n"
        f"희망 기업 규모: {request.preferred_company_size}"
    )

    context_docs = []

    result = get_llm_response(query, context_docs)

    return AnalyzeResponse(
        answer=result["answer"],
        sources=result["sources"]
    )
    