import os
import webbrowser

def host_portfolio():
    # Create a directory for the portfolio
    os.mkdir("portfolio")

    # Create a file for the portfolio's index page
    with open("portfolio/index.html", "w") as f:
        f.write("""
<!DOCTYPE html>
<html>
<head>
<title>Eshwar Desetty's Portfolio</title>
</head>
<body>
<h1>Eshwar Desetty</h1>
<p>Eshwar Desetty is a student pursuing Engineering in Cybersecurity. He is interested in ethical hacking and loves cars and mechanics of cars.</p>
<p>Here are some links to his work:</p>
<ul>
<li><a href="https://github.com/eshwardesetty/ethical-hacking">Ethical Hacking Projects</a></li>
<li><a href="https://www.linkedin.com/in/eshwardesetty/">LinkedIn Profile</a></li>
<li><a href="https://www.youtube.com/channel/UC--4--4--4--4">YouTube Channel</a></li>
</ul>
</body>
</html>
""")

    # Open the portfolio in a web browser
    webbrowser.open("portfolio/index.html")

if __name__ == "__main__":
    host_portfolio()
