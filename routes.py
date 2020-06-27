from start_me_from_here import app, get_session
from models import Meetup, User, Town, Post
from flask import render_template, redirect, url_for, request, session, flash


@app.route('/')
@app.route('/index/')
def index():
    return 'to jest index'

@app.route('/meetup')
@app.route('/meetup/')
def meetup():
    conn = get_session()

    meetup_id = request.args.get('meetup')

    if meetup_id:
        meetup_id = int(meetup_id)
        event_details = conn.query(Meetup).filter(Meetup.meetup_id == meetup_id).one()
        if len(event_details.comments_list):
            comments = [event_comment.dict_format() for event_comment in event_details.comments_list]
        return render_template('event.html', event_details=event_details.dict_format(), comments=comments)

    return render_template('event.html')


@app.route('/add_meetup', methods=['GET', 'POST'])
@app.route('/add_meetup/', methods=['GET', 'POST'])
def add_meetup():
    conn = get_session()
    # user = conn.query(User).filter(User.id == session['user_id']).one()

    if request.method == 'POST':
        # HARDCODED USER
        user_id = 1
        title = request.form['title'].strip()
        date = request.form['date'].strip()
        location = request.form['location'].strip()
        description = request.form['description'].strip()
        activity_people = request.form['people'].strip()
        activity_animals = request.form['animals'].strip()
        activity_ecology = request.form['ecology'].strip()

        location_object = conn.query(Town).filter(Town.name == location).one()

        if activity_people == 'True':
            activity_people = True
        else:
            activity_people = None

        if activity_animals == 'True':
            activity_animals = True
        else:
            activity_animals = None

        if activity_ecology == 'True':
            activity_ecology = True
        else:
            activity_ecology = None


        new_event = Meetup(user_id=user_id, title=title, date=date,
                           location=location_object.town_id,
                           description=description,
                           activity_people=activity_people,
                           activity_animals=activity_animals,
                           activity_ecology=activity_ecology)

        conn.add(new_event)
        conn.commit()
        conn.close()
    elif request.method == 'GET':
        return render_template('add_meetup.html')


    return render_template('add_meetup.html')


@app.route('/add_post', methods=['GET', 'POST'])
@app.route('/add_post/', methods=['GET', 'POST'])
def add_comment():
    conn = get_session()

    if request.method == 'POST':
        title = request.form['title'].strip()
        username = request.form['username'].strip()
        date = request.form['date'].strip()
        content = request.form['content'].strip()

        new_comment = Post(username=username, title=title, date=date, content=content)

        conn.add(new_comment)
        conn.commit()
        conn.close()

        return redirect(url_for('event'))
    elif request.method == 'GET':

        return render_template('add_post.html')

    return redirect(url_for('event'))
