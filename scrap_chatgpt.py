import urllib.parse


def build_indeed_url(base_url, query, location, experience_level=None, is_remote=None, education=None, start=None):
    url_params = {
        'q': query,
        'l': location,
    }
    if experience_level:
        url_params['explvl'] = experience_level
    if is_remote:
        url_params['remote'] = 'true' if is_remote else 'false'
    if education:
        url_params['edu'] = education
    if start:
        url_params['start'] = start

    query_string = urllib.parse.urlencode(url_params)
    return f"{base_url}?{query_string}"


# Example usage:
base_url = 'https://www.indeed.com/jobs'
query = 'Quality Engineer, $50,000'
location = 'Lafayette, IN'
experience_level = 'entry_level'
is_remote = False
education = 'Bachelor'
start=10

url = build_indeed_url(base_url, query, location, experience_level, is_remote, education, start)
print(url)