# coding: utf-8
#

__apk_version__ = '1.1.3'
# 1.1.3 use thread to make watchers.watched faster, try to fix input method type multi
# 1.1.2 fix count error when have child && sync watched, to prevent watchers.remove error
# 1.1.1 support toast capture
# 1.1.0 update uiautomator-v18:2.1.2 -> uiautomator-v18:2.1.3 (This version fixed setWaitIdleTimeout not working bug)
# 1.0.14 catch NullException, add gps mock support
# 1.0.13 whatsinput suppoort, but not very well
# 1.0.12 add toast support
# 1.0.11 add auto install support
# 1.0.10 fix service not started bug
# 1.0.9 fix apk version code and version name
# ERR: 1.0.8 bad version number. show ip on notification
# ERR: 1.0.7 bad version number. new input method, some bug fix

__atx_agent_version__ = '0.3.5'
# 0.3.5 hot fix for session
# 0.3.4 fix session() sometimes can not get mainActivity error
# 0.3.3 /shell support timeout
# 0.3.2 fix dns resolve error when network changes
# 0.3.0 use github.com/codeskyblue/heartbeat library instead of websocket, add /whatsinput
# 0.2.1 support occupy /minicap connection
# 0.2.0 add session support
# 0.1.8 fix screenshot always the same image. (BUG in 0.1.7), add /shell/stream add timeout for /shell
# 0.1.7 fix dns resolve error in /install
# 0.1.6 change download logic. auto fix orientation
# 0.1.5 add singlefight for minicap and minitouch, proxy dial-timeout change 30 to 10
# 0.1.4 phone remote control
# 0.1.2 /download support
# 0.1.1 minicap buildin