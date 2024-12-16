from flask import Flask, request, jsonify
from linkedin_api import Linkedin
from linkedin_cookies import accounts_cookies
from data_manipulation import extract_job_ids, fetch_job_details, filter_jobs_by_keywords

app = Flask(__name__)

def get_authenticated_linkedin(username, password):
    """Authenticate to LinkedIn using the provided username."""
    if username not in accounts_cookies:
        available_accounts = list(accounts_cookies.keys())
        return None, jsonify({
            "error": f"No cookies found for this account: {username}.",
            "available_accounts": available_accounts
        }), 400

    selected_cookies = accounts_cookies[username]
    linkedin = Linkedin(username, password, cookies=selected_cookies)
    return linkedin, None

# Endpoint to get job IDs based on search parameters
@app.route('/get_job_ids', methods=['GET'])
def get_job_ids():
    username = request.args.get('username', "abdeljalil.sayarh@gmail.com")
    password = request.args.get('password', "54321Nisk@")
    keywords = request.args.get('keywords')
    location = request.args.get('location')
    experience = request.args.getlist('experience')
    job_type = request.args.getlist('job_type')
    industries = request.args.getlist('industries')
    limit = int(request.args.get('limit', 10))

    linkedin, error_response = get_authenticated_linkedin(username,password)
    if error_response:
        return error_response

    try:
        jobs = linkedin.search_jobs(
            keywords=keywords,
            location_name=location,
            experience=experience,
            job_type=job_type,
            industries=industries,
            limit=limit
        )
        if not jobs:
            return jsonify({"error": "No jobs found for the given parameters.", "job_ids": []}), 404

        job_ids = extract_job_ids(jobs)
        return jsonify({"job_ids": job_ids})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to fetch job details given a list of job IDs
@app.route('/fetch_job_details', methods=['GET'])
def fetch_job_details_endpoint():
    username = request.args.get('username', "abdeljalil.sayarh@gmail.com")
    password = request.args.get('password', "54321Nisk@")
    job_id = request.args.get('job_id')

    if not job_id:
        return jsonify({"error": "Missing 'job_id' parameter."}), 400

    linkedin, error_response = get_authenticated_linkedin(username,password)
    if error_response:
        return error_response

    try:
        # Convert job_id into a list of one element
        job_id = str(job_id)
        job_ids = [job_id]
        keys_to_extract = ["title", "name", "url", "formattedLocation", "company_apply_url", "text"]

        jobs_details = fetch_job_details(linkedin, job_ids, keys_to_extract)
        return jsonify({"jobs_details": jobs_details})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
