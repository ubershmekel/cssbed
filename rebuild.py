import os


list_marker = '<!-- options -->'
snippet_marker = "<link rel='stylesheet' href='https://cdn.jsdelivr.net/gh/kognise/water.css@latest/dist/dark.css'>"
name_marker = 'CSS Bed'
snippet_fn = 'snippet.txt'
link_fn = 'link.txt'
reset_fn = 'reset.css'
source_marker = "https://github.com/ubershmekel/cssbed"

'''
<ul>
  <li><a href="/water.css/">Water.css</a></li>
</ul>
      '''

base = open('index.html').read()

def render(path):
  print("path " + path)
  html = base
  snippet_path = os.path.join(path, snippet_fn)
  link_path = os.path.join(path, link_fn)
  #reset_path = os.path.join(path, reset_fn)
  if os.path.exists(snippet_path):
    snippet = open(snippet_path).read()
    html = html.replace(snippet_marker, snippet)
  link = open(link_path).read()
  html = html.replace(source_marker, link)
  html = html.replace(name_marker, path)
  parts = html.split(list_marker)
  html = parts[0] + themes_list_html + parts[2]
  target = os.path.join(path, 'index.html')
  open(target, 'w').write(html)

def get_themes():
  for fn in os.listdir('.'):
    if os.path.isdir(fn) and not fn.startswith('.'):
      yield fn

themes = sorted(list(get_themes()))

print(themes)
themes_list_html = '<ul>\n'
for theme in themes:
  themes_list_html += '<li><a href="/' + theme + '">' + theme + '</a>\n'
themes_list_html += '</ul>'

print(themes_list_html)

for theme in themes:
  print("rendering " + theme)
  render(theme)
