from flask import Flask, render_template, request, send_file, redirect
import os
import subprocess
from pokergpt import askQuestion
from pokergpt import cleanPlayerStats
from csvAnalyzer import generatePlayerStats
player_data = {}

app = Flask(__name__)

def formatTwoDec(player_data):
    formatted_data = {}
    for player, stats in player_data.items():
        formatted_stats = {}
        for key, value in stats.items():
            if isinstance(value, (int, float)):
                formatted_stats[key] = round(value, 2)
            else:
                formatted_stats[key] = value
        formatted_data[player] = formatted_stats
    return formatted_data


@app.route('/', methods=['GET', 'POST'])
def index():
    global globalData
    if 'reset' in request.args:
       
        globalData = None  
        return redirect('/')
    if request.method == 'POST':
        
        if 'reset' in request.form:
            globalData = None  
        else:
            uploaded_file = request.files['file']
            if uploaded_file.filename.endswith('.csv'):
                new_file_name = "importantpokernow.csv"
                new_file_path = os.path.join(
                    os.path.dirname(__file__), new_file_name)
                uploaded_file.save(new_file_path)
                subprocess.run(['python', 'graphs.py'], check=True)
                globalData = generatePlayerStats() # problem is here. Calling on no file
                player_data = formatTwoDec(globalData)
                print(player_data)
                return render_template('success.html', player_data=player_data)
            else:
                message="Upload your pokernow.csv file!"
                return render_template('index.html', message=message)
    return render_template('index.html')


@ app.route('/view_pdf')
def view_pdf():
  
    pdf_path=os.path.join(os.path.dirname(__file__), 'player_statistics.pdf')
    return send_file(pdf_path, as_attachment=False)

@app.route('/ask_question', methods=['POST'])
def ask_question():
    user_question = request.form['question']
    response = askQuestion(user_question)  # Call your function here
    return response

@app.route('/generate_strategy', methods=['POST'])
def generate_strategy():
    player_name = str(request.form['player_name']).strip()
    player_data = formatTwoDec(globalData)
    cleanedData = cleanPlayerStats(player_data[player_name], player_name)
    return cleanedData



if __name__ == '__main__':
     app.run(debug=True)
