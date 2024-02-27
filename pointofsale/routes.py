from flask import render_template, request, redirect, url_for
from pointofsale import app, db
from pointofsale.models import Menus, Submenus, Items, Currentorder


@app.route("/")
def home():
    return render_template("startscreen.html")


@app.route("/main_menu")
def main_menu():
    menus = list(Menus.query.order_by(Menus.menus_name).all())
    return render_template("main_menu.html", menus=menus)


@app.route("/add_menus", methods=["GET", "POST"])
def add_menus():
    if request.method == "POST":
        menus = Menus(
            menus_name=request.form.get("menus_name"),
            menus_description = request.form.get("menus_description")
        )
        db.session.add(menus)
        db.session.commit()
        return redirect(url_for("main_menu"))
    return render_template("add_menus.html")


@app.route("/edit_menus/<int:menus_id>", methods=["GET", "POST"])
def edit_menus(menus_id):
    menus = Menus.query.get_or_404(menus_id)
    if request.method == "POST":
        menus.menus_name=request.form.get("menus_name"),
        menus.menus_description=request.form.get("menus_description")
        db.session.add(menus)
        db.session.commit()
        return redirect(url_for("main_menu"))
    return render_template("edit_menus.html", menus=menus)


@app.route("/delete_menus/<int:menus_id>", methods=["GET", "POST"])
def delete_menus(menus_id):
    menus = Menus.query.get_or_404(menus_id)
    if request.method == "POST":
        db.session.delete(menus)
        db.session.commit()
        return redirect(url_for("main_menu"))
    return render_template("delete_menus.html", menus=menus)


@app.route("/add_submenus/<int:submenus_id>", methods=["GET", "POST"])
def add_submenus(submenus_id):
    submenus = list(Submenus.query.filter_by(menus_id=submenus_id).all())
    menus = Menus.query.get_or_404(submenus_id)
    if request.method == "POST":
        submenus=Submenus(
            submenu_name=request.form.get("submenus_name"),
            submenu_description=request.form.get("submenus_description"),
            menus_id=submenus_id
        )
        db.session.add(submenus)
        db.session.commit()
    return render_template("add_submenus.html", menus=menus, submenus=submenus, submenus_id=submenus_id)


@app.route("/view_submenus/<int:submenus_id>")
def view_submenus(submenus_id):
    submenus = list(Submenus.query.filter_by(menus_id=submenus_id).all())
    menus = Menus.query.get_or_404(submenus_id)
    return render_template("view_submenus.html",menus=menus, submenus=submenus, submenus_id=submenus_id)


@app.route("/edit_submenus/<int:submenus_id>", methods=["GET", "POST"])
def edit_submenus(submenus_id):
    submenus = Submenus.query.get_or_404(submenus_id)
    if request.method == "POST":
        submenus.submenu_name=request.form.get("submenus_name"),
        submenus.submenu_description=request.form.get("submenus_description")
        db.session.add(submenus)
        db.session.commit()
        return redirect(url_for("view_submenus", submenus_id=submenus.menus_id))
    return render_template("edit_submenus.html", submenus=submenus)


@app.route("/delete_submenus/<int:submenus_id>", methods=["GET", "POST"])
def delete_submenus(submenus_id):
    submenus=Submenus.query.get_or_404(submenus_id)
    if request.method == "POST":
        db.session.delete(submenus)
        db.session.commit()
        return redirect(url_for("view_submenus", submenus_id=submenus.menus_id))
    return render_template("delete_submenus.html", submenus=submenus)


@app.route("/view_items/<int:menus_id>", methods=["GET", "POST"])
def view_items( menus_id):
    submenus = Submenus.query.get_or_404(menus_id)
    items=list(Items.query.filter_by(submenus_id=menus_id).all())
    return render_template("view_items.html", items=items, submenus=submenus, menus_id=menus_id)


@app.route("/add_items/<int:menus_id>", methods=["GET", "POST"])
def add_items(menus_id):
    items=list(Items.query.order_by(Items.submenus_id).all())
    submenus=Submenus.query.get_or_404(menus_id)
    if request.method == "POST":
        items=Items(
            items_name=request.form.get("items_name"),
            items_description=request.form.get("items_description"),
            items_price=request.form.get("items_price"),
            submenus_id=menus_id
        )
        db.session.add(items)
        db.session.commit()
    return render_template("add_items.html", items=items, menus_id=menus_id, submenus=submenus)


@app.route("/edit_items/<int:submenus_id>", methods=["GET", "POST"])
def edit_items(submenus_id):
    items = Items.query.get_or_404(submenus_id)
    submenus_name=Submenus.query.get_or_404(items.submenus_id)
    if request.method == "POST":
        items.items_name=request.form.get("items_name"),
        items.items_description=request.form.get("items_description"),
        items.items_price=request.form.get("items_price"),
        db.session.add(items)
        db.session.commit()
        return redirect(url_for("view_items", menus_id=items.submenus_id, items=items))
    return render_template("edit_items.html", submenus_id=submenus_id, items=items, submenus_name=submenus_name)


@app.route("/delete_items/<int:submenus_id>", methods=["GET", "POST"])
def delete_items(submenus_id):
    items=Items.query.get_or_404(submenus_id)
    if request.method == "POST":
        db.session.delete(items)
        db.session.commit()
        return redirect(url_for("view_items", menus_id=items.submenus_id, items=items))
    return render_template("delete_items.html", submenus_id=submenus_id, items=items)


@app.route("/current_order")
def current_order():
    current_order = list(Currentorder.query.order_by(Currentorder.id).all())
    global total_price
    total_price=0
    for price in current_order:
        total_price+=price.currentorder_price
    return render_template("current_order.html", current_order=current_order, total_price=total_price)

@app.route("/addto_order/<int:item_id>/<int:submenus_id>/<item_name>/<item_price>", methods=["GET", "POST"])
def addto_order(item_id, item_name, item_price, submenus_id):
    submenus=Submenus.query.get_or_404(submenus_id)
    items=list(Items.query.filter_by(submenus_id=submenus_id).all())
    current_order=Currentorder(
        currentorder_name=item_name,
        currentorder_price=item_price,
        item_id=item_id
    )
    db.session.add(current_order)
    db.session.commit()
    return render_template("view_items.html", menus_id=item_id, submenus_id=submenus_id, submenus=submenus, items=items)


@app.route("/remove_item/<int:item_id>", methods=["GET", "POST"])
def remove_item(item_id):
    delete_item=Currentorder.query.get_or_404(item_id)
    item_name=delete_item.currentorder_name
    if request.method == "POST":
        db.session.delete(delete_item)
        db.session.commit()
        return redirect(url_for("current_order"))
    return render_template("remove_item.html", delete_item=delete_item, item_id=item_id, item_name=item_name)


@app.route("/sales")
def sales():
    return render_template("sales.html")


@app.route("/startscreen")
def startscreen():
    return render_template("startscreen.html")
