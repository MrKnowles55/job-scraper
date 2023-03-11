# Salary Estimate : q=%$X&l=
#       goes between q= and l=

# Posted by : sc=0bf%3AexX3B&
#   Employer =    rec%28%29%
#   Recruiter =   dh()%

# Remote : sc= X
#   Remote = 0kf%3Aattr%28DSQF7%29%3B&
#   Posted by AND Remote = 0bf%3AexYCX3B&
#       where Y is Posted by variable


# Where : City+Name%2C+STATE&

# Within : radius=X&    (blank if 25 miles)
#   1, 5, 10, 15, 25, 35, 50, 100

# Date Posted : fromage=X&
#   1, 3, 7, 14


def foo(post_by="", remote="", type="", level="", education=""):
    valid_options = {
        "post_by": ["employer", "recruiter"],
        "remote": ["remote"],
        "type": ["full time", "part time", "contract", "temporary", "internship"],
        "level": ["entry", "mid", "senior", "none"],
        "education": ["none", "high", "associate", "bachelor, master", "doctoral"]
    }

    if post_by not in valid_options["post_by"] and post_by:
        raise ValueError(f"Invalid value for name: {post_by}. Valid options are: {valid_options['post_by']}")

    if remote not in valid_options["remote"] and remote:
        raise ValueError(f"Invalid value for name: {remote}. Valid options are: {valid_options['remote']}")

    if type not in valid_options["type"] and type:
        raise ValueError(f"Invalid value for name: {type}. Valid options are: {valid_options['type']}")

    if level not in valid_options["level"] and level:
        raise ValueError(f"Invalid value for name: {level}. Valid options are: {valid_options['level']}")

    if education not in valid_options["education"] and education:
        raise ValueError(f"Invalid value for name: {education}. Valid options are: {valid_options['education']}")

    output = "0"
    if post_by:
        match post_by:
            case "employer":
                output += "bf%3Aexrec%28%29%"
            case "recruiter":
                output += "bf%3Aexdh%28%29"

    if remote or education or type or level:
        output += "2C"

    if remote:
        output += "kf%3Aattr%28DSQF7%29"

    if education:
        match education:
            case "none":
                if not remote:
                    output += "kf%3A"
                output += "attr%28QJZM9%252COR%29"

            case "high":
                if not remote:
                    output += "kf%3A"
                output += "attr%28FCGTU%7CQJZM9%252COR%29"

            case "associate":
                if not remote:
                    output += "kf%3A"
                output += "attr%28FCGTU%7CQJZM9%7CUTPWG%252COR%29"

            case "bachelor":
                if not remote:
                    output += "kf%3A"
                output += "attr%28FCGTU%7CHFDVW%7CQJZM9%7CUTPWG%252COR%29"

            case "master":
                if not remote:
                    output += "kf%3A"
                output += "attr%28EXSNN%7CFCGTU%7CHFDVW%7CQJZM9%7CUTPWG%252COR%29"

            case "doctoral":
                if not remote:
                    output += "kf%3A"
                output += "attr%286QC5F%252COR%29"

    return "sc=" + output + "%3B&"


print(foo(post_by="recruiter", remote="remote"))

def generate_indeed_url(job_title, location, radius=25, sort_by='relevance', job_type='', salary='', experience='', start=0):
    """
    Generate an Indeed URL based on search parameters
    """
    base_url = 'https://www.indeed.com/jobs'
    params = {
        'q': job_title,
        'l': location,
        'radius': radius,
        'sort': sort_by,
        'jt': job_type,
        'salary': salary,
        'experience': experience,
        'start': start

    }
    url_params = '&'.join([f'{key}={value}' for key, value in params.items() if value])
    return f'{base_url}?{url_params}'

# Example usage
url = generate_indeed_url('quality engineer', 'lafayette, IN', radius=10, salary="$50,000", experience="entry")
print(url)
