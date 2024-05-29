# Python and fastAPI

## Install deps
- go to lesson folder: `cd lessons`
- create virtual environement: `python -m venv venv`
- activate virtual environement: `venv\Scripts\activate`
- install dependencies: `pip install -r requirements.txt`
- run fastapi app: `fastapi dev MAINFILEPATH` example: `fastapi dev main.py`

## Types

- int
- float
- bool
- bytes
- list: list[str]
- tuple: tuple[int, int, str]
- set: set[bytes]
- dict: dict[str, float]
- Union: int | str régen Union[int, str]
- Optional: str | None = None régen Optional[str] = None 
- Pydantic models 
  ```python
  class User(BaseModel):
      id: int
      name: str = "John Doe"
      signup_ts: datetime | None = None
      friends: list[int] = []
  ```
- metadata: `def say_hello(name: Annotated[str, "this is just metadata"]) -> str:`


## Docs
- uvicorn: [https://www.uvicorn.org/](https://www.uvicorn.org/)
- semver: [https://semver.org/](https://semver.org/)
- pydantic: [https://docs.pydantic.dev/latest/](https://docs.pydantic.dev/latest/)
- fastAPI: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)

## Other tools and "things"
- hypercorn: uvicorn altrnative [https://hypercorn.readthedocs.io/en/latest/index.html](https://hypercorn.readthedocs.io/en/latest/index.html)
- Pypi [https://pypi.org/](https://pypi.org/)
- Színes, szagos powershell: [https://ohmyposh.dev/](https://ohmyposh.dev/)
- Win package manager: [https://community.chocolatey.org/](https://community.chocolatey.org/)