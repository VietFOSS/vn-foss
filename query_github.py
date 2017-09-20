import os, requests

GH_PERSONAL_TOKEN = os.environ['GH_PERSONAL_TOKEN']
GH_GRAPHQL_EP = '''https://api.github.com/graphql'''
GH_AUTH_VALUE = "bearer %s" % GH_PERSONAL_TOKEN
GH_HEADERS = {
  "Authorization": GH_AUTH_VALUE,
  "Content-Type": "application/x-www-form-urlencoded",
}

QUERY_USER_BASIC_INFO = '''
query {
  user(login: "vietlq") {
    avatarUrl (size: 256),
    bio,
    email,
    websiteUrl,
    company,
    location
  }
}
'''

GH_QUERY_JSON = {"query": QUERY_USER_BASIC_INFO}

requests.post(GH_GRAPHQL_EP, json=GH_QUERY_JSON, headers=GH_HEADERS)
