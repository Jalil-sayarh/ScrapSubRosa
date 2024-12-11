
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

