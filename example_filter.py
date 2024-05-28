import json

def load_users(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def filter_users(users, min_age=None, max_age=None, city=None):
    filtered = []
    for user in users:
        if min_age is not None and user['age'] < min_age:
            continue
        if max_age is not None and user['age'] > max_age:
            continue
        if city is not None and user['city'].lower() != city.lower():
            continue
        filtered.append(user)
    return filtered

def main():
    users = load_users('users.json')
    filtered_users = filter_users(users, min_age=25, city='New York')
    for user in filtered_users:
        print(user)

if __name__ == "__main__":
    main()