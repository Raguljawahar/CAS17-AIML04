from flask import Flask, request, jsonify, render_template
import os
from toxicity_detector import detect_toxicity_with_label
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__, 
            static_folder='../static',
            template_folder='../templates')

logger.info("Initializing toxicity detection model...")

@app.route('/')
def index():
    """Serve the main chat page"""
    return render_template('index.html')

@app.route('/api/detect-toxicity', methods=['POST'])
def api_detect_toxicity():
    """API endpoint for toxicity detection"""
    try:
        data = request.json
        if not data or 'text' not in data:
            return jsonify({'error': 'No text provided'}), 400
        
        text = data['text']
        logger.info(f"Received toxicity detection request: '{text[:30]}...'")
        
        toxicity_scores, label = detect_toxicity_with_label(text)
        
        response = {
            'isToxic': label == 'Toxic',
            'categories': {}
        }
        
        for category, score in toxicity_scores.items():
            response['categories'][category] = {
                'match': score >= 0.5,
                'probability': score
            }
        
        logger.info(f"Toxicity detection result: {label}")
        return jsonify(response)
    
    except Exception as e:
        logger.error(f"Error in toxicity detection: {str(e)}", exc_info=True)
        return jsonify({'error': str(e)}), 500

@app.errorhandler(404)
def not_found(e):
    return render_template('index.html'), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
