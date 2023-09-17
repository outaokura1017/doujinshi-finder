import requests
import re
def nyahentai(string:str):
    r = requests.get(f"https://nyahentai.re/?s={string}")
    match = re.search(r'https://nyahentai\.re/fanzine/re([^/]+)', r.text)
    if match:
        r18path = match.group(1)
        if '"' in r18path:
            r18path = r18path[:r18path.find('"')]  # ダブルクオーテーション（"）の前の部分を抽出
        else:    
            r18path = r18path
        print('https://nyahentai.re/fanzine/re' + r18path)
        global a
        a += 1
    else:
        a += 0

def momonga(string:str):
    r = requests.get(f"https://momon-ga.com/?s={string}")
    match = re.search(r'https://momon-ga\.com/fanzine/mo([^/]+)', r.text)
    if match:
        r18path = match.group(1)
        if '"' in r18path:
            r18path = r18path[:r18path.find('"')]  # ダブルクオーテーション（"）の前の部分を抽出
        else:    
            r18path = r18path
        print('https://momon-ga.com/fanzine/mo' + r18path)
        global a
        a += 1
    else:
        a += 0

def doujinantena(string:str):
    r = requests.get(f"https://doujinantena.top/?s={string}")
    match = re.search(r'https://doujinantena\.top/comic/do([^/]+)', r.text)
    if match:
        r18path = match.group(1)
        if '"' in r18path:
            r18path = r18path[:r18path.find('"')]  # ダブルクオーテーション（"）の前の部分を抽出
        else:    
            r18path = r18path
        print('https://doujinantena/comic/do' + r18path)
        global a
        a += 1
    else:
        a += 0

def dddsmart(string:str):
    r = requests.get(f"https://ddd-smart.net/search.php?keyword={string}")
    match = re.search(r'/doujinshi3/([^/]+)', r.text)
    if match:
        r18path = match.group(1).replace('" target="',"").replace('"><',"").replace("&page=0&from=search&from=package-list_self", "")
        if '"' in r18path:
            r18path = r18path[:r18path.find('"')]  # ダブルクオーテーション（"）の前の部分を抽出
        else:    
            r18path = r18path
        print('https://ddd-smart.net/doujinshi3/' + r18path)
        global a
        a += 1
    else:
        a += 0


def doujinnomori(string:str):
    r = requests.get(f"https://doujinnomori.com/comics/free-search?type=&id=&keyword={string}")
    match = re.search(r'comics/detail([^/]+)', r.text)
    if match:
        r18path = match.group(1).replace('" class="1ede1ee8-1041-4d3b-b4b8-833258fee1ff" target="_blank">', "").replace("<figure>", "").replace('<img class="comic__img 1ede1ee8-1041-4d3b-b4b8-833258fee1ff" src="https:', "").replace(" ","")
        r18path = '\n'.join(line for line in r18path.splitlines() if line.strip())
        if '"' in r18path:
            r18path = r18path[:r18path.find('"')]  # ダブルクオーテーション（"）の前の部分を抽出
        else:    
            r18path = r18path
        print('https://doujinnomori.com/comics/detail' + r18path)
        global a
        a += 1
    else:
        a += 0

def shinshimanga(string:str):
    r = requests.get(f"https://shinshi-manga.net/comics/free-search?keyword=https://shinshi-manga.net/comics/free-search?keyword=ksdjkfedjoafej09afeh9afeh0iafedjdkdkdjksdldlsldlskdioawjdiopwjd")
    match = re.search(r'/comics/detail([^/]+)', r.text)
    noosusume = match.group(1).replace('" class="post__link 652a67c2-f2b0-4cb8-b0d5-45d617147884" target="_blank"><', "").replace('" class="post__link a49f17c8-e95a-4483-90cf-b79dac9aee9a" target="_blank"><', "")
    noosusume= '\n'.join(line for line in noosusume.splitlines() if line.strip())
    r = requests.get(f"https://shinshi-manga.net/comics/free-search?keyword={string}")
    match = re.search(r'/comics/detail([^/]+)', r.text)
    if match:
        global a
        r18path = match.group(1).replace('" class="post__link 652a67c2-f2b0-4cb8-b0d5-45d617147884" target="_blank"><', "").replace('" class="post__link a49f17c8-e95a-4483-90cf-b79dac9aee9a" target="_blank"><', "")
        r18path= '\n'.join(line for line in r18path.splitlines() if line.strip())
        if '"' in r18path:
            r18path = r18path[:r18path.find('"')]  # ダブルクオーテーション（"）の前の部分を抽出
        else:    
            r18path = r18path
        if r18path==noosusume:
            a += 0
            return
        print('https://shinshi-manga.net/comics/detail' + r18path)
        a += 1
    else:
        a += 0

aaa = input("nya!: ")
global a
a = 0
shinshimanga(aaa)
if a==1:
    print("founded")
    input()
else:
    doujinnomori(aaa)
    if a==1:
        input()
    else:
        dddsmart(aaa)
        if a==1:
            input()
        else:
            nyahentai(aaa)
            if a==1:
                input()
            else:
                momonga(aaa)
                if a==1:
                    input()
                else:
                    doujinantena(aaa)
                    if a==1:
                        input()
                    else:
                        print("not found")
