import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(int(password))
        self.age = int(age)
class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = 0
        self.adult_mode = False
class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = []
        self.videos = []
        self.current_user = None


    def log_in(self, nickname, password):
        if nickname and password in self.users:
            self.current_user = (nickname, password)

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users.append(nickname)
            self.users.append(password)
            self.users.append(age)
    def log_out(self, current_user):
        self.current_user = None

    def add(self, *args):
        for i in args:
            for j in self.videos:
                if i.title not in j.title:
                    self.videos.append(args)
        else:
            pass


    def get_videos(self, search_title):
        for i in self.videos:
            for j in self.videos:
                if j.lower() in search_title.lower() or search_title.lower() in j.lower():
                    return self.videos
    def watch_video(self, title_video):
        if title_video == self.videos:
            print(time.sleep(10))




if __name__ == "__main__":
    ur = UrTube
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')



