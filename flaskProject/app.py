from flask import Flask,render_template,request,escape,jsonify
import vsearch
#调用数据库
import mysql.connector
app = Flask(__name__)


#viewlog.py
def log_request(req:'flask_request',res:'str'):
    with open('vsearch.log','a') as log:
        print(req.form,req.remote_addr,req.user_agent,res,file=log,sep='|')
# print(dir(str(req)),res,file=log,end='|')


# python 与数据库 操作
def log_req(req,res):
    """将用户信息（request和results）存入数据库"""
    # 1. 连接数据库
    dbconfig = {
        'host':'127.0.0.1',
        'user':'root',
        'password':'111111',
        'database':'userqq',
        'auth_plugin' : 'mysql_native_password'
    }
    # 2. 链接数据库 conn
    conn = mysql.connector.connect(**dbconfig)

    # 3. 创建一个游标 cursor
    cursor = conn.cursor()

    # 4. 用Python语言记录MySQL语言
    _SQL = """
            insert into log 
            (phrase,letters,ip,results)
            values
            (%s,%s,%s,%s)
    """

    # 5. 执行MySQL语言
    cursor.execute(_SQL,(req.form['phrase'],
                         req.form['letters'],
                         req.remote_addr,
                         # req.user_agent.browser,
                         res))

    # 6. 执行

    conn.commit()
    cursor.close()
    conn.close()


@app.route('/')

@app.route('/entry')
def entry_page():
    return render_template('entry.html',
                           the_title='这里🉑️查元音')

@app.route('/search4', methods=['POST'])
def do_search():
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = '这是你的结果🎫'
    results = str(vsearch.search4letters(phrase,letters))
    log_request(request,results)
    # return "hdjkahsdklsa"
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)

@app.route('/viewlog')
def viewTheLog():
    contents=[]
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles= ('表单数据🐔','👨用户IP','💻用户UA','🐛输出结果')
    return render_template('viewlog.html',
                           the_title= '日志汇总📝',
                           the_row_titles= titles,
                           the_data = contents,)


if __name__ == '__main__':
    app.run()
