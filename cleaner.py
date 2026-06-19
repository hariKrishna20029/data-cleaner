from flask import Flask, render_template, request, send_file
import pandas as pd 
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template("space.html")

@app.route('/upload', methods = ['POST'])
def upload():
        file = request.files['file']

        if file.filename.endswith('.csv'):
              df = pd.read_csv(file)
        else:
              df = pd.read_excel(file)

        rows_before = len(df)

        #remove duplicates
        df = df.drop_duplicates()

        #fill missing values
        df = df.fillna("N/A")
        rows_after = len(df)
        df.to_csv("cleaned_data.csv", index=False)

        stats = df.describe(include= 'all').to_html()

        table = df.head(20).to_html()

        return render_template(
              'space.html',
              table = table,
             stats = stats,
             rows_before= rows_before,
             rows_after= rows_after,
        )

@app.route('/download')
def download():
       return send_file("cleaned_data.csv", 
                        as_attachment=True
                        )

    

     

if __name__ == "__main__":
        app.run(debug = True)
