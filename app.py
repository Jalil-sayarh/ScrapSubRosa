from flask import Flask, request, jsonify
from linkedin_api import Linkedin
from linkedin_cookies import cookiejar

app = Flask(__name__)

# Route to authenticate and search jobs
@app.route('/search_jobs', methods=['GET'])
def search_jobs():
    # Get query parameters
    username = request.args.get('username')
    password = request.args.get('password')
    keywords = request.args.get('keywords')
    location = request.args.get('location')
    experience = request.args.getlist('experience')  # List of experience levels
    job_type = request.args.getlist('job_type')  # List of job types
    industries = request.args.getlist('industries')  # List of industry URN IDs
    limit = int(request.args.get('limit', 10))  # Default limit to 10

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    try:
        # Authenticate with LinkedIn
        linkedin = Linkedin(username, password, cookies=cookiejar)

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
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
