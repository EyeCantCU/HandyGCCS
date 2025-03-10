#!/sbin/python3
# This file is part of Handheld Game Console Controller System (HandyGCCS)
# Copyright 2022-2023 Derek J. Clark <derekjohn.clark@gmail.com>

from evdev import AbsInfo, ecodes as e
from pathlib import Path

CHIMERA_LAUNCHER_PATH = Path('/usr/share/chimera/bin/chimera-web-launcher')
CONFIG_DIR = "/etc/handygccs/"
CONFIG_PATH = "/etc/handygccs/handygccs.conf"
CONTROLLER_EVENTS = {
    e.EV_KEY: [
        e.KEY_ESC,
        e.KEY_1,
        e.KEY_2,
        e.KEY_3,
        e.KEY_4,
        e.KEY_5,
        e.KEY_6,
        e.KEY_7,
        e.KEY_8,
        e.KEY_9,
        e.KEY_0,
        e.KEY_MINUS,
        e.KEY_EQUAL,
        e.KEY_BACKSPACE,
        e.KEY_TAB,
        e.KEY_Q,
        e.KEY_W,
        e.KEY_E,
        e.KEY_R,
        e.KEY_T,
        e.KEY_Y,
        e.KEY_U,
        e.KEY_I,
        e.KEY_O,
        e.KEY_P,
        e.KEY_LEFTBRACE,
        e.KEY_RIGHTBRACE,
        e.KEY_ENTER,
        e.KEY_LEFTCTRL,
        e.KEY_A,
        e.KEY_S,
        e.KEY_D,
        e.KEY_F,
        e.KEY_G,
        e.KEY_H,
        e.KEY_J,
        e.KEY_K,
        e.KEY_L,
        e.KEY_SEMICOLON,
        e.KEY_APOSTROPHE,
        e.KEY_GRAVE,
        e.KEY_LEFTSHIFT,
        e.KEY_BACKSLASH,
        e.KEY_Z,
        e.KEY_X,
        e.KEY_C,
        e.KEY_V,
        e.KEY_B,
        e.KEY_N,
        e.KEY_M,
        e.KEY_COMMA,
        e.KEY_DOT,
        e.KEY_SLASH,
        e.KEY_RIGHTSHIFT,
        e.KEY_KPASTERISK,
        e.KEY_LEFTALT,
        e.KEY_SPACE,
        e.KEY_CAPSLOCK,
        e.KEY_F1,
        e.KEY_F2,
        e.KEY_F3,
        e.KEY_F4,
        e.KEY_F5,
        e.KEY_F6,
        e.KEY_F7,
        e.KEY_F8,
        e.KEY_F9,
        e.KEY_F10,
        e.KEY_NUMLOCK,
        e.KEY_SCROLLLOCK,
        e.KEY_KP7,
        e.KEY_KP8,
        e.KEY_KP9,
        e.KEY_KPMINUS,
        e.KEY_KP4,
        e.KEY_KP5,
        e.KEY_KP6,
        e.KEY_KPPLUS,
        e.KEY_KP1,
        e.KEY_KP2,
        e.KEY_KP3,
        e.KEY_KP0,
        e.KEY_KPDOT,
        e.KEY_ZENKAKUHANKAKU,
        e.KEY_102ND,
        e.KEY_F11,
        e.KEY_F12,
        e.KEY_RO,
        e.KEY_KATAKANA,
        e.KEY_HIRAGANA,
        e.KEY_HENKAN,
        e.KEY_KATAKANAHIRAGANA,
        e.KEY_MUHENKAN,
        e.KEY_KPJPCOMMA,
        e.KEY_KPENTER,
        e.KEY_RIGHTCTRL,
        e.KEY_KPSLASH,
        e.KEY_SYSRQ,
        e.KEY_RIGHTALT,
        e.KEY_HOME,
        e.KEY_UP,
        e.KEY_PAGEUP,
        e.KEY_LEFT,
        e.KEY_RIGHT,
        e.KEY_END,
        e.KEY_DOWN,
        e.KEY_PAGEDOWN,
        e.KEY_INSERT,
        e.KEY_DELETE,
        e.KEY_MACRO,
        e.KEY_MUTE,
        e.KEY_VOLUMEDOWN,
        e.KEY_VOLUMEUP,
        e.KEY_POWER,
        e.KEY_KPEQUAL,
        e.KEY_KPPLUSMINUS,
        e.KEY_PAUSE,
        e.KEY_KPCOMMA,
        e.KEY_HANGUEL,
        e.KEY_HANJA,
        e.KEY_YEN,
        e.KEY_LEFTMETA,
        e.KEY_RIGHTMETA,
        e.KEY_COMPOSE,
        e.KEY_STOP,
        e.KEY_CALC,
        e.KEY_SLEEP,
        e.KEY_WAKEUP,
        e.KEY_MAIL,
        e.KEY_BOOKMARKS,
        e.KEY_COMPUTER,
        e.KEY_BACK,
        e.KEY_FORWARD,
        e.KEY_NEXTSONG,
        e.KEY_PLAYPAUSE,
        e.KEY_PREVIOUSSONG,
        e.KEY_STOPCD,
        e.KEY_HOMEPAGE,
        e.KEY_REFRESH,
        e.KEY_F13,
        e.KEY_F14,
        e.KEY_F15,
        e.KEY_SEARCH,
        e.KEY_MEDIA,
        e.BTN_SOUTH,
        e.BTN_EAST,
        e.BTN_NORTH,
        e.BTN_WEST,
        e.BTN_TL,
        e.BTN_TR,
        e.BTN_SELECT,
        e.BTN_START,
        e.BTN_MODE,
        e.BTN_THUMBL,
        e.BTN_THUMBR,
    ],
    e.EV_ABS: [
        (e.ABS_X, AbsInfo(0, -32768, 32767, 16, 128, 0)),
        (e.ABS_Y, AbsInfo(0, -32768, 32767, 16, 128, 0)),
        (e.ABS_Z, AbsInfo(0, 0, 255, 0, 0, 0)),
        (e.ABS_RX, AbsInfo(0, -32768, 32767, 16, 128, 0)),
        (e.ABS_RY, AbsInfo(0, -32768, 32767, 16, 128, 0)),
        (e.ABS_RZ, AbsInfo(0, 0, 255, 0, 0, 0)),
        (e.ABS_HAT0X, AbsInfo(0, -1, 1, 0, 0, 0)),
        (e.ABS_HAT0Y, AbsInfo(0, -1, 1, 0, 0, 0)),
    ],
    e.EV_MSC: [
        e.MSC_SCAN,
    ],
    e.EV_LED: [
        e.LED_NUML,
        e.LED_CAPSL,
        e.LED_SCROLLL,
    ],
    e.EV_FF: [
        e.FF_RUMBLE,
        e.FF_PERIODIC,
        e.FF_SQUARE,
        e.FF_TRIANGLE,
        e.FF_SINE,
        e.FF_GAIN,
    ],
}
DETECT_DELAY = 0.5
EVENT_ALT_TAB = [[e.EV_KEY, e.KEY_LEFTALT], [e.EV_KEY, e.KEY_TAB]]
EVENT_ESC = [[e.EV_MSC, e.MSC_SCAN], [e.EV_KEY, e.KEY_ESC]]
EVENT_KILL = [[e.EV_KEY, e.KEY_LEFTMETA], [e.EV_KEY, e.KEY_LEFTCTRL], [e.EV_KEY, e.KEY_ESC]]
EVENT_MODE = [[e.EV_KEY, e.BTN_MODE]]
EVENT_OPEN_CHIM = ["Open Chimera"]
EVENT_OSK = [[e.EV_KEY, e.BTN_MODE], [e.EV_KEY, e.BTN_NORTH]]
EVENT_OSK_DE = [[e.EV_KEY, e.KEY_LEFTMETA], [e.EV_KEY, e.KEY_LEFTCTRL], [e.EV_KEY, e.KEY_O]]
EVENT_QAM = [[e.EV_KEY, e.BTN_MODE], [e.EV_KEY, e.BTN_SOUTH]]
EVENT_SCR = [[e.EV_KEY, e.BTN_MODE], [e.EV_KEY, e.BTN_TR]]
EVENT_TOGGLE_GYRO = ["Toggle Gyro"]
EVENT_TOGGLE_MOUSE = ["Toggle Mouse Mode"]
EVENT_TOGGLE_PERF = ["Toggle Performance"]
EVENT_MAP = {
        "ALT_TAB": EVENT_ALT_TAB,
        "ESC": EVENT_ESC,
        "KILL": EVENT_KILL,
        "MODE": EVENT_MODE,
        "OPEN_CHIMERA": EVENT_OPEN_CHIM,
        "OSK": EVENT_OSK,
        "QAM": EVENT_QAM,
        "SCR": EVENT_SCR,
        "TOGGLE_GYRO": EVENT_TOGGLE_GYRO,
        "TOGGLE_MOUSE": EVENT_TOGGLE_MOUSE,
        "TOGGLE_PERFORMANCE": EVENT_TOGGLE_PERF,
    }
POWER_ACTION_HIBERNATE = ["Hibernate"]
POWER_ACTION_SHUTDOWN = ["Shutdown"]
POWER_ACTION_SUSPEND = ["Suspend"]
POWER_ACTION_MAP = {
        "HIBERNATE": POWER_ACTION_HIBERNATE,
        "SHUTDOWN":  POWER_ACTION_SHUTDOWN,
        "SUSPEND":   POWER_ACTION_SUSPEND,
    }
INSTANT_EVENTS = [EVENT_MODE, EVENT_OPEN_CHIM, EVENT_TOGGLE_GYRO, EVENT_TOGGLE_MOUSE, EVENT_TOGGLE_PERF]
QUEUED_EVENTS = [EVENT_ALT_TAB, EVENT_ESC, EVENT_KILL, EVENT_OSK, EVENT_OSK_DE, EVENT_QAM, EVENT_SCR]
FF_DELAY = 0.2
HIDE_PATH = Path("/dev/input/.hidden/")
HOME_PATH = Path('/home')
JOY_MAX = 32767
JOY_MIN = -32767
