from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Secure EHR System</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">

<div class="container py-5">
    <h1 class="mb-4 text-center text-primary">Secure EHR System</h1>
    
    <form method="POST" class="card p-4 shadow">
        <div class="mb-3">
            <label for="name" class="form-label">Patient Name</label>
            <input type="text" class="form-control" id="name" name="name" required>
        </div>
        
        <div class="mb-3">
            <label for="age" class="form-label">Age</label>
            <input type="number" class="form-control" id="age" name="age" required>
        </div>
        
        <div class="mb-3">
            <label for="symptoms" class="form-label">Symptoms</label>
            <textarea class="form-control" id="symptoms" name="symptoms" rows="3" required></textarea>
        </div>
        
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>

    {% if submitted %}
    <div class="alert alert-success mt-4" role="alert">
        <h4 class="alert-heading">Record Submitted</h4>
        <p><strong>Name:</strong> {{ name }}</p>
        <p><strong>Age:</strong> {{ age }}</p>
        <p><strong>Symptoms:</strong> {{ symptoms }}</p>
    </div>
    {% endif %}
</div>

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        symptoms = request.form.get('symptoms')
        return render_template_string(HTML_PAGE, submitted=True, name=name, age=age, symptoms=symptoms)
    return render_template_string(HTML_PAGE, submitted=False)

import os

if __name__ == '__main__':
    host = '127.0.0.1' if os.environ.get('FLASK_ENV') == 'development' else '0.0.0.0'
    app.run(host=host, port=5000)


