import wikipedia
from flask import Flask, request, render_template

# wikipedia.set_lang("fr")

app = Flask(__name__)


@app.route('/')
def index():
    if request.args.get('q'):
        l = []
        for page in wikipedia.search(request.args.get('q')):
            print(page)
            search =  wikipedia.page(page)
            l.append({
                'title': search.title,
                'url': search.url,
                'summary': search.summary,
            })
            
        data = {'search': l}
        return data
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)