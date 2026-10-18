
from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import current_user, login_required

from ..extensions import db
from ..models.equipment import Equipment

equipment_bp = Blueprint(
    "equipment",
    __name__,
    url_prefix="/equipment",
)

ALLOWED_STATUSES = ("Available", "Out of service")


def require_staff():
    """Prevent Students from managing equipment."""
    if not current_user.is_staff:
        abort(403)


def validate_equipment_form():
    """Clean and validate submitted equipment information."""
    values = {
        "name": request.form.get("name", "").strip(),
        "category": request.form.get("category", "").strip(),
        "description": request.form.get(
            "description", ""
        ).strip(),
        "status": request.form.get("status", "").strip(),
    }

    if not 1 <= len(values["name"]) <= 120:
        return values, "Name must be 1-120 characters."

    if not 1 <= len(values["category"]) <= 80:
        return values, "Category must be 1-80 characters."

    if len(values["description"]) > 2000:
        return values, "Description is too long."

    if values["status"] not in ALLOWED_STATUSES:
        return values, "Invalid equipment status."

    return values, None


@equipment_bp.get("/")
@login_required
def catalogue():
    """Display all equipment or filter by category."""
    selected_category = request.args.get(
        "category", ""
    ).strip()

    statement = db.select(Equipment).order_by(
        Equipment.name.asc(),
        Equipment.id.asc(),
    )

    if selected_category:
        statement = statement.where(
            Equipment.category == selected_category
        )

    equipment_items = db.session.scalars(
        statement
    ).all()

    categories = db.session.scalars(
        db.select(Equipment.category)
        .distinct()
        .order_by(Equipment.category.asc())
    ).all()

    return render_template(
        "equipment/catalogue.html",
        equipment_items=equipment_items,
        categories=categories,
        selected_category=selected_category,
    )


@equipment_bp.route("/new", methods=["GET", "POST"])
@login_required
def add():
    """Allow Staff to add equipment."""
    require_staff()

    if request.method == "POST":
        values, error = validate_equipment_form()

        if error:
            flash(error, "error")
            return render_template(
                "equipment/form.html",
                equipment=None,
                form_data=values,
                statuses=ALLOWED_STATUSES,
            ), 400

        equipment = Equipment(**values)

        db.session.add(equipment)
        db.session.commit()

        flash("Equipment added successfully.", "success")

        return redirect(url_for("equipment.catalogue"))

    return render_template(
        "equipment/form.html",
        equipment=None,
        form_data={},
        statuses=ALLOWED_STATUSES,
    )


@equipment_bp.route(
    "/<int:equipment_id>/edit",
    methods=["GET", "POST"],
)
@login_required
def edit(equipment_id):
    """Allow Staff to update equipment."""
    require_staff()

    equipment = db.get_or_404(
        Equipment,
        equipment_id,
    )

    if request.method == "POST":
        values, error = validate_equipment_form()

        if error:
            flash(error, "error")
            return render_template(
                "equipment/form.html",
                equipment=equipment,
                form_data=values,
                statuses=ALLOWED_STATUSES,
            ), 400

        equipment.name = values["name"]
        equipment.category = values["category"]
        equipment.description = values["description"]
        equipment.status = values["status"]

        db.session.commit()

        flash("Equipment updated successfully.", "success")

        return redirect(url_for("equipment.catalogue"))

    return render_template(
        "equipment/form.html",
        equipment=equipment,
        form_data={},
        statuses=ALLOWED_STATUSES,
    )


@equipment_bp.post("/<int:equipment_id>/delete")
@login_required
def delete(equipment_id):
    """Allow Staff to delete equipment."""
    require_staff()

    equipment = db.get_or_404(
        Equipment,
        equipment_id,
    )

    db.session.delete(equipment)
    db.session.commit()

    flash("Equipment deleted successfully.", "success")

    return redirect(url_for("equipment.catalogue"))
