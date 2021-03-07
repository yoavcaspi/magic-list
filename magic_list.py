from collections import UserList


class MagicList(UserList):
    def __setitem__(self, i, item):
        if len(self.data) == i or i == -1:
            self.data.append(item)
        else:
            self.data[i] = item
