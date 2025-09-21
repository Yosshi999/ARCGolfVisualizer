from pathlib import Path
import re
from datetime import datetime

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
    