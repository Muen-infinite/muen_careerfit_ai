# backend/routers/health.py
# health.py 파일
# 서버가 정상적으로 실행되고 있는지 확인하는 API를 만드는 파일이다.


# FastAPI에서 APIRouter 클래스를 가져온다.
# APIRouter는 여러 개의 API를 그룹(폴더)처럼 관리할 수 있게 해준다.
from fastapi import APIRouter


# APIRouter 객체를 생성한다.
# 앞으로 이 router 안에 여러 개의 API(주소)를 등록하게 된다.
router = APIRouter()


# "/health" 주소로 GET 요청이 들어오면
# 바로 아래의 health_check() 함수를 실행한다.
#
# tags=["System"]은 Swagger UI에서
# "System"이라는 그룹으로 묶어 보여주기 위한 설정이다.
@router.get("/health", tags=["System"])


# health_check라는 함수를 만든다.
# 함수 이름은 자유롭게 지을 수 있지만,
# "서버 상태를 확인한다"는 의미를 담아 이렇게 이름을 지었다.
def health_check():

    """
    여러 줄 문자열(Docstring)

    이 함수가 어떤 역할을 하는지 설명하는 문서이다.
    Python이나 Swagger가 이 내용을 읽어서 개발자에게 보여줄 수도 있다.

    실제 프로그램 실행에는 거의 영향을 주지 않고,
    설명서 역할을 한다.
    """

    # 딕셔너리(Dictionary)를 반환한다.
    # FastAPI는 이 딕셔너리를 자동으로 JSON 형태로 변환해서
    # 브라우저나 React에게 보내준다.
    return {

        # 서버가 정상이라는 상태값
        "status": "ok",

        # 사람이 읽기 쉬운 설명 메시지
        "message": "CareerFit AI 서버가 정상 동작 중입니다."
    }