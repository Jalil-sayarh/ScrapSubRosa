from flask import Flask, request, jsonify
from linkedin_api import Linkedin
from linkedin_cookies import accounts_cookies
from data_manipulation import extract_job_ids, fetch_job_details, filter_jobs_by_keywords

app = Flask(__name__)

# Route to authenticate and search jobs
@app.route('/search_jobs', methods=['GET'])
def search_jobs():
    # Get query parameters
    username = request.args.get('username', "abdeljalil.sayarh@gmail.com")
    password = request.args.get('password', "54321Nisk@")
    keywords = request.args.get('keywords')
    location = request.args.get('location')
    experience = request.args.getlist('experience')  # List of experience levels
    job_type = request.args.getlist('job_type')  # List of job types
    industries = request.args.getlist('industries')  # List of industry URN IDs
    limit = int(request.args.get('limit', 10))  # Default limit to 10 jobs

    try:
        # Check if the username exists in accounts_cookies
        if username not in accounts_cookies:
            available_accounts = list(accounts_cookies.keys())
            return jsonify({
                "error": f"No cookies found for this account: {username}.",
                "available_accounts": available_accounts
            }), 400

        # Retrieve cookies for the specified username
        selected_cookies = accounts_cookies[username]

        # Authenticate with LinkedIn
        linkedin = Linkedin(username, password, cookies=selected_cookies)

        # Search for jobs
        jobs = linkedin.search_jobs(
            keywords=keywords,
            location_name=location,
            experience=experience,
            job_type=job_type,
            industries=industries,
            limit=limit
        )

        # Process job results
        job_ids = extract_job_ids(jobs)
        jobs_details = fetch_job_details(linkedin, job_ids, ["title", "name", "url", "formattedLocation", "company_apply_url", "text"])
        relevant_jobs = filter_jobs_by_keywords(jobs_details)

        return jsonify({"relevant_jobs": relevant_jobs})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
