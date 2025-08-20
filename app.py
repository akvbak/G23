from flask import Flask, render_template, request, redirect, url_for, flash
from models import Organization, init_db
import re

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change for production

init_db()

EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'

@app.route('/')
def home():
    orgs = Organization.all()
    return render_template('index.html', organizations=orgs)

@app.route('/organizations/<int:org_id>')
def details(org_id):
    org = Organization.get(org_id)
    if not org:
        flash('Organization not found.', 'danger')
        return redirect(url_for('home'))
    return render_template('details.html', org=org)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        type_ = request.form.get('type')
        if type_ == 'custom':
            custom_type = request.form.get('customType')
            type_ = custom_type
        location = request.form.get('location')
        yearFounded = request.form.get('yearFounded')
        contactEmail = request.form.get('contactEmail')
        errors = []
        if not name:
            errors.append('Name is required.')
        if not type_:
            errors.append('Type is required.')
        elif type_ == 'custom' or type_ == '':
            errors.append('Please enter a valid organization type.')
        if not contactEmail or not re.match(EMAIL_REGEX, contactEmail):
            errors.append('Valid email is required.')
        if errors:
            for e in errors:
                flash(e, 'danger')
            return render_template('create.html')
        Organization.create({
            'name': name,
            'type': type_,
            'location': location,
            'yearFounded': yearFounded,
            'contactEmail': contactEmail
        })
        flash('Organization created!', 'success')
        return redirect(url_for('home'))
    return render_template('create.html')

@app.route('/edit/<int:org_id>', methods=['GET', 'POST'])
def edit(org_id):
    org = Organization.get(org_id)
    if not org:
        flash('Organization not found.', 'danger')
        return redirect(url_for('home'))
    if request.method == 'POST':
        name = request.form.get('name')
        type_ = request.form.get('type')
        if type_ == 'custom':
            custom_type = request.form.get('customType')
            type_ = custom_type
        location = request.form.get('location')
        yearFounded = request.form.get('yearFounded')
        contactEmail = request.form.get('contactEmail')
        errors = []
        if not name:
            errors.append('Name is required.')
        if not type_:
            errors.append('Type is required.')
        elif type_ == 'custom' or type_ == '':
            errors.append('Please enter a valid organization type.')
        if not contactEmail or not re.match(EMAIL_REGEX, contactEmail):
            errors.append('Valid email is required.')
        if errors:
            for e in errors:
                flash(e, 'danger')
            return render_template('edit.html', org=org)
        Organization.update(org_id, {
            'name': name,
            'type': type_,
            'location': location,
            'yearFounded': yearFounded,
            'contactEmail': contactEmail
        })
        flash('Organization updated!', 'success')
        return redirect(url_for('details', org_id=org_id))
    return render_template('edit.html', org=org)

@app.route('/delete/<int:org_id>', methods=['POST'])
def delete(org_id):
    org = Organization.get(org_id)
    if not org:
        flash('Organization not found.', 'danger')
    else:
        Organization.delete(org_id)
        flash('Organization deleted.', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
