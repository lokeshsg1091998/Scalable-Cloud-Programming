from flask import Flask, render_template, request
from database import init_db
from models import Calculation
from tax_engine import TaxEngine
import json

app = Flask(__name__)

init_db()

@app.route("/", methods=["GET", "POST"])
def dashboard():

    results = None
    chart_data = None

    if request.method == "POST":
        try:
            gross = float(request.form.get("gross", 0))
            deductions = float(request.form.get("deductions", 0))

            results = TaxEngine.compute(gross, deductions)

            Calculation.save(results)

            chart_data = json.dumps([
                results["gross"],
                results["deductions"],
                results["tax_payable"],
                results["net_income"]
            ])

        except ValueError:
            results = None

    history = Calculation.last_five()

    return render_template(
        "dashboard.html",
        results=results,
        history=history,
        chart_data=chart_data
    )


if __name__ == "__main__":
    app.run(debug=True)