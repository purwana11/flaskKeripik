from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Define the Pesanan model for CRUD operations
class Pesanan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    produk = db.Column(db.String(100), nullable=False)
    jumlah = db.Column(db.Integer, nullable=False)
    harga = db.Column(db.Integer, nullable=False)
    total_harga = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<Pesanan {self.id}>'

@app.route("/reservation", methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        nama = request.form['nama']
        produk = request.form['produk']
        jumlah = int(request.form['jumlah'])
        harga = int(request.form['harga'])
        total_harga = jumlah * harga

        # Membuat instance baru Pesanan dan menambahkannya ke basis data
        new_order = Pesanan(nama=nama, produk=produk, jumlah=jumlah, harga=harga, total_harga=total_harga)
        db.session.add(new_order)
        db.session.commit()
        
        return redirect(url_for('testimonial'))
    
    return render_template("reservation.html")

@app.route("/hasilpesanan")
def hasilpesanan():
    # Retrieve all orders from the database
    orders = Pesanan.query.all()
    return render_template("reservation.html", orders=orders)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/testimonial")
def testimonial():
    return render_template("testimonial.html")

@app.route("/service")
def service():
    return render_template("service.html")

if __name__ == "__main__":
    app.run(debug=True)