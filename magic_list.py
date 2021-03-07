from collections import UserList


class MagicList(UserList):
    def __setitem__(self, i, item):
        if len(self.data) == i:
            self.data.append(item)
        else:
            self.data[i] = item
