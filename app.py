from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from password_manager import PasswordManager
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Required for flashing messages

# Initialize password manager
password_manager = PasswordManager()


@app.route("/")
def index():
    """Render main page with all passwords."""
    return render_template("index.html", sites=password_manager.passwords.items())


@app.route("/add", methods=["POST"])
def add_password():
    """Add a new password."""
    site = request.form.get("site", "").lower()
    password = request.form.get("password", "")
    generate = request.form.get("generate", False)

    if not site:
        flash("Site name is required", "error")
        return redirect(url_for("index"))

    if site in password_manager.passwords:
        flash("Site already exists", "error")
        return redirect(url_for("index"))

    if generate or not password:
        password = password_manager.generate_password()

    password_manager.passwords[site] = password
    password_manager._save_passwords(password_manager.passwords)
    flash(f"Password for {site} created successfully", "success")
    return redirect(url_for("index"))


@app.route("/update/<site>", methods=["POST"])
def update_password(site):
    """Update existing password."""
    site = site.lower()
    if site not in password_manager.passwords:
        flash("Site not found", "error")
        return redirect(url_for("index"))

    generate = request.form.get("generate", False)
    if generate:
        password = password_manager.generate_password()
    else:
        password = request.form.get("password", "")
        if not password:
            flash("Password is required", "error")
            return redirect(url_for("index"))

    password_manager.passwords[site] = password
    password_manager._save_passwords(password_manager.passwords)
    flash(f"Password for {site} updated successfully", "success")
    return redirect(url_for("index"))


@app.route("/generate")
def generate_password():
    """Generate a new password."""
    return jsonify({"password": password_manager.generate_password()})


if __name__ == "__main__":
    app.run(debug=True)
