import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname.lower() == nickname.lower() and user.password == password:
                self.current_user = user
                return
        print("Неверные логин или пароль")

    def register(self, nickname, password, age):

        if nickname in [user.nickname for user in self.users]:
            print(f"Пользователь {nickname} уже существует")


        elif age >= 18 and nickname not in [user.nickname for user in self.users]:
            self.users.append(User(nickname, password, age))
            self.current_user = self.users[-1]

        elif age < 18:
            self.users.append(User(nickname, password, age))
            print(f"Войдите в аккаунт, чтобы смотреть видео")
            print("Вам нет 18 лет, пожалуйста покиньте страницу")

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for movie in args:
            if movie not in self.videos:
                self.videos.append(movie)

    def get_videos(self, search_word):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video(self, video_title):
        if self.current_user:
            for video in self.videos:
                if video.title.lower() == video_title.lower():

                    video.time_now = 0
                    for i in range(0, 1):
                        print(video.time_now, end=' ')
                        time.sleep(1),
                        video.time_now += 1
                    print("Конец видео")


ur = UrTube()
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
