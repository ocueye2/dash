import sys
import os
def load(path):
    f = open(path)
    return f.read()

def prepare(config):
    config = config.splitlines()
    out = f""" 
        <div class="item">
            <a href="{config[1]}" style='{config[3]}'>
            <h2>{config[0]}</h2>
            <p>{config[2]}</p>
            </a>
        </div>
    """
    return(out)


groups = os.listdir(f"{os.path.dirname(sys.argv[0])}/services")
html = ""
for i in groups:
    items = os.listdir(f"{os.path.dirname(sys.argv[0])}/services/{i}")
    html = html + f"""
    <h1>{i}</h1>
    <div class="group">
    """

    for a in items:

        temp = load(f"{os.path.dirname(sys.argv[0])}/services/{i}/{a}")
        html = html + prepare(temp)
    html = html + "</div>"

css = open(f"{os.path.dirname(sys.argv[0])}/template/temp.css")
html = f"""
<style>
{css.read()}
</style>
{html}
"""
f = open(f"{os.path.dirname(sys.argv[0])}/render/render.html","w")
f.write(html)

exec(load(f"{os.path.dirname(sys.argv[0])}/dash.py"))