from app import create_app

app = create_app()

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'veryfast299792458'
    app.debug = True
    app.run()