import requests

sample_db = {
    1:"Jack",
    2:"Bob",
    3:"Alice"
}

def get_user_from_sample_db(user_id):
    return sample_db.get(user_id)


def get_users():
    response = requests.get('http://jsonplaceholder.typicode.com/users')
    if response.status_code == 200:
        return response.json()
    
    raise requests.HTTPError('Cannot fetch users')