from flask import render_template, request, redirect ,abort


# nome_da_rota    google_ico    caminho 
rotas = {'home':['home','/home'],
            'sobre':['assignment','/sobre'],
            'inscrição':['perm_contact_calendar','/inscricao'],
            'aaaa':['question_answer','/aaaa']}

img=['001.jpeg','002.jpg','003.jpg','004.png']


def pages(app):
    @app.route('/')
    def index():
        return redirect('/home')
    
    @app.route('/<rota>' , methods=['get','post'])
    def home(rota):
        if request.method =='POST':
            frame=f'''<h2>inscrição aceita</2> <br>
            {request.form}
'''
        elif rota=='home':
            frame=render_template('frameindex.html')
        elif rota=='inscricao':
            frame=render_template('frameinscricao.html')
        elif rota =='sobre':
            frame = render_template('framesobre.html') 
        else:
            return abort(404)
        return render_template('index.html', rotas=rotas, img=img, frame=frame)

