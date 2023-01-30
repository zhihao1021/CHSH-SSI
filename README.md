# Web-PPT
> Made brief by HTML, and running web server by simple script, providing the any device in the local network to access。

## Feature
1. Easy to deploy.
2. Host anywhere, even on an android phone.
3. Support markdown files.
4. Free for all.

## How to Run
0. Create a virtual environment of python and activate(Optional).
    ```
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

1. Install the package.
    ```
    pip install -r .\requirements.txt
    ```

2. Run - There are two method to run the script.
   - Use Command Line.
    ```
    uvicorn main:app --host 0.0.0.0 --port 8080
    ```
   - Use Python Script.
   ```
   python main.py

   # The first times run with python script will generate a config.
   # Default values of host and port are 0.0.0.0 and 8080.
   # You can modify it by edit config.json in the directory
    ```

3. Open the browser on any device oin the local network, and connect to the ip and port display on the terminal windows of the server you run the script.

## Modify the Page
The method of changing page is using hash in the url, therefore there is needless to reload the website when switch the page.

The kernel of the front-site operation is in the `templates/index.html`, the only place user need to modify is style.

If you want to create a new page, you can create a new file named `page-<index>.html` in the `pages` directory. Remember that the index must follow the order starting from 1 or it will not be loaded. If you want to switch to another page which not the sibling of the page, you can easily done it by change the url hash to the `page-<index>` py run the javascript: `windows.hash = "page-<index>";`.

To embed an markdown file into the page, you can use the `zero-md` tag like `<zero-md src="/markdowns/README.md"><zero-md>`(there is an example in `pages/page-2.html`). The files under the `markdowns` directory will map to the route `/markdown` as `static` to `/static`.

## Develope Environment
```
 - Windows:
    - Version: Windows 10 Pro 22H2
    - OS Build: 19045.2251
 
 - Environment
    - Python: 3.10.4
    - pip: 22.0.4
    - FFmpeg: 2022-04-28-git-ec07b15477-full_build
 
 - Browser
    - Opera GX
       - Version: LVL 4 (core: 94.0.4606.79)
       - Chromium Version: 108.0.5359.125

 - IDE
    - Visual Studio Code     v1.74.3
    - Extensions
       - Pylance             v2022.3.1
       - Python              v2022.20.2
       - HTML CSS Support    v1.13.1
       - Markdown All in One v3.5.0
```

## Developer Say
If you like this repo, please click the star button at the upper right corner of this page.

If there some bugs in the code, please open a issue.