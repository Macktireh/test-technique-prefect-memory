import wikipedia
from flask import Flask, request, render_template

# wikipedia.set_lang("fr")

app = Flask(__name__)

    
@app.route('/')
def index():
    if request.args.get('q'):
        l = []
        for page in wikipedia.search(request.args.get('q')):
            try:
                search =  wikipedia.page(page)
                l.append({
                    'title': search.title,
                    'url': search.url,
                    'summary': search.summary,
                })
            except:
                pass
        data = {'search': l}
        return data
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)