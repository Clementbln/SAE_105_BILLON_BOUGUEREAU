def generate_html_file(file_name, title, column_titles, data_rows):
    #Contenu HTML
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <link rel="stylesheet" type="text/css" href="global.css" />
    </head>
    <body>
        <h1>{title}</h1>
        <table>
            <tr>
                {''.join(f'<th>{col}</th>' for col in column_titles)}
            </tr>
            {''.join(f'<tr>{"".join(f"<td>{data}</td>" for data in row)}</tr>' for row in data_rows)}
        </table>
    </body>
    </html>
