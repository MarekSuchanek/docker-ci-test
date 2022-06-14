import fastapi

app = fastapi.FastAPI(
    title='Hello-World',
    version='1.0.0',
)

@app.get(path='/')
async def get_info():
    return fastapi.Response(
        content='Hello world!',
        media_type='text/plain',
    )
