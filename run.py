from flaskapp import create_app

if __name__ == "__main__":
    print("Running....")
    app = create_app()
    app.run(debug=True, host="0.0.0.0")
