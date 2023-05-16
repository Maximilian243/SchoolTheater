from pywebio_battery import *
from pywebio import *
from pywebio.session import eval_js, run_js

html = '''<input type="file" id="fileElem" multiple accept="image/*" onchange="handleFiles(this.files)">'''

js = '''if (fileElem) {
    fileElem.click();
  }
  e.preventDefault()'''

sock = """var xhr = new XMLHttpRequest();
xhr.open('POST', '/upload', true);
xhr.setRequestHeader('Content-Type', 'multipart/form-data');
xhr.onload = function() {
  if (xhr.status === 200) {
    console.log('Файл загружен!');
  } else {
    console.log('Произошла ошибка.');
  }
};
var formData = new FormData();
formData.append('file', file);
xhr.send(formData);"""


def application():
    def newfile():
        data = {}
        while len(data.keys()) == 0:
            data = eval_js('''document.getElementById('fileElem').files''')

    output.put_markdown('# ПАНЕЛЬ ДИСТАНЦИОННОГО УПРАВЛЕНИЯ')
    output.put_scrollable(output.put_scope('files'))
    output.put_scope('panel').style('bottom: 10px; margin-left:20px;')
    output.put_scope('panell')
    output.put_html(html)
    run_js("""document.getElementById('fileElem').style.display = 'none'""")
    output.put_button('Новые файлы', onclick=lambda: run_js(js))
    newfile()


start_server(application, host='192.168.137.1', port=80, debug=True)
