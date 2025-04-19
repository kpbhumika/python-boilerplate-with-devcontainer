from fastapi.responses import JSONResponse
from fastapi import APIRouter, Request


api_router = APIRouter()

@api_router.get("/test",response_class=JSONResponse)
async def test(request: Request):
    # return a test json response
    return {"message": "This is a test endpoint"}

@api_router.post("/testPost",response_class=JSONResponse)
async def testPost(request: Request):
    request_body = await request.json()
    # return a test json response
    return {"message": "This is a test endpoint"}
