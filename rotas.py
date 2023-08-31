from flask import render_template, request, redirect

def rotas(app):
    @app.route('/')
    def index():
        return redirect('/home')
    
    @app.route('/home')
    def home():
        rotas = {'home':['home','/home'],
                 'sobre':['assignment','/sobre'],
                 'inscrição':['perm_contact_calendar','/inscricao'],
                 'aaaa':['question_answer','/aaaa']}
        img=['001','002','003']
        
        return render_template('index.html', rotas=rotas, img=img)
    
    @app.route('/cadastro',methods=['GET','POST'])
    def dacas():
        if request.method =='GET':
            return render_template('incrição.html')
        elif request.method =='POST':
            return 'POST'
        else:
            return "invalido"

    @app.route('/sobre')
    def sobre():
        return render_template('sobre.html')

