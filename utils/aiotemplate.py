from os.path import isfile, join

from aiofiles import open as aopen
from fastapi.responses import HTMLResponse


async def open_template(filepath: str) -> HTMLResponse:
    path = join(
        "templates",
        filepath if filepath.endswith(".html")
        else filepath + ".html"
    )
    if isfile(path):
        async with aopen(path, mode="rb") as html_file:
            return HTMLResponse(await html_file.read())
    else:
        return await error_404()


async def open_markdown(filepath: str) -> HTMLResponse:
    path = join(
        "markdowns",
        filepath if filepath.endswith(".md")
        else filepath + ".md"
    )
    if isfile(path):
        async with aopen(path, mode="rb") as html_file:
            return HTMLResponse(await html_file.read())
    else:
        return await error_404()


async def error_404() -> HTMLResponse:
    async with aopen("404.html", mode="rb") as html_file:
        return HTMLResponse(await html_file.read(), 404)
