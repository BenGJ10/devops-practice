from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/health')
def health():
    return {
        "status": "UP",
        "message": "Application is running successfully"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cloud DevOps App</title>

    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family: Arial, sans-serif;
        }

        body{
            background:#f4f6f9;
            color:#333;
        }

        .navbar{
            background:#ffffff;
            padding:20px 60px;
            display:flex;
            justify-content:space-between;
            align-items:center;
            box-shadow:0 2px 10px rgba(0,0,0,0.08);
        }

        .logo{
            font-size:24px;
            font-weight:bold;
            color:#2563eb;
        }

        .hero{
            height:85vh;
            display:flex;
            flex-direction:column;
            justify-content:center;
            align-items:center;
            text-align:center;
            padding:20px;
        }

        .hero h1{
            font-size:52px;
            margin-bottom:20px;
            color:#111827;
        }

        .hero p{
            font-size:20px;
            color:#6b7280;
            max-width:700px;
            line-height:1.6;
        }

        .status-card{
            margin-top:40px;
            background:white;
            padding:25px 40px;
            border-radius:12px;
            box-shadow:0 4px 15px rgba(0,0,0,0.08);
        }

        .status{
            color:green;
            font-weight:bold;
            font-size:20px;
        }

        .footer{
            text-align:center;
            padding:20px;
            color:#777;
            background:white;
            border-top:1px solid #ddd;
        }

        .btn{
            margin-top:30px;
            padding:14px 28px;
            border:none;
            background:#2563eb;
            color:white;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
            transition:0.3s;
        }

        .btn:hover{
            background:#1e40af;
        }
    </style>
</head>

<body>

    <div class="navbar">
        <div class="logo">Cloud DevOps</div>
        <div>Flask + Jenkins CI/CD</div>
    </div>

    <div class="hero">
        <h1>Flask Application Deployed Successfully</h1>

        <p>
            This is a sample Flask application integrated with Jenkins
            for CI/CD pipeline demonstration and deployment automation.
        </p>

        <div class="status-card">
            <p class="status">Application Status: RUNNING</p>
        </div>

        <button class="btn" onclick="window.location.href='/health'">
            Check Health Endpoint
        </button>
    </div>

    <div class="footer">
        © 2026 Cloud DevOps Practical Project
    </div>

</body>
</html>
"""