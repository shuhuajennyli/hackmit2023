from website import create_app
from flask import Blueprint, render_template, request, jsonify

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)