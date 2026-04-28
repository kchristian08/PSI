from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route("/")
def index():
    cor = request.cookies.get("cor")
    
    if not cor:
        cor = "#ffffff"  # padrão
    
    return render_template("index.html", cor=cor)

@app.route("/definir_cor", methods=["POST"])
def definir_cor():
    cor = request.form.get("cor")

    print("COR RECEBIDA:", cor)  # DEBUG
    
    response = make_response(redirect("/"))
    response.set_cookie("cor", cor, max_age=60*60*24*30)

    return response

if __name__ == "__main__":
    app.run(debug=True)