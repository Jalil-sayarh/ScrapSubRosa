import re

def extract_job_ids(job_results):
    """
    Extracts job IDs from a list of job postings.

    Args:
        job_results (list): List of job postings, each as a dictionary.

    Returns:
        list: List of job IDs, each as a string.
    """
    job_ids = []

    for job in job_results:
        # Ensure the entityUrn key exists in the job posting
        if "entityUrn" in job:
            # Extract the ID from the entityUrn (the part after 'fsd_jobPosting:')
            entity_urn = job["entityUrn"]
            job_id = entity_urn.split(":")[-1]  # Get the last part of the URN
            
            job_ids.append(job_id)

    return job_ids

def fetch_job_details(linkedin, job_ids, keys_to_extract):
    """
    Fetch job details for each job ID and extract specified keys, including nested keys.

    Args:
        linkedin (Linkedin): Authenticated Linkedin object.
        job_ids (list): List of job IDs.
        keys_to_extract (list): Flat list of keys to extract. Nested keys should be handled dynamically.

    Returns:
        list: A list of dictionaries containing extracted job details.
    """
    job_details_list = []

    for job_id in job_ids:
        try:
            # Fetch job details using the LinkedIn API
            job_data = linkedin.get_job(job_id)

            # Initialize a dictionary to store the extracted data
            extracted_data = {}

            for key in keys_to_extract:
                # Dynamically extract nested keys
                value = None
                if key == "name":  # Company name
                    value = (
                        job_data.get("companyDetails", {})
                        .get("com.linkedin.voyager.deco.jobs.web.shared.WebCompactJobPostingCompany", {})
                        .get("companyResolutionResult", {})
                        .get("name", None)
                    )
                elif key == "url":  # Company URL
                    value = (
                        job_data.get("companyDetails", {})
                        .get("com.linkedin.voyager.deco.jobs.web.shared.WebCompactJobPostingCompany", {})
                        .get("companyResolutionResult", {})
                        .get("url", None)
                    )
                elif key == "text":  # Job description text
                    value = job_data.get("description", {}).get("text", None)
                elif key == "formattedLocation":  # Job location
                    value = job_data.get("formattedLocation", None)
                elif key == "company_apply_url":  # Apply URL
                    value = (
                        job_data.get("applyMethod", {})
                        .get("com.linkedin.voyager.jobs.OffsiteApply", {})
                        .get("companyApplyUrl", None)
                    )
                elif key == "title":  # Job title
                    value = job_data.get("title", None)

                # Add the extracted value to the dictionary
                extracted_data[key] = value

            # Append the dictionary to the results list
            job_details_list.append(extracted_data)
        except Exception as e:
            print(f"Error fetching job {job_id}: {e}")
            # Optionally, add an entry with error info
            job_details_list.append({"job_id": job_id, "error": str(e)})

    return job_details_list


def filter_jobs_by_keywords(job_details_list, disqualifying_keywords = ["stage", "alternant", "intern", "trainee", "junior","internship"], fields_to_check=["title", "text"]):
    """
    Filters job details based on the presence of disqualifying keywords.

    Args:
        job_details_list (list): List of job details dictionaries.
        disqualifying_keywords (list): List of keywords to filter out.
        fields_to_check (list): List of fields to check for keywords (e.g., "title", "text").

    Returns:
        list: A filtered list of job details dictionaries.
    """
    filtered_jobs = []

    # Compile regular expressions for the disqualifying keywords
    keyword_patterns = [re.compile(rf'\b{re.escape(keyword)}\b', re.IGNORECASE) for keyword in disqualifying_keywords]

    for job_details in job_details_list:
        # Flag to determine if the job should be disqualified
        disqualify = False

        for field in fields_to_check:
            # Check if the field exists and contains a value
            field_value = job_details.get(field, "").lower()

            # Check for disqualifying keywords as whole words in the field value
            if any(pattern.search(field_value) for pattern in keyword_patterns):
                disqualify = True
                break  # No need to check further fields for this job

        # Add the job to the filtered list if it's not disqualified
        if not disqualify:
            filtered_jobs.append(job_details)

    return filtered_jobs
