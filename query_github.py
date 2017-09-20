import os, requests

GH_PERSONAL_TOKEN = os.environ['GH_PERSONAL_TOKEN']
GH_GRAPHQL_EP = '''https://api.github.com/graphql'''
GH_AUTH_VALUE = "bearer %s" % GH_PERSONAL_TOKEN
GH_HEADERS = {"Authorization": GH_AUTH_VALUE}

QUERY_USER_BASIC_INFO = '''
{
  user(login: "vietlq") {
    avatarUrl (size: 256)
    bio
    email
    websiteUrl
    company
    location
}
'''

requests.post(GH_GRAPHQL_EP, data=QUERY_USER_BASIC_INFO, headers=GH_HEADERS)
