import pytest
from television import Television

def test_init():
    tv = Television()
    expected_str = 'Power = False, Channel = 0, Volume = 0'
    assert str(tv) == expected_str

def test_power():
    tv_p = Television()
    tv_p.power()
    expected_str_for_power = 'Power = True, Channel = 0, Volume = 0'
    assert str(tv_p) == expected_str_for_power

    tv_p.power()
    expected_str_for_power2 = 'Power = False, Channel = 0, Volume = 0'
    assert str(tv_p) == expected_str_for_power2

def test_mute():
    tv_m = Television()
    tv_m.power()
    tv_m.volume_up()
    tv_m.mute()
    expected_str_for_mute = 'Power = True, Channel = 0, Volume = 0'
    assert str(tv_m) == expected_str_for_mute

    tv_m2 = Television()
    tv_m2.power()
    tv_m2.volume_up()
    tv_m2.mute()
    tv_m2.mute()
    expected_str_for_mute2 = 'Power = True, Channel = 0, Volume = 1'
    assert str(tv_m2) == expected_str_for_mute2

    tv_m3 = Television()
    tv_m3.mute()
    expected_str_for_mute3 = 'Power = False, Channel = 0, Volume = 0'
    assert str(tv_m3) == expected_str_for_mute3

    tv_m4 = Television()
    tv_m4.mute()
    tv_m4.mute()
    expected_str_for_mute4 = 'Power = False, Channel = 0, Volume = 0'
    assert str(tv_m4) == expected_str_for_mute4

def test_channel_up():
    tv_c = Television()
    tv_c.channel_up()
    expected_str_for_channel_up = 'Power = False, Channel = 0, Volume = 0'
    assert str(tv_c) == expected_str_for_channel_up

    tv_c2 = Television()
    tv_c2.power()
    tv_c2.channel_up()
    expected_str_for_channel_up2 = 'Power = True, Channel = 1, Volume = 0'
    assert str(tv_c2) == expected_str_for_channel_up2

    tv_c3 = Television()
    tv_c3.power()
    tv_c3.channel_up()
    tv_c3.channel_up()
    tv_c3.channel_up()
    tv_c3.channel_up()
    expected_str_for_channel_up3 = 'Power = True, Channel = 0, Volume = 0'
    assert str(tv_c3) == expected_str_for_channel_up3

def test_channel_down():
    tv_cd = Television()
    tv_cd.channel_down()
    expected_str_for_channel_down = 'Power = False, Channel = 0, Volume = 0'
    assert str(tv_cd) == expected_str_for_channel_down

    tv_cd2 = Television()
    tv_cd2.power()
    tv_cd2.channel_down()
    tv_cd2.channel_down()
    expected_str_for_channel_down2 = 'Power = True, Channel = 2, Volume = 0'
    assert str(tv_cd2) == expected_str_for_channel_down2

def test_volume_up():
    tv_v = Television()
    tv_v.volume_up()
    expected_str_for_volume_up = 'Power = False, Channel = 0, Volume = 0'
    assert str(tv_v) == expected_str_for_volume_up

    tv_v2 = Television()
    tv_v2.power()
    tv_v2.volume_up()
    expected_str_for_volume_up2 = 'Power = True, Channel = 0, Volume = 1'
    assert str(tv_v2) == expected_str_for_volume_up2

    tv_v3 = Television()
    tv_v3.power()
    tv_v3.mute()
    tv_v3.volume_up()
    expected_str_for_volume_up3 = 'Power = True, Channel = 0, Volume = 1'
    assert str(tv_v3) == expected_str_for_volume_up3

    tv_v4 = Television()
    tv_v4.power()
    tv_v4.volume_up()
    tv_v4.volume_up()
    tv_v4.volume_up()
    expected_str_for_volume_up4 = 'Power = True, Channel = 0, Volume = 2'
    assert str(tv_v4) == expected_str_for_volume_up4

def test_volume_down():
    tv_d = Television()
    tv_d.volume_down()
    expected_str_for_volume_down = 'Power = False, Channel = 0, Volume = 0'
    assert str(tv_d) == expected_str_for_volume_down

    tv_d2 = Television()
    tv_d2.power()
    tv_d2.volume_up()
    tv_d2.volume_up()
    tv_d2.volume_down()
    expected_str_for_volume_down2 = 'Power = True, Channel = 0, Volume = 1'
    assert str(tv_d2) == expected_str_for_volume_down2

    tv_d3 = Television()
    tv_d3.power()
    tv_d3.volume_up()
    tv_d3.volume_up()
    tv_d3.mute()
    tv_d3.volume_down()
    expected_str_for_volume_down3 = 'Power = True, Channel = 0, Volume = 1'
    assert str(tv_d3) == expected_str_for_volume_down3
