from pywebio_battery import *
from pywebio import *


def application():
    def newfile():
        output.clear('panell')
        input.file_upload('Выберите файлы', 'audio/*')
    output.put_markdown('# ПАНЕЛЬ ДИСТАНЦИОННОГО УПРАВЛЕНИЯ')
    output.put_scrollable(output.put_scope('files'))
    output.put_scope('panel').style('bottom: 10px; margin-left:20px;')
    output.put_scope('panall')
    output.put_button('Новые файлы', onclick=newfile, scope='panell')

    # output.put_text('Hello', scope='panel')


start_server(application, host='192.168.137.1', port=8, debug=True)
