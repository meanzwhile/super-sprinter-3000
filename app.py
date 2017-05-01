from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/story", methods=["GET"])
def story():
    return render_template("form.html")


@app.route("/new_story", methods=["POST"])
def post_story():
    story_title = request.form["story_title"]
    user_story = request.form["user_story"]
    acceptance_criteria = request.form["acceptance_criteria"]
    business_value = request.form["business_value"]
    estimation = request.form["estimation"]
    status_list = request.form["status_list"]

    ID_Counter = 0
    with open("database.csv", "r") as file:
        lines = file.readlines()
        for element in lines:
            ID_Counter += 1
    table = [str(ID_Counter), story_title, user_story, acceptance_criteria, business_value, estimation, status_list]

    with open("database.csv", "a") as file:
        for elem in table:
            file.write(elem + ";")
        file.write("\n")
    return render_template("form.html")


@app.route("/story/<story_id>")
def story_id(story_id):
    with open("database.csv", "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    for i in range(len(table)):
        if table[i][0] == story_id:
            story_title = table[i][1]
            user_story = table[i][2]
            acceptance_criteria = table[i][3]
            business_value = table[i][4]
            estimation = table[i][5]
            status_list = table[i][6]
            print(story_title)
    return render_template("form.html",
                           story_id=story_id,
                           story_title=story_title,
                           user_story=user_story,
                           acceptance_criteria=acceptance_criteria,
                           business_value=business_value,
                           estimation=estimation,
                           status_list=status_list)


@app.route("/list")
@app.route("/")
def main():
    with open("database.csv", "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return render_template("list.html", table=table)


if __name__ == '__main__':
    app.run()
