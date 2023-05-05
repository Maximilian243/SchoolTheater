from pywebio_battery import *
from pywebio import *
from pywebio.session import eval_js, run_js


html = '''<input type="file" id="fileElem" multiple accept="image/*" onchange="handleFiles(this.files)">'''

js = '''if (fileElem) {
    fileElem.click();
  }
  e.preventDefault()'''

def application():
    def newfile():
        output.clear('panell')
        print(input.file_upload('Выберите файлы', 'audio/*'))
    output.put_markdown('# ПАНЕЛЬ ДИСТАНЦИОННОГО УПРАВЛЕНИЯ')
    output.put_scrollable(output.put_scope('files'))
    output.put_scope('panel').style('bottom: 10px; margin-left:20px;')
    output.put_scope('panall')
    output.put_html(html)
    run_js("""document.getElementById('fileElem').style.display = 'none'""")
    output.put_button('Новые файлы', onclick=lambda: run_js(js))
    data = {}
    while len(data.keys()) == 0:
        data = eval_js('''document.getElementById('fileElem').files''')
    print(eval_js('''console.log(document.getElementById('fileElem').files)'''))
    print(data)
    output.toast(data)

    # output.put_text('Hello', scope='panel')


start_server(application, host='192.168.137.1', port=8, debug=True)
