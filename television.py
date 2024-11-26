#add type hinting to methods

class Television:
    """Class variables"""
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """function that sets the default values
        Parameters: None

        Returns: None

        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    #turns tv on and off
    def power(self):
        """turns the tv on and off

        Parameters: None

        Returns: None

        """
        if not self.__status:
            self.__status = True
        elif self.__status:
            self.__status = False

    def mute(self):
        """Mutes the tv

        Parameters: None

        Returns: None

        """
        if not self.__muted:
            self.__muted = True
            self.__volume = 0
        elif self.__muted:
            self.__muted = False

    def channel_up(self):
        """increases the channel

        Parameters: None

        Returns: None

        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """turns the channel down

        Parameters: None

        Returns: None

        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        """turns the tv volume up

        Parameters: None

        Returns: None

        """
        if self.__status:
            if self.__volume == self.MAX_VOLUME:
                self.__volume == self.MAX_VOLUME
            else:
                self.__volume += 1

        if self.__muted:
            self.__muted = False

    def volume_down(self):
        """turns the tv volume down

        Parameters: None

        Returns: None

        """
        if self.__status:
            if self.__volume == self.MIN_VOLUME:
                self.__volume == self.MIN_VOLUME
            else:
                self.__volume -= 1

        if self.__muted:
            self.__muted = False

    def __str__(self):
        """ function that sets the print layout

        Parameters: None

        Returns: string: print statement that returns the values of status, channel, and volume

        """
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
