# from flask import Flask, render_template
# from api import api_bp


# app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
# app.register_blueprint(api_bp)

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def index(path):
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run()

from flask import Flask, abort, request
import whisper
from tempfile import NamedTemporaryFile

# Load the Whisper model:
model = whisper.load_model('base')

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handler():
    if not request.files:
        # If the user didn't submit any files, return a 400 (Bad Request) error.
        abort(400)

    # For each file, let's store the results in a list of dictionaries.
    results = []

    # Loop over every file that the user submitted.
    for filename, handle in request.files.items():
        # Create a temporary file.
        # The location of the temporary file is available in `temp.name`.
        temp = NamedTemporaryFile()
        # Write the user's uploaded file to the temporary file.
        # The file will get deleted when it drops out of scope.
        handle.save(temp)
        # Let's get the transcript of the temporary file.
        result = model.transcribe(temp.name)
        # Now we can store the result object for this file.
        results.append({
            'filename': filename,
            'transcript': result['text'],
        })

    # This will be automatically converted to JSON.
    return {'results': results}