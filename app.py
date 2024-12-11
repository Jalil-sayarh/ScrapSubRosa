from flask import Flask, request, jsonify
from linkedin_api import Linkedin

app = Flask(__name__)

# Route to authenticate and search jobs
@app.route('/search_jobs', methods=['GET'])
def search_jobs():
    # Get request data
    data = request.json
    username = data.get('username')
    password = data.get('password')
    keywords = data.get('keywords')
    location = data.get('location', None)
    experience = data.get('experience', [])
    job_type = data.get('job_type', [])
    industries = data.get('industries', [])
    limit = data.get('limit', 10)

    # Authenticate with LinkedIn
    linkedin = Linkedin(username, password)

    # Search for jobs
    jobs = linkedin.search_jobs(
        keywords=keywords,
        location_name=location,
        experience=experience,
        job_type=job_type,
        industries=industries,
        limit=limit
    )

    return jsonify(jobs)

if __name__ == '__main__':
    app.run(port=5000)
