import ui

# Function to compare groceries based on input from the UI
def compare_groceries(sender):
    # Get input values from text fields
    ounces_a = float(view['ounces_a'].text)
    price_a = float(view['price_a'].text)
    ounces_b = float(view['ounces_b'].text)
    price_b = float(view['price_b'].text)
    ounces_c = float(view['ounces_c'].text)
    price_c = float(view['price_c'].text)

    # Calculate cost per ounce for Grocery A, B, and C
    cost_per_oz_a = price_a / ounces_a
    cost_per_oz_b = price_b / ounces_b
    cost_per_oz_c = price_c / ounces_c

    # Compare and find the best value among the three
    result = f"Grocery A: ${cost_per_oz_a:.2f} per ounce\n"
    result += f"Grocery B: ${cost_per_oz_b:.2f} per ounce\n"
    result += f"Grocery C: ${cost_per_oz_c:.2f} per ounce\n"
    
    # Determine the best value
    if cost_per_oz_a < cost_per_oz_b and cost_per_oz_a < cost_per_oz_c:
        result += "\nGrocery A offers the best value."
    elif cost_per_oz_b < cost_per_oz_a and cost_per_oz_b < cost_per_oz_c:
        result += "\nGrocery B offers the best value."
    elif cost_per_oz_c < cost_per_oz_a and cost_per_oz_c < cost_per_oz_b:
        result += "\nGrocery C offers the best value."
    else:
        result += "\nSome groceries offer the same value per ounce."

    # Update the result label with the comparison result
    view['result_label'].text = result

# Load and create the user interface in Pythonista
view = ui.View()  # Create the main view
view.name = 'Grocery Comparison'
view.background_color = 'white'

# Add text fields and labels for Grocery A
label_a = ui.Label(frame=(10, 10, 200, 40))
label_a.text = 'Grocery A (Ounces and Price):'
view.add_subview(label_a)

ounces_a = ui.TextField(frame=(10, 50, 100, 40))
ounces_a.placeholder = 'Ounces A'
ounces_a.name = 'ounces_a'
view.add_subview(ounces_a)

price_a = ui.TextField(frame=(120, 50, 100, 40))
price_a.placeholder = 'Price A ($)'
price_a.name = 'price_a'
view.add_subview(price_a)

# Add text fields and labels for Grocery B
label_b = ui.Label(frame=(10, 110, 200, 40))
label_b.text = 'Grocery B (Ounces and Price):'
view.add_subview(label_b)

ounces_b = ui.TextField(frame=(10, 150, 100, 40))
ounces_b.placeholder = 'Ounces B'
ounces_b.name = 'ounces_b'
view.add_subview(ounces_b)

price_b = ui.TextField(frame=(120, 150, 100, 40))
price_b.placeholder = 'Price B ($)'
price_b.name = 'price_b'
view.add_subview(price_b)

# Add text fields and labels for Grocery C
label_c = ui.Label(frame=(10, 210, 200, 40))
label_c.text = 'Grocery C (Ounces and Price):'
view.add_subview(label_c)

ounces_c = ui.TextField(frame=(10, 250, 100, 40))
ounces_c.placeholder = 'Ounces C'
ounces_c.name = 'ounces_c'
view.add_subview(ounces_c)

price_c = ui.TextField(frame=(120, 250, 100, 40))
price_c.placeholder = 'Price C ($)'
price_c.name = 'price_c'
view.add_subview(price_c)

# Add a button to perform the comparison
compare_button = ui.Button(frame=(10, 310, 100, 40))
compare_button.title = 'Compare'
compare_button.action = compare_groceries
view.add_subview(compare_button)

# Add a label to display the result
result_label = ui.Label(frame=(10, 370, 300, 100))
result_label.name = 'result_label'
result_label.text = ''
view.add_subview(result_label)

# Present the UI as a sheet in Pythonista
view.present('sheet')
