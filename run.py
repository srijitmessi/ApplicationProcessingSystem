from app import app, config
app.run(debug=config.debug, host=config.host_path, port= config.port)
