

class Television:
    """Class variables"""
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """function that sets the default values
        Parameters: None

        Returns: None

        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__old_volume = self.__volume

    def power(self) -> None:
        """turns the tv on and off

        Parameters: None

        Returns: None

        """
        if not self.__status:
            self.__status = True
        elif self.__status:
            self.__status = False

    def mute(self) -> None:
        """Mutes the tv

        Parameters: None

        Returns: None

        """
        if self.__status:
            if not self.__muted:
                self.__muted = True
                self.__old_volume = self.__volume
                self.__volume = 0
            elif self.__muted:
                self.__muted = False
                self.__volume = self.__old_volume

    def channel_up(self) -> None:
        """increases the channel

        Parameters: None

        Returns: None

        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """turns the channel down

        Parameters: None

        Returns: None

        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """turns the tv volume up

        Parameters: None

        Returns: None

        """
        if self.__muted:
            self.__muted = False
            self.__volume = self.__old_volume

        if self.__status:
            if self.__volume == self.MAX_VOLUME:
                self.__volume = self.MAX_VOLUME
            else:
                self.__volume += 1



    def volume_down(self):
        """turns the tv volume down

        Parameters: None

        Returns: None

        """
        if self.__muted:
            self.__muted = False
            self.__volume = self.__old_volume

        if self.__status:
            if self.__volume == self.MIN_VOLUME:
                self.__volume = self.MIN_VOLUME
            else:
                self.__volume -= 1


    def __str__(self) -> str:
        """ function that sets the print layout

        Parameters: None

        Returns: string: print statement that returns the values of status, channel, and volume

        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'



