from app import app as application

# travis test
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8080, debug=False)