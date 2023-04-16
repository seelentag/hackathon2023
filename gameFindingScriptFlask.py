from flask import Flask, request, render_template
import gameFindingScriptHelperFunctions as gf

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/sort_users', methods=['POST'])
# def upload_file():
#     file = request.files['inputFile']
#     filename = file.filename
#     file.save(filename)
#     result = sort_users_into_groups(filename)
#     return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort_users', methods=['POST'])
def sort_users():
    # Check if a file was uploaded
    if 'csv_file' not in request.files:
        return 'No file was uploaded.'

    # Get the file from the request
    csv_file = request.files.get('csv_file')

    # Check if the file is not empty
    if csv_file.filename == '':
        return 'The uploaded file is empty.'

    # Check if the file is a CSV file
    if not csv_file.filename.endswith('.csv'):
        return 'The uploaded file is not a CSV file.'

    # Save the file to disk
    filename = 'uploaded_file.csv'
    csv_file.save(filename)

    # Sort users into groups
    groups = sort_users_into_groups(filename)

    # Return the groups as a response
    return '<pre>' + groups + '</pre>' + '<a href="/">Back to login</a>'

def sort_users_into_groups(filename):
    # Poking through initial CSV file and cleaning the data for our purposes
    cleanedData = gf.open_file_and_clean_data(filename)

    # Creating a dictionary of people with inner lists of available times and other preferences
    users_under_18 = []
    users_over_18_under_30 = []
    users_over_30_under_60 = []
    users_over_60 = []

    for i in range(len(cleanedData)):
        if cleanedData[i] == "Yes":
            username = cleanedData[i+1]
            age = int(cleanedData[i+2])
            day = cleanedData[i+3]
            time = cleanedData[i+4]
            time = (day + " " + gf.get_hour_minute(time))

            if age < 18:
                users_under_18.append(gf.user(username, time, age))
            elif age >= 18 and age < 30:
                users_over_18_under_30.append(gf.user(username, time, age))
            elif age >= 30 and age < 60:
                users_over_30_under_60.append(gf.user(username, time, age))
            else:
                users_over_60.append(gf.user(username, time, age))

    # Matching people based on their available times
    time_groups_under_18 = gf.sort_users(users_under_18)
    time_groups_under_30 = gf.sort_users(users_over_18_under_30)
    time_groups_under_60 = gf.sort_users(users_over_30_under_60)
    time_groups_over_60 = gf.sort_users(users_over_60)

    # Outputting a txt file with grouped users
    groups_under_18 = gf.create_group_string(time_groups_under_18)
    groups_under_30 = gf.create_group_string(time_groups_under_30)
    groups_under_60 = gf.create_group_string(time_groups_under_60)
    groups_over_60 = gf.create_group_string(time_groups_over_60)

    groups = gf.concatenate_age_groups(groups_under_18, groups_under_30, groups_under_60, groups_over_60)

    return str(groups)

if __name__ == '__main__':
    app.run(debug=True)
