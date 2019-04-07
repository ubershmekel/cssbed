import os


list_marker = '<!-- options -->'
snippet_marker = "<link rel='stylesheet' href='https://cdn.jsdelivr.net/gh/kognise/water.css@latest/dist/dark.css'>"
name_marker = 'CSS Bed'
snippet_fn = 'snippet.txt'
link_fn = 'link.txt'
reset_fn = 'reset.css'
index_fn = 'index.html'
source_marker = "https://github.com/ubershmekel/cssbed"

'''
<ul>
  <li><a href="/water.css/">Water.css</a></li>
</ul>
      '''

base = open(index_fn).read()

def fix_options(html):
  parts = html.split(list_marker)
  return parts[0] + list_marker + themes_list_html + list_marker + parts[2]


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
  html = fix_options(html)
  target = os.path.join(path, index_fn)
  open(target, 'w').write(html)

def get_themes():
  for fn in os.listdir('.'):
    if os.path.isdir(fn) and not fn.startswith('.'):
      yield fn

themes = sorted(list(get_themes()))

print(themes)
themes_list_html = '\n    <ul>\n'
for theme in themes:
  themes_list_html += '      <li><a href="/' + theme + '">' + theme + '</a>\n'
themes_list_html += '    </ul>\n'

print(themes_list_html)

for theme in themes:
  print("rendering " + theme)
  render(theme)

# Mainly render the root to update the theme list.
# Also, this is kind of recursive in a trippy way.
html = open(index_fn).read()
open(index_fn, 'w').write(fix_options(html))


