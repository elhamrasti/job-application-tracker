
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect("applications.db")
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/")
def home():
    connection = get_db_connection()

    applications = connection.execute(
        "SELECT * FROM applications ORDER BY id DESC"
    ).fetchall()

    total = len(applications)

    interviews = connection.execute(
        "SELECT COUNT(*) FROM applications WHERE status = ?",
        ("Interview",)
    ).fetchone()[0]

    offers = connection.execute(
        "SELECT COUNT(*) FROM applications WHERE status = ?",
        ("Offer",)
    ).fetchone()[0]

    rejected = connection.execute(
        "SELECT COUNT(*) FROM applications WHERE status = ?",
        ("Rejected",)
    ).fetchone()[0]

    connection.close()

    return render_template(
        "index.html",
        applications=applications,
        total=total,
        interviews=interviews,
        offers=offers,
        rejected=rejected
    )


@app.route("/add", methods=["GET", "POST"])
def add_application():

    if request.method == "POST":

        company = request.form["company"].strip()
        job_title = request.form["job_title"].strip()
        application_date = request.form["application_date"]
        status = request.form["status"]
        notes = request.form["notes"].strip()

        if not company or not job_title or not application_date:
            return "Company, job title and date are required.", 400

        allowed_statuses = ["Applied", "Interview", "Rejected", "Offer"]

        if status not in allowed_statuses:
            return "Invalid application status.", 400

        connection = get_db_connection()

        connection.execute(
            """
            INSERT INTO applications
            (company, job_title, application_date, status, notes)
            VALUES (?, ?, ?, ?, ?)
            """,
            (company, job_title, application_date, status, notes)
        )

        connection.commit()
        connection.close()

        return redirect(url_for("home"))

    return render_template("add_application.html")


@app.route("/edit/<int:application_id>", methods=["GET", "POST"])
def edit_application(application_id):

    connection = get_db_connection()

    application = connection.execute(
        "SELECT * FROM applications WHERE id = ?",
        (application_id,)
    ).fetchone()

    if application is None:
        connection.close()
        abort(404)

    if request.method == "POST":

        company = request.form["company"].strip()
        job_title = request.form["job_title"].strip()
        application_date = request.form["application_date"]
        status = request.form["status"]
        notes = request.form["notes"].strip()

        allowed_statuses = ["Applied", "Interview", "Rejected", "Offer"]

        if not company or not job_title or not application_date:
            connection.close()
            return "Company, job title and date are required.", 400

        if status not in allowed_statuses:
            connection.close()
            return "Invalid application status.", 400

        connection.execute(
            """
            UPDATE applications
            SET company = ?,
                job_title = ?,
                application_date = ?,
                status = ?,
                notes = ?
            WHERE id = ?
            """,
            (
                company,
                job_title,
                application_date,
                status,
                notes,
                application_id
            )
        )

        connection.commit()
        connection.close()

        return redirect(url_for("home"))

    connection.close()

    return render_template(
        "edit_application.html",
        application=application
    )


@app.route("/delete/<int:application_id>", methods=["POST"])
def delete_application(application_id):

    connection = get_db_connection()

    application = connection.execute(
        "SELECT id FROM applications WHERE id = ?",
        (application_id,)
    ).fetchone()

    if application is None:
        connection.close()
        abort(404)

    connection.execute(
        "DELETE FROM applications WHERE id = ?",
        (application_id,)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
