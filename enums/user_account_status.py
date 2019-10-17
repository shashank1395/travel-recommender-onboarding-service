import enum

class UserAccountStatus(enum.Enum):
    ACTIVE = 1
    INACTIVE = 2
    BANNED = 3
    SUSPENDED = 4
    DELETED = 5

user_account_status_map = {}

for status in (UserAccountStatus):
    user_account_status_map[status.value] = status

def get_status_by_code(status_code):
    if(status_code in user_account_status_map):
        return user_account_status_map.get(status_code)
    else:
        return -1