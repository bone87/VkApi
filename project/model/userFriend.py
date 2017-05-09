from project.model.user import User


class UserFriend(User):
    def parse_response_to_user_friend_model(self, response):
        self.__init__(response)
        self.friend_status = response['friend_status']
        return self
