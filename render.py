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
            <h3>{config[0]}</h3>
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
    <h2>{i}</h2>
    <div class="group">
    """

    for a in items:

        temp = load(f"{os.path.dirname(sys.argv[0])}/services/{i}/{a}")
        html = html + prepare(temp)
    html = html + "</div>"

css = open(f"{os.path.dirname(sys.argv[0])}/template/temp.css")
html = f"""
<h1> My ok ish dashboard </h1>
<style>
{css.read()}
</style>
{html}
"""
f = open(f"{os.path.dirname(sys.argv[0])}/render/render.html","w")
f.write(html)

port = 1111
try:
    exec(open(f"{os.path.dirname(sys.argv[0])}/run.py").read())
except OSError as error:
    if error.errno == 98:
        print(f"recompiled, another service or instance of this server is running on port {port}")
        print("if this server is running, it will have the current config")
    else:
        print(f"unexpected error: '{error}'")