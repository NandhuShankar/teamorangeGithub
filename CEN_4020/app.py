from flask import Flask, request, redirect, render_template, flash, url_for, session
import json
import os
import re
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

USERS_FILE = 'users.json'
JOBS_FILE = 'jobs.json'

@app.route('/general')
def general():
    return render_template('general.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/accessibility')
def accessibility():
    return render_template('accessibility.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')
@app.route('/brand_policy')
def brand_policy():
    return render_template('brand_policy.html')

@app.route('/browse-incollege')
def browse_incollege():
    return render_template('browse-incollege.html')

@app.route('/business-solutions')
def business_solutions():
    return render_template('business-solutions.html')

@app.route('/career')
def career():
    return render_template('career.html')

@app.route('/cookie_policy')
def cookie_policy():
    return render_template('cookie_policy.html')

@app.route('/copyright_notice')
def copyright_notice():
    return render_template('copyright_notice.html')

@app.route('/copyright_policy')
def copyright_policy():
    return render_template('copyright_policy.html')

@app.route('/developer')
def developer():
    return render_template('developer.html')

@app.route('/directories')
def directory():
    return render_template('directories.html')

@app.route('/guest_control')
def guest_control():
    return render_template('guest_control.html')

@app.route('/language')
def language():
    return render_template('language.html')

@app.route('/press')
def press():
    return render_template('press.html')

@app.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')

@app.route('/user_agreement')
def user_agreement():
    return render_template('user_agreement.html')

def read_jobs_from_json():
    if not os.path.exists(JOBS_FILE):
        return []
    with open(JOBS_FILE, 'r') as file:
        return json.load(file)

def write_jobs_to_json(jobs):
    with open(JOBS_FILE, 'w') as file:
        json.dump(jobs, file, indent=4)
def read_users_from_json():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, 'r') as file:
        return json.load(file)

def write_users_to_json(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=4)

def find_user_by_username(username):
    users = read_users_from_json()
    for user in users:
        if user['username'] == username:
            return user
    return 
def add_friend_request(sender_username, receiver_username):
    students = read_users_from_json()  # Load the current list of users

    # Find sender and receiver in the list
    sender = next((student for student in students if student['username'] == sender_username), None)
    receiver = next((student for student in students if student['username'] == receiver_username), None)

    if sender and receiver:
        # Update the receiver's pendingFriendRequests list
        if 'pendingFriendRequests' not in receiver:
            receiver['pendingFriendRequests'] = []
        if sender_username not in receiver['pendingFriendRequests']:
            receiver['pendingFriendRequests'].append(sender_username)
        
        # Update the sender's sentFriendRequests list
        if 'sentFriendRequests' not in sender:
            sender['sentFriendRequests'] = []
        if receiver_username not in sender['sentFriendRequests']:
            sender['sentFriendRequests'].append(receiver_username)

        # Save the updated data back to the JSON file
        write_users_to_json(students)
@app.route('/accept-friend-request', methods=['POST'])
def accept_friend_request():
    from_username = request.form['from_username']
    to_username = request.form['to_username']

    users = read_users_from_json()  # Assume this function reads your JSON data
    
    # Finding the sender and receiver in the users list
    from_user = next((user for user in users if user['username'] == from_username), None)
    to_user = next((user for user in users if user['username'] == to_username), None)
    
    if from_user and to_user:
        # Update the receiver's data
        if 'pendingFriendRequests' in to_user and from_username in to_user['pendingFriendRequests']:
            to_user['pendingFriendRequests'].remove(from_username)
        
        if 'friends' not in to_user:
            to_user['friends'] = []
        to_user['friends'].append(from_username)

        # Update the sender's data
        if 'sentFriendRequests' in from_user and to_username in from_user['sentFriendRequests']:
            from_user['sentFriendRequests'].remove(to_username)
        
        if 'friends' not in from_user:
            from_user['friends'] = []
        from_user['friends'].append(to_username)

        # Save the updated users back to JSON
        write_users_to_json(users)
        
        flash('Friend request accepted!', 'success')
    else:
        flash('An error occurred.', 'error')
    
    return redirect(url_for('user_page', username=to_username))
@app.route('/user/<username>')
def user_page(username):
    users = read_users_from_json()  # Load users from your JSON file
    user = next((u for u in users if u['username'] == username), None)
    pending_friend_requests = []

    if user:
        # Get the list of usernames who have sent a friend request to this user
        pending_friend_requests = user.get('pendingFriendRequests', [])
    
    return render_template('user_page.html', username=username, pending_friend_requests=pending_friend_requests)

@app.route('/profile/<username>')
def profile(username):
    users = read_users_from_json()
    current_user_profile = next((u for u in users if u['username'] == username), None)
    if current_user_profile:
        return render_template('profile.html', **current_user_profile)
    return 'User not found', 404

@app.route('/edit_profile_form', methods=['GET', 'POST'])
def edit_profile_form():
    username = session.get('username')
    # if not username:
        # return redirect(url_for('index'))
    users = read_users_from_json()
    user = next((u for u in users if u['username'] == username), None)
    user_index = users.index(user)  # Get the index of the user
    # if input is not empty
    if request.method == 'POST':
        user['profile_made'] = True
        if request.form['first_name']:
            user['first_name'] = request.form['first_name']
        if request.form['last_name']:
            user['last_name'] = request.form['last_name']
        if request.form['major']:
            user['major'] = request.form['major']
        if request.form['university']:
            user['university'] = request.form['university']
        if request.form['description']:
            user['description'] = request.form['description']
        if request.form['education']:
            user['education'] = request.form['education']

        # experience section
        if request.form['experience_title']:
            user['experience']['title'] = request.form['experience_title']
        if request.form['experience_employer']:
            user['experience']['employer'] = request.form['experience_employer']
        if request.form['experience_location']:
            user['experience']['location'] = request.form['experience_location']
        if request.form['experience_start_date']:
            user['experience']['start_date'] = request.form['experience_start_date']
        if request.form['experience_end_date']:
            user['experience']['end_date'] = request.form['experience_end_date']
        if request.form['experience_description']:
            user['experience']['description'] = request.form['experience_description']
        users[user_index] = user  # Replace the old user data with the updated user data
        with open('users.json', 'w') as f:  # Open the JSON file in write mode
            json.dump(users, f, indent=4)  # Write the updated data back to the JSON file
        # user['education'] = request.form['education']
        # write_users_to_json(users)
        # flash('Profile updated successfully!', 'success')
        # return redirect(url_for('user_page', username=username))
    return render_template('edit_profile_form.html', **user)

@app.route('/find', methods=['GET', 'POST'])
def find():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        users = read_users_from_json()
        for user in users:
            if user['first_name'] == firstname and user['last_name'] == lastname:
                return render_template('find.html', message="They are a part of the InCollege system.")
        return render_template('find.html', message="They are not yet a part of the InCollege system yet.")
    return render_template('find.html')

@app.route('/learn')
def learn():
    username = session.get('username')
    if not username:
        return redirect(url_for('index'))
    return render_template('learn.html', username=username)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        # Collect job details from the form
        job = {
            "title": request.form['title'],
            "description": request.form['description'],
            "employer": request.form['employer'],
            "location": request.form['location'],
            "salary": request.form['salary'],
            "poster": session.get('username')  # Assumes username is stored in session
        }
        # Read current jobs, add the new job, and write back to the JSON file
        jobs = read_jobs_from_json()
        jobs.append(job)
        write_jobs_to_json(jobs)
        flash('Job posted successfully!', 'success')
        return redirect('/search')  # Prevents form re-submission on refresh
    return render_template('search.html')
@app.route('/logout')
def logout():
    session.pop('username', None)
    session.clear()
    return redirect(url_for('index'))
@app.route('/search-students' , methods=['GET', 'POST'])
def search_students():
    search_results = None
    not_found_message = None
    if request.method == 'POST':
        search_term = request.form['search_term'].lower()
        students = read_users_from_json()  # Assume this function reads your JSON data into a Python list
        # Filter students based on the search term
        search_results = [student for student in students if search_term in student.get('last_name', '').lower() or 
                  search_term in student.get('university', '').lower() or search_term in student.get('major', '').lower()]
        if not search_results:
            not_found_message = 'No students found matching the search term'

    return render_template('search-students.html', search_results=search_results, not_found_message=not_found_message)

@app.route('/send-friend-request', methods=['POST'])
def send_friend_request():
    receiver_username = request.form['username']
    sender_username = session.get('username')  # Assuming the current user's username is stored in the session
    
    # Assume you have a function that updates the JSON data with the friend request
    add_friend_request(sender_username, receiver_username)
    
    flash('Friend request sent successfully!')
    return redirect('/search-students')
@app.route('/show-my-network/<username>')
def show_my_network(username):
    users = read_users_from_json()
    user = next((u for u in users if u['username'] == username), None)
    if user:
        friends = user.get('friends', [])
    else:
        friends = []

    return render_template('show_my_network.html', username=username, friends=friends)
@app.route('/disconnect-friend', methods=['POST'])
def disconnect_friend():
    friend_username = request.form['friend_username']
    username = request.form['username']

    users = read_users_from_json()

    # Find the users in the JSON data
    user = next((u for u in users if u['username'] == username), None)
    friend = next((u for u in users if u['username'] == friend_username), None)

    if user and friend:
        # Remove each user from the other's friends list
        if friend_username in user.get('friends', []):
            user['friends'].remove(friend_username)
        if username in friend.get('friends', []):
            friend['friends'].remove(username)

        # Save the updated users back to JSON
        write_users_to_json(users)

        flash('Successfully disconnected from ' + friend_username, 'success')
    else:
        flash('An error occurred.', 'error')

    # Redirect back to the Show My Network page
    return redirect(url_for('show_my_network', username=username))
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'signup' in request.form:
            username = request.form['username']
            password = request.form['password']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            users = read_users_from_json()
            if not find_user_by_username(username):
                users.append({
                "username": username,
                "password": password,  # Consider hashing this password
                "first_name": first_name,
                "last_name": last_name,
                "profile_made": False,
                "major": "",
                "university": "",
                "description": "",
                "experience":
                {
                    "title": "",
                    "employer": "",
                    "location": "",
                    "start_date": "",
                    "end_date": "",
                    "description": ""
                },
                "education": "",
                })

                write_users_to_json(users)
                flash('Signup successful! Please login.', 'success')
            else:
                flash('Username already exists!', 'error')
        elif 'login' in request.form:
            username = request.form['username']
            password = request.form['password']
            user = find_user_by_username(username)
            if user and user['password'] == password:
                session['username'] = username  # Store username in session
                return redirect(url_for('user_page', username=username))
            else:
                flash('Incorrect username or password!', 'error')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)