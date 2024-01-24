from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from jobs_db_flask_sqlalchemy import connect, flask_init
app = flask_init()
db = connect(app)
#

with app.app_context():
    class Jobs(db.Model):
        
        __tablename__ = 'Jobs'
        id = db.Column(db.Integer, primary_key = True, autoincrement = True)
        title = db.Column(db.String(50))
        salary = db.Column(db.Float)
        symbol = db.Column(db.String(5))
        location = db.Column(db.String(50))
        

        def __repr__(self):
            return f"{self.title} {self.salary} R$"
        
        def get_jobs():
            
            busca = Jobs.query.all()
            jobs = []
            for job in busca:
                jobs.append(job)
            return busca
        
        def add_job():
    
            title = input("Title of Job: ")
            salary = float(input("Salary: "))
            location = input("Location: [country - est]")
            symbol = input("Monetary Symbol: ")
            new_job = Jobs(title = title, salary = salary, location = location, symbol = symbol)
            db.session.add(new_job)
            confirm = input(f"Do you confirm the addition of {title} - {salary}? [Y/N]").upper()
            if confirm == "Y":
                db.session.commit()
                x = input("Data Insert, do you wanna continue: [Y/N]").upper()
                
            else:
                db.session.rollback()
                print("Data not Inserted")
                
                    

        def delete_job():
            print("JOBS IN DATABASE")
            name_job = Jobs.get_jobs()
            job_id = input("Wich job id do you wanna delete: ")
            job_delete = Jobs.query.get(job_id)
            
            if job_delete:
                db.session.delete(job_delete)
                db.session.commit()
                print("Job deleted successfully")
            else:
                print("Job not found")

        def drop_table():
            table_name = Jobs.__tablename__
            table = db.metadata.tables.get(table_name)
            table.drop(db.engine)
            print(f"Table '{table_name}' deleted successfully.")

    # class Candidate(db.Model):
    
    #     __table__name = 'Candidate'
    #     id = db.Column(db.Integer, primary_key =True, autoincrement = True)
    #     name = db.Column(db.String(50))
    #     email = db.Column(db.String(70))
    #     resume = db.Column(db.String(500))
    #     portfolio = db.Column(db.String())
    
    @app.route("/")
    def home():
        query = Jobs.get_jobs()
        return render_template('01_index.html', query = query)

    @app.route("/jobs/<id>")
    def jobs_page(id = Jobs.id, title = Jobs.title):
        id_page = id
        query_job = Jobs.query.filter_by(id = id_page)
        return render_template("02_job_page.html", query = query_job)
    
    @app.route("/application")
    def application():
        return render_template("03_application.html")
   
    #Jobs.drop_table()
    # with app.app_context():
    #db.create_all()

    if __name__ == "__main__":
        app.run(host = '0.0.0.0', debug = True) 


    