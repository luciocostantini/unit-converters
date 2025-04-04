from flask import Flask, render_template, request

app = Flask(__name__)

# --- Conversion Functions ---

def temperature(initialTemp, initialTempUnit, finalTempUnit):
    c_temp = initialTemp
    if initialTempUnit.lower() == 'f':
        c_temp = (c_temp - 32) * (5 / 9)
    elif initialTempUnit.lower() == 'k':
        c_temp -= 273.15

    if finalTempUnit.lower() == 'f':
        return c_temp * (9 / 5) + 32
    elif finalTempUnit.lower() == 'k':
        return c_temp + 273.15
    else:
        return c_temp

def weight(initialWeight, initialWeightUnit, finalWeightUnit):
    g_weight = initialWeight
    if initialWeightUnit.lower() == 'oz':
        g_weight *= 28.35
    elif initialWeightUnit.lower() == 'lb':
        g_weight *= 453.6
    elif initialWeightUnit.lower() == 'kg':
        g_weight *= 1000
    elif initialWeightUnit.lower() == 'mg':
        g_weight /= 1000

    if finalWeightUnit.lower() == 'oz':
        g_weight /= 28.3495
    elif finalWeightUnit.lower() == 'lb':
        g_weight /= 453.592
    elif finalWeightUnit.lower() == 'kg':
        g_weight /= 1000
    elif finalWeightUnit.lower() == 'mg':
        g_weight *= 1000
    return g_weight

def length(initialLength, initialLengthUnit, finalLengthUnit):
    m_length = initialLength
    if initialLengthUnit.lower() == 'mm':
        m_length /= 1000
    elif initialLengthUnit.lower() == 'cm':
        m_length /= 100
    elif initialLengthUnit.lower() == 'km':
        m_length *= 1000
    elif initialLengthUnit.lower() == 'in':
        m_length /= 39.37
    elif initialLengthUnit.lower() == 'ft':
        m_length /= 3.281
    elif initialLengthUnit.lower() == 'yd':
        m_length *= 0.9144
    elif initialLengthUnit.lower() == 'mi':
        m_length *= 1609.32

    if finalLengthUnit.lower() == 'mm':
        m_length *= 1000
    elif finalLengthUnit.lower() == 'cm':
        m_length *= 100
    elif finalLengthUnit.lower() == 'km':
        m_length /= 1000
    elif finalLengthUnit.lower() == 'in':
        m_length *= 39.37
    elif finalLengthUnit.lower() == 'ft':
        m_length *= 3.281
    elif finalLengthUnit.lower() == 'yd':
        m_length /= 0.9144
    elif finalLengthUnit.lower() == 'mi':
        m_length /= 1609.32
    return m_length

# --- Flask Route ---

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        category = request.form['category']
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']

        if category == 'length':
            result_value = length(value, from_unit, to_unit)
        elif category == 'weight':
            result_value = weight(value, from_unit, to_unit)
        elif category == 'temperature':
            result_value = temperature(value, from_unit, to_unit)
        else:
            result_value = 'Invalid category'

        result = f"{value} {from_unit} = {result_value:.2f} {to_unit}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)


