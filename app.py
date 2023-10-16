from flask import Flask, render_template

app = Flask(__name__)  # Create Flask app

@app.route('/fizzbuzz')  # Define route for FizzBuzz page
def fizzbuzz():
    data = []  # Initialize list for FizzBuzz results
    for num in range(1, 101):  # Loop through numbers 1 to 100
        if num % 15 == 0:
            data.append('FizzBuzz')  # Divisible by both 3 and 5
        elif num % 3 == 0:
            data.append('Fizz')  # Divisible by 3
        elif num % 5 == 0:
            data.append('Buzz')  # Divisible by 5
        else:
            data.append(num)  # Other numbers

    return render_template('fizzbuzz.html', data=data)  # Render template with FizzBuzz data

if __name__ == '__main__':
    app.run(debug=True)  # Start app with debugging
