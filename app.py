from flask import Flask, jsonify
from views import views
app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

#safe route to catch
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'error': "page not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port= 5000)
     