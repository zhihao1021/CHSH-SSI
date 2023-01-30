from os.path import isfile, join

from ujson import loads

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

async def open_page(filepath: str) -> HTMLResponse:
    async with aopen("templates/pages/map.json", mode="r") as map_file:
        map_data: dict = loads(await map_file.read())
    filepath = map_data.get(filepath.removesuffix(".html"), filepath)
    if filepath == None:
        return await error_404()
    path = join(
        "templates/pages",
        filepath if filepath.endswith(".html")
        else filepath + ".html"
    )
    if isfile(path):
        async with aopen(path, mode="rb") as html_file:
            res = await html_file.read()
            return HTMLResponse(res.replace(
                b"#page-n",
                ("#" + filepath.removesuffix(".html")).encode())
            )
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
