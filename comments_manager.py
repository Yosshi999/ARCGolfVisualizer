from pathlib import Path
import re
from datetime import datetime
from flask import render_template_string
from urllib.parse import quote,unquote

class Comment:
    def __init__(self,time,text):
        self.time = time
        self.text = text
    
    @classmethod
    def from_form(self,data):
        time=f"{datetime.now().strftime('%Y%m%d%H%M%S')}"
        return Comment(time=time,text=data["comment"])

    def is_empty(self):
        return self.text.strip() == ""

    def pp_text(self):
        texts = re.split(r"(@\d{3}|#[^\W]+)",self.text)
        template = ""
        vars_dict = {}
        var_cnt = 0
        def gen_var():
            nonlocal var_cnt
            var_cnt += 1
            return f"var{var_cnt}"

        for text in texts:
            if (m := re.match(r"^(@(\d{3}))$",text)):
                s = m.group(2)
                template += f'<a href="/problem/task{s}" target="_blank">@{s}</a>'
            elif (m := re.match(r"^(#[^\W]+)$",text)):
                s = m.group(1)
                template += f'<a href="/search/{quote(s)}" target="_blank">{s}</a>'
            else:
                v = gen_var()
                template += "{{" + v + "}}"
                vars_dict[v] = text

        return render_template_string(template,**vars_dict)

COMMENTS = Path("comments")

class Comments_manager:
    def __init__(self):
        self.cache={}
    # get comments for problem [task]
    def get_comments(self,task):
        if not task in self.cache:
            base = COMMENTS
            data = set()
            for fn in (base / task).glob("*.comment"):
                try:
                    m = re.match("(\d+).comment",fn.name)
                    time = m.group(1)
                    data.add(Comment(time=time,text=open(fn,"r").read()))
                except Exception as e:
                    print(f"Failed for loading comment {fn}")
            self.cache[task] = data
        
        return self.cache[task]
    
    def save_comment(self,task,comment):
        print("save",task,comment)
        (COMMENTS / task).mkdir(exist_ok=True)
        fp = COMMENTS / task / f"{comment.time}.comment"
        fp.write_bytes(comment.text.encode("utf-8"))
        self.cache[task].add(comment)
    