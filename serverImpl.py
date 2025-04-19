import hashlib
import time
from flask import Flask, request, session
import domain
import server

app = Flask(__name__, template_folder='domain', static_folder='domain/static')
app.secret_key = 'your_secret_key'
app.debug = True

@app.before_request
def before_request():
    if 'user_id' not in session:
        ip = request.remote_addr
        current_time = time.time()
        user_id = hashlib.md5(f'{ip}{current_time}'.encode()).hexdigest()
        session['user_id'] = user_id

@app.route("/")
def root():
    return domain.root.display()


@app.route("/inventory", methods=["GET"])
def inventory():
    steamid = request.args.get('steamid') or None
    return domain.inventory.display(steamid)

@app.route("/inventory/add", methods=['POST'])
def inv_add():
    item_name = request.form["name"]
    quantity = request.form["quantity"]
    item_type = request.form["type"]
    steamid = request.form["steamid"]
    return domain.inventory.add(steamid, item_name, item_type, quantity)

@app.route("/inventory/update", methods=['POST'])
def inv_update():
    steamid = request.form["steamid"] or None
    try:
        json = request.form["json"]
    except KeyError:
        json = None
    return domain.inventory.update(steamid, json, request.headers, request.cookies)

@app.route("/inventory/alter", methods=["POST"])
def inv_alter():
    steamid = request.form["steamid"]
    item = request.form["item"]
    quantity = request.form["quantity"]
    return domain.inventory.alter(steamid, item, quantity)

@app.route("/prices")
def prices():
    return domain.prices.display()

@app.route("/prices/update")
def prices_update():
    print(request.cookies.get('Device-Id'), request.headers)
    return domain.prices.update(request.cookies, request.headers)


@app.route("/database")
def database():
    return domain.database.display()

if __name__ == '__main__':
    server.__init__()
    app.run(use_reloader=True)

