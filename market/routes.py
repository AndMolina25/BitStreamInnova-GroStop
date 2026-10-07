import random
from datetime import date, datetime

from flask import flash, redirect, render_template, request, url_for

from market import app, my_sql

# ---------------------------------------------------------------------------
# Estado del carrito (global, compartido por todo el proceso).
# NOTA: se mantiene igual que en la versión original para no romper el flujo
# actual, pero ver recomendaciones: debería migrarse a `flask.session`.
# ---------------------------------------------------------------------------
cart_id = 0
total_val = 0
total_count = 0
customer_cart_list = []

# Oferta por defecto con la que se crea el carrito (valor original: 3).
DEFAULT_OFFER_ID = 3
# Valor del formulario que significa "sin cupón".
NO_COUPON = 'Coupon_Code'


class StaticClass:
    cart_id = random.randint(1000, 100000)

    @staticmethod
    def giveCartId():
        StaticClass.cart_id += 1
        return StaticClass.cart_id


# ---------------------------------------------------------------------------
# Helpers de base de datos
# ---------------------------------------------------------------------------
def fetch_one(query, params=()):
    """Ejecuta un SELECT y devuelve una sola fila (o None)."""
    cur = my_sql.connection.cursor()
    try:
        cur.execute(query, params)
        return cur.fetchone()
    finally:
        cur.close()


def fetch_all(query, params=()):
    """Ejecuta un SELECT y devuelve todas las filas (tupla vacía si no hay)."""
    cur = my_sql.connection.cursor()
    try:
        cur.execute(query, params)
        return cur.fetchall()
    finally:
        cur.close()


def execute_write(query, params=()):
    """Ejecuta INSERT/UPDATE con commit, y rollback si algo falla."""
    cur = my_sql.connection.cursor()
    try:
        cur.execute(query, params)
        my_sql.connection.commit()
    except Exception:
        my_sql.connection.rollback()
        raise
    finally:
        cur.close()


def execute_many(query, rows):
    """Ejecuta varios INSERT en una sola transacción."""
    if not rows:
        return
    cur = my_sql.connection.cursor()
    try:
        cur.executemany(query, rows)
        my_sql.connection.commit()
    except Exception:
        my_sql.connection.rollback()
        raise
    finally:
        cur.close()


def like_pattern(term):
    """Convierte un texto en patrón LIKE '%texto%' escapando % y _ del usuario."""
    escaped = term.replace('\\', '\\\\').replace('%', '\\%').replace('_', '\\_')
    return f'%{escaped}%'


def reinitialize():
    """Reinicia el carrito al iniciar sesión un cliente."""
    global cart_id, total_val, total_count, customer_cart_list
    cart_id = StaticClass.giveCartId()
    total_val = 0
    total_count = 0
    customer_cart_list = []


# ---------------------------------------------------------------------------
# Administrador
# ---------------------------------------------------------------------------
@app.route('/admin/<admin_id>')
def adminRedirect(admin_id):
    total_users = fetch_one("SELECT COUNT(*) FROM customer")[0]
    total_products = fetch_one("SELECT COUNT(*) FROM product")[0]
    return render_template(
        'adminOption.html',
        admin_id=admin_id,
        total_users=total_users,
        total_products=total_products,
    )


@app.route('/adminOrder/<admin_id>', methods=['GET', 'POST'])
def adminViewOrder(admin_id):
    if request.method == 'POST':
        return redirect(url_for('adminRedirect', admin_id=admin_id))

    orders = fetch_all("SELECT * FROM orders")
    my_list = [
        {'Order_ID': order[0], 'Mode': order[1], 'Amount': order[2], 'Date': order[9]}
        for order in orders
    ]
    return render_template('viewOrder.html', list=my_list)


@app.route('/adminOffer/<admin_id>', methods=['GET', 'POST'])
def adminAddOffer(admin_id):
    if request.method == 'POST':
        form = request.form
        execute_write(
            "INSERT INTO offer(Promo_Code,Percentage_Discount,Min_OrderValue,Max_Discount,admin_id) "
            "VALUES(%s, %s, %s, %s, %s)",
            (form['Promo_Code'], form['Percentage_Discount'],
             form['Min_OrderValue'], form['Max_Discount'], admin_id),
        )
        flash('You have successfully added a Offer !')
    return render_template('addOffer.html', admin_id=admin_id)


@app.route('/adminDelivery_boy/<admin_id>', methods=['GET', 'POST'])
def adminAdd_Delivery_Boy(admin_id):
    if request.method == 'POST':
        form = request.form
        execute_write(
            "INSERT INTO delivery_boy(First_Name,Last_Name,Mobile_No,Email,Password,Average_Rating,Admin_ID) "
            "VALUES(%s, %s, %s, %s, %s, %s, %s)",
            (form['First_Name'], form['Last_Name'], form['Mobile_No'],
             form['Email'], form['Password'], None, admin_id),
        )
        flash('You have successfully added a delivery boy !')
    return render_template('addDelivery.html', admin_id=admin_id)


@app.route('/adminSeller/<admin_id>', methods=['GET', 'POST'])
def adminAdd_Seller(admin_id):
    if request.method == 'POST':
        form = request.form
        execute_write(
            "INSERT INTO seller(First_Name,Last_Name,Email,Phone_Number,Password,Place_Of_Operation,Admin_ID) "
            "VALUES(%s, %s, %s, %s, %s, %s, %s)",
            (form['First_Name'], form['Last_Name'], form['Email'],
             form['Phone_Number'], form['Password'], form['Place_Of_Operation'], admin_id),
        )
        flash('You have successfully added a seller !')
    return render_template('addSeller.html', admin_id=admin_id)


@app.route('/adminProduct/<admin_id>', methods=['GET', 'POST'])
def adminAdd_Product(admin_id):
    if request.method == 'POST':
        form = request.form
        execute_write(
            "INSERT INTO product(Name,Price,Brand,Measurement,Admin_ID,Category_ID,Unit) "
            "VALUES(%s, %s, %s, %s, %s, %s, %s)",
            (form['Name'], form['Price'], form['Brand'], form['Measurement'],
             admin_id, form['Category_ID'], form['Unit']),
        )
        flash('You have successfully added a Product !')
    return render_template('addNewProducts.html', admin_id=admin_id)


# ---------------------------------------------------------------------------
# Vendedor
# ---------------------------------------------------------------------------
@app.route('/sell/<seller_id>', methods=['GET', 'POST'])
def sell(seller_id):
    if request.method == 'POST':
        form = request.form
        try:
            quantity = int(form['Quantity'])
        except ValueError:
            quantity = -1

        product = fetch_one(
            "SELECT * FROM product WHERE Name = %s AND Brand = %s LIMIT 1",
            (form['Name'], form['Brand']),
        )
        if product is None or quantity < 0:
            flash('Invalid Product details or Quantity')
        else:
            execute_write(
                "INSERT INTO sells(Seller_ID,Product_ID,No_of_Product_Sold) VALUES(%s, %s, %s)",
                (seller_id, product[0], quantity),
            )
            flash('Product added successfully ')
    return render_template('addProduct.html')


# ---------------------------------------------------------------------------
# Cliente: catálogo, carrito y pedido
# ---------------------------------------------------------------------------
@app.route('/home/<user_id>', methods=['GET', 'POST'])
def userEnter(user_id):
    global total_count, total_val

    if request.method == 'POST':
        execute_write(
            "INSERT INTO cart(Cart_ID,Total_Value,Total_Count,Offer_ID,Final_Amount) "
            "VALUES(%s, %s, %s, %s, %s)",
            (cart_id, total_val, total_count, DEFAULT_OFFER_ID, total_val),
        )
        return redirect(url_for('placeOrder', user_id=user_id))

    # Agregar al carrito (se mantiene el mecanismo original por query string).
    args = request.args
    if all(key in args for key in ('Name', 'Brand', 'Price')):
        try:
            price = int(args['Price'])
        except ValueError:
            flash('Invalid product price')
        else:
            total_count += 1
            total_val += price
            customer_cart_list.append(
                {'Name': args['Name'], 'Brand': args['Brand'], 'Price': args['Price']}
            )
            flash('Product has been added successfully to the cart !')

    # Buscador: /home/<user_id>?q=texto
    q = (args.get('q') or '').strip()
    if q:
        products = fetch_all("SELECT * FROM product WHERE Name LIKE %s", (like_pattern(q),))
    else:
        products = fetch_all("SELECT * FROM product")

    my_list = [{'Name': p[1], 'Price': p[2], 'Brand': p[3]} for p in products]
    return render_template('home.html', list=my_list, q=q)


def _calculate_discount(promo_code, order_total):
    """Devuelve (oferta, descuento) para el código dado; (None, 0) si no aplica."""
    offer = fetch_one("SELECT * FROM offer WHERE Promo_Code = %s LIMIT 1", (promo_code,))
    if offer is None:
        return None, 0

    min_order_value = int(offer[3])
    max_discount = int(offer[4])
    if int(order_total) <= min_order_value:
        return offer, 0

    discount = (int(order_total) * float(offer[2])) / 100
    return offer, min(discount, max_discount)


@app.route('/order/<user_id>', methods=['GET', 'POST'])
def placeOrder(user_id):
    global total_val

    if request.method == 'POST':
        promo_code = request.form['Promo_Code']

        if promo_code == NO_COUPON:
            execute_write("UPDATE cart SET Offer_ID = %s WHERE Cart_ID = %s", (None, cart_id))
        else:
            offer, deduct = _calculate_discount(promo_code, total_val)
            if deduct == 0:
                execute_write("UPDATE cart SET Offer_ID = %s WHERE Cart_ID = %s", (None, cart_id))
            else:
                total_val -= deduct
                execute_write(
                    "UPDATE cart SET Offer_ID = %s, Final_Amount = %s WHERE Cart_ID = %s",
                    (offer[0], total_val, cart_id),
                )

        # Relacionar cada producto del carrito con el cliente y el carrito.
        associations = []
        for item in customer_cart_list:
            product = fetch_one(
                "SELECT * FROM product WHERE Name = %s LIMIT 1", (item['Name'],)
            )
            if product is not None:
                associations.append((user_id, cart_id, product[0]))
        execute_many(
            "INSERT INTO associated_with(Customer_ID,Cart_ID,Product_ID) VALUES(%s, %s, %s)",
            associations,
        )
        return redirect(url_for('order_placing', user_id=user_id))

    return render_template('order.html', list=customer_cart_list)


@app.route('/placeOrder/<user_id>', methods=['GET', 'POST'])
def order_placing(user_id):
    if request.method == 'POST':
        form = request.form
        delivery_boy = fetch_one("SELECT Delivery_Boy_ID FROM delivery_boy ORDER BY RAND() LIMIT 1")
        if delivery_boy is None:
            flash('No delivery partner is available right now. Please try again later.')
        else:
            execute_write(
                "INSERT INTO orders(Mode,Amount,City,State,Order_Time,House_Flat_No,Pincode,Cart_ID,Date,Delivery_Boy_ID) "
                "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (form['Mode'], total_val, form['City'], form['State'],
                 datetime.now().strftime("%H:%M:%S"), form['HNO'], form['Pincode'],
                 cart_id, date.today(), delivery_boy[0]),
            )
            flash('Your Order has been placed Successfully !')
    return render_template('orderDetails.html', total_val=total_val)


# ---------------------------------------------------------------------------
# Páginas estáticas
# ---------------------------------------------------------------------------
@app.route('/HomePage')
@app.route('/')
def homePage():
    return render_template('homepage.html')


@app.route('/loginRegisterSeller')
def loginRegisterSeller():
    return render_template('loginregisterSeller.html')


@app.route('/loginRegisterUser')
def loginRegisterUser():
    return render_template('loginregisterUser.html')


@app.route('/loginRegisterAdmin')
def loginRegisterAdmin():
    return render_template('loginregisterAdmin.html')


# ---------------------------------------------------------------------------
# Registro
# ---------------------------------------------------------------------------
@app.route('/customerRegister', methods=['GET', 'POST'])
def customerRegister():
    if request.method == 'POST':
        form = request.form
        execute_write(
            "INSERT INTO customer(First_Name,Last_Name,Email,Mobile_No,Password) "
            "VALUES(%s, %s, %s, %s, %s)",
            (form['First_Name'], form['Last_Name'], form['Email'],
             form['Mobile_No'], form['Password']),
        )
        flash('You have registered successfully !')
    return render_template('customerRegister.html')


@app.route('/adminRegister', methods=['GET', 'POST'])
def adminRegister():
    if request.method == 'POST':
        form = request.form
        execute_write(
            "INSERT INTO admin(First_Name,Last_Name,Admin_Password) VALUES(%s, %s, %s)",
            (form['First_Name'], form['Last_Name'], form['Password']),
        )
        flash('You have registered successfully !')
    return render_template('adminRegister.html')


@app.route('/sellerRegister', methods=['GET', 'POST'])
def sellerRegister():
    if request.method == 'POST':
        form = request.form
        admin = fetch_one("SELECT Admin_ID FROM admin ORDER BY RAND() LIMIT 1")
        if admin is None:
            flash('Registration is unavailable: no administrator exists yet.')
        else:
            execute_write(
                "INSERT INTO seller(First_Name,Last_Name,Email,Phone_Number,Password,Place_Of_Operation,Admin_ID) "
                "VALUES(%s, %s, %s, %s, %s, %s, %s)",
                (form['First_Name'], form['Last_Name'], form['Email'],
                 form['Phone_Number'], form['Password'], form['Place_Of_Operation'], admin[0]),
            )
            flash('You have registered successfully !')
    return render_template('sellerRegister.html')


# ---------------------------------------------------------------------------
# Login
# ---------------------------------------------------------------------------
@app.route('/UserLogin', methods=['GET', 'POST'])
def UserLogin():
    if request.method == 'POST':
        form = request.form
        customer = fetch_one("SELECT * FROM customer WHERE Email = %s LIMIT 1", (form['Email'],))
        if customer is None or form['Password'] != customer[5]:
            flash('Invalid Email or Password')
        else:
            reinitialize()
            return redirect(url_for('userEnter', user_id=customer[0]))
    return render_template('UserLogin.html')


@app.route('/AdminLogin', methods=['GET', 'POST'])
def AdminLogin():
    if request.method == 'POST':
        form = request.form
        admin = fetch_one(
            "SELECT * FROM admin WHERE First_Name = %s AND Last_Name = %s LIMIT 1",
            (form['First_Name'], form['Last_Name']),
        )
        if admin is None or form['Password'] != admin[3]:
            flash('Invalid Email or Password')
        else:
            return redirect(url_for('adminRedirect', admin_id=admin[0]))
    return render_template('AdminLogin.html')


@app.route('/SellerLogin', methods=['GET', 'POST'])
def SellerLogin():
    if request.method == 'POST':
        form = request.form
        seller = fetch_one("SELECT * FROM seller WHERE Email = %s LIMIT 1", (form['Email'],))
        if seller is None or form['Password'] != seller[5]:
            flash('Invalid Email or Password')
        else:
            return redirect(url_for('sell', seller_id=seller[0]))
    return render_template('SellerLogin.html')