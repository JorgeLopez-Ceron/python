#add type hinting to methods

class Television:
    #class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    #function to set instance values to defaults
    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    #turns tv on and off
    def power(self):
        if not self.__status:
            self.__status = True
        elif self.__status:
            self.__status = False
    #mutes and un mutes tv
    def mute(self):
        if not self.__muted:
            self.__muted = True
            self.__volume = 0
        elif self.__muted:
            self.__muted = False

    #increases the channel
    def channel_up(self):
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1
    #decreases the channel
    def channel_down(self):
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    #increases volume
    def volume_up(self):
        if self.__status:
            if self.__volume == self.MAX_VOLUME:
                self.__volume == self.MAX_VOLUME
            else:
                self.__volume += 1

        if self.__muted:
            self.__muted = False

    #decreases volume
    def volume_down(self):
        if self.__status:
            if self.__volume == self.MIN_VOLUME:
                self.__volume == self.MIN_VOLUME
            else:
                self.__volume -= 1

        if self.__muted:
            self.__muted = False

    #string that prints with tv info
    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

# tests
tv_1 = Television()
tv_1.power()

tv_1.channel_up()
tv_1.channel_up()
tv_1.volume_up()

tv_1.channel_up()
tv_1.channel_up()
tv_1.channel_up()
tv_1.volume_down()
tv_1.volume_down()

tv_1.power()
tv_1.volume_up()
tv_1.channel_down()

tv_1.power()
tv_1.volume_up()
tv_1.volume_up()
tv_1.volume_up()
tv_1.channel_down()
tv_1.channel_down()
tv_1.mute()
print(tv_1)
