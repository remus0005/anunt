# Script Python pentru a genera un fișier HTML cu design modern
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pagina Modernă</title>
    <style>
        /* Global Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }
        body {
            background-color: #f0f0f0;
            color: #333;
            line-height: 1.6;
            padding: 20px;
        }

        h1 {
            font-size: 3rem;
            text-align: center;
            color: #4CAF50;
            margin-bottom: 20px;
        }

        .container {
            width: 80%;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }

        button {
            background-color: #4CAF50;
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 5px;
            font-size: 1.2rem;
            cursor: pointer;
            transition: background-color 0.3s ease;
            margin-top: 20px;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }

        button:hover {
            background-color: #45a049;
        }

        /* Footer Styles */
        footer {
            text-align: center;
            margin-top: 40px;
            color: #666;
        }

        footer a {
            color: #4CAF50;
            text-decoration: none;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            h1 {
                font-size: 2.5rem;
            }
            .container {
                width: 95%;
            }
            button {
                width: 100%;
            }
        }
    </style>
</head>
<body>

    <h1>Pagina Modernă cu Python!</h1>
    <div class="container">
        <p>Bun venit pe această pagină creată cu ajutorul unui script Python. Puteți să personalizați designul și să adăugați mai multe funcționalități!</p>
        <button onclick="alert('Salut! Acesta este un mesaj JavaScript.')">Click pentru un mesaj!</button>
    </div>

    <footer>
        <p>Creat de <a href="https://www.exemplu.com" target="_blank">Exemplu</a></p>
    </footer>

</body>
</html>
"""

# Creăm fișierul HTML
with open("pagina_modernă.html", "w") as file:
    file.write(html_content)

print("Fișierul HTML a fost generat cu succes: pagina_modernă.html")
