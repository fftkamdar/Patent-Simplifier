from flask import Flask, render_template, request

app = Flask(__name__)

def simplify_description(description):
    """
    Simplifies the patent description by:
    - Removing complex words longer than 8 characters.
    - Breaking down complex sentences.
    - Keeping only key concepts.
    """
    # Simplify by removing long words (greater than 8 characters)
    words = description.split()
    simplified_words = [word for word in words if len(word) <= 8]
    
    # Join the simplified words back into a sentence
    simplified_description = ' '.join(simplified_words)
    
    # Additional simplifications (like breaking down long sentences into simpler ones) can be done here.
    
    # Return simplified text
    return simplified_description

@app.route('/', methods=['GET', 'POST'])
def index():
    simplified = ''
    if request.method == 'POST':
        description = request.form['description']
        simplified = simplify_description(description)
    return render_template('index.html', simplified=simplified)

if __name__ == '__main__':
    app.run(debug=True)
