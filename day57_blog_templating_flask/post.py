import requests

ALL_POSTS_URL: str = 'https://api.npoint.io/9a23bb235b4f7968642f'


class Post:

    def __init__(self):
        self.all_posts: str = requests.get(url=ALL_POSTS_URL).json()

    def get_current_post(self, numero):
        for post in self.all_posts:
            compare_index = self.all_posts.index(post)
            if compare_index == numero:
                return post
