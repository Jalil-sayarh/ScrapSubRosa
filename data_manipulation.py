
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
