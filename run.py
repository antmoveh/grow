from application import app


if __name__ == "__main__":
    # app.run(port=8001, debug=True)
    app.run(host="0.0.0.0", port=8008, debug=True)