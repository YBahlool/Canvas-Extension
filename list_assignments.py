import requests
import json
import datetime
import pytz

def collect_active_course_ids(headers, courses_url) :
    params = {
        'enrollment_state' : 'active'
    }
    response = requests.get(courses_url, headers = headers, params = params).content
    course_list = json.loads(response)
    course_ids = []
    for course in course_list:
        course_ids.append(course["id"])
    
    return course_ids

def list_upcoming_assignments(course_ids, headers, courses_url,):

    params = {
        'bucket' : 'upcoming'
    }
    upcoming_assignments = {}

    for course_id in course_ids:
        assignments_url = courses_url + f"/{course_id}/assignments"
        response = requests.get(assignments_url, headers = headers, params = params).content
        assignment_list = json.loads(response)
        for assignment in assignment_list:
            
            name = assignment["name"]
            due_date = str(assignment["due_at"][0:-1])
            input_datetime_str = due_date
            input_datetime = datetime.datetime.strptime(input_datetime_str, "%Y-%m-%dT%H:%M:%S")
            input_datetime = pytz.utc.localize(input_datetime)
            target_timezone =  pytz.timezone("US/Pacific")
            pst_datetime = input_datetime.astimezone(target_timezone)
            pst_datetime_str = pst_datetime.strftime("%Y-%m-%d %H:%M:%S %Z")
            id = assignment["id"]
            upcoming_assignments[id] = (name, pst_datetime_str, course_id)
        
    return upcoming_assignments


def main():

    access_token = "8683~JYEreRuq7Zy2M3MhNWSpcE26Iu3kpNIruQW9c5qVkQJ71NzIsKnD8XzZS8Iezl7d"

    headers = {'Authorization': f'Bearer {access_token}'}

    courses_url = f"https://deanza.instructure.com/api/v1/users/self/courses"

    course_ids = collect_active_course_ids(headers, courses_url)

    upcoming_assignments = list_upcoming_assignments(course_ids, headers, courses_url)

    print(upcoming_assignments)

    with open("assignmentlist.txt", "w") as f:

        for assignment_id in upcoming_assignments:
            name = upcoming_assignments[assignment_id][0]
            due_time = upcoming_assignments[assignment_id][1]
            course_id = upcoming_assignments[assignment_id][2]
            link = f"https://deanza.instructure.com/courses/{course_id}/assignments/{assignment_id}"
            f.write(f"{name}, {due_time}, {link}\n")
            


main()
