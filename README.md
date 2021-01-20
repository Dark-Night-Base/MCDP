# MCDP

MCDP Can Download Plugins

⚠️️ MCDP does NOT support python2 and MCDaemon! Currently only supports 
[MCDReforged](https://github.com/Fallen-Breath/MCDReforged). 

⚠️ MCDP does NOT support plugins with folders, 
but these whose folders have the same name with the plugin, 
such as `hello.py` with folder `hello/`, are supported.

## How to use

Install Gitpython first: 

```Linux
pip3 install python-git
```

Then put `MCDP.py` in `plugins/`, others can be done inside the game

- `!!MCDP`: Show help message
- `!!MCDP list`: List the plugins
- `!!MCDP install [plugin]`: Install or upgrade plugin
- `!!MCDP remove [plugin]`: Remove the plugin
- `!!MCDP update`: Update list of available plugins
- `!!MCDP upgrade`: Upgrade the installed plugins

## How it works

*MCDP* manages your plugins via *git*. That's it.

## How to contribute

Click [here](https://github.com/Dark-Night-Base/MCDP/compare) to raise a pull request!

Remember: you'd better to merge into branch [dev](https://github.com/Dark-Night-Base/MCDP/tree/dev) if your plugin has not been fully tested yet.

💡️ We encourage write configurations inside the `MCDReforged/config/` 
instead of making another config file for a single plugin.

## Plugin List

### Tool

#### In Game

| Name                                                   | Maintainer                                           | Function                                         |Updated Time|
| ------------------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------ | ---------- |
| [Here](https://github.com/TISUnion/Here)               | [Fallen_Breath](https://github.com/Fallen-Breath)    | Boardcast your position and high light yourself  | 2021-01-15 |
| [daycount](https://github.com/Dark-Night-Base/daycount)| [Dark-Night-Base](https://github.com/Dark-Night-Base)| `!!day` give you the number of day passed        | 2020-04-28 |
| [Calculator](https://github.com/TISUnion/Calculator)   | [Fallen_Breath](https://github.com/Fallen-Breath)    | In game calculator                               | 2021-01-15 |
| [Beep](https://github.com/TISUnion/Beep)             | [LucunJi](https://github.com/LucunJi)             | Beeps when someone is mentioned in text with an `@` | 2021-01-15 |
| [Seen](https://github.com/TISUnion/Seen/tree/MCDR)   | [Pandaria98](https://github.com/Pandaria98)       | a plugin for showing someone's time spent on working fish  | 2021-01-16 |
| [Timer](https://github.com/Da-Dog/MCDR_Timer)            | [Da_Dog](https://github.com/Da-Dog)           | A count down timer and stopwatch     | 2020-04-16 |
| [MCDR-WikiSearcher](https://github.com/GamerNoTitle/MCDR-WikiSearcher) | [GamerNoTitle](https://github.com/GamerNoTitle)   | A plugin helps you search Minecraft Wiki in game and get the result on one click | 2020-04-16 |
| [LocationMarker](https://github.com/TISUnion/LocationMarker) | [Fallen_Breath](https://github.com/Fallen-Breath) | A server side waypoint manager | 2021-01-19 |
<!-- | [joinMOTD](https://github.com/TISUnion/joinMOTD)       | [Fallen_Breath](https://github.com/Fallen-Breath)    | Welcome message and server list on player joined | 2020-04-07 | -->

#### Outside

| Name                                                        | Maintainer                                        | Function                                                                      |Updated Time|
| ----------------------------------------------------------- | ------------------------------------------------- | --------------------------------------------------- | ---------- |
| [PCRC-MCDR](https://github.com/TISUnion/PCRC-MCDR)          | [Fallen_Breath](https://github.com/Fallen-Breath) | a PCRC plugin                                                                 | 2021-01-15|
<!-- | ----------------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------- | ---------- | -->
<!-- | [MCDR-bot](https://github.com/MCDReforged-Plugins/MCDR-bot) | [Fallen_Breath](https://github.com/Fallen-Breath) | Fake player support based on [pycraft](https://github.com/ammaraskar/pyCraft) | -->
<!-- | [ChatBridge](https://github.com/TISUnion/ChatBridge)        | [Fallen_Breath](https://github.com/Fallen-Breath) | Boardcast chat between mc servers or even discord server                      | -->
### Server Control

| Name                                                        | Maintainer                                        | Function                                            |Updated Time|
| ----------------------------------------------------------- | ------------------------------------------------- | --------------------------------------------------- | ---------- |
| [SimpleOP](https://github.com/MCDReforged-Plugins/SimpleOP) | [Fallen_Breath](https://github.com/Fallen-Breath) | `!!op` to get op, `!!restart` to restart the server | 2021-01-15 |
| [CrashRestart](https://github.com/MCDReforged-Plugins/CrashRestart) | [Fallen_Breath](https://github.com/Fallen-Breath) | A plugin to restart the server after server crashes. Maximum allowance for crashes is configurable | 2021-01-15 |
| [Hibernate](https://github.com/Dark-Night-Base/Hibernate) |[Dark-Night-Base](https://github.com/Dark-Night-Base) | A plugin which hibernates your server when no one's online, and resume it when someone login | 2021-01-20 |

<!-- ### Command Helper -->

<!-- | Name                                                                   | Maintainer                                        | Function                                                              | -->
<!-- | ---------------------------------------------------------------------- | ------------------------------------------------- | --------------------------------------------------------------------- | -->
<!-- | [CarpetFeatureHelper](https://github.com/TISUnion/CarpetFeatureHelper) | [Fallen_Breath](https://github.com/Fallen-Breath) | Give the ability of switching some of carpet options to non-op player | -->

### File Management

| Name                                                               | Maintainer                                            | Function                                       |Updated Time|
| ------------------------------------------------------------------ | ----------------------------------------------------- | ---------------------------------------------- | ---------- |
| [QuickBackupM](https://github.com/TISUnion/QuickBackupM)           | [Fallen_Breath](https://github.com/Fallen-Breath)     | Backup/Restore plugin, with muti backup slot   | 2021-01-14 |
| [RegionFileUpdater](https://github.com/TISUnion/RegionFileUpdater) | [Fallen_Breath](https://github.com/Fallen-Breath)     | Update region files for mirror server          | 2021-01-15 |
| [StatsHelper](https://github.com/TISUnion/StatsHelper)             | [Fallen_Breath](https://github.com/Fallen-Breath)     | Statistic query and scoardboard maker          | 2021-01-16 |
| [AutoBackup](https://github.com/Dark-Night-Base/AutoBackup)        | [Dark-Night-Base](https://github.com/Dark-Night-Base) | Auto backup via *rsync* (tested only on Linux) | 2020-04-07 |
| [MCDP](https://github.com/Dark-Night-Base/MCDP)                    | [Dark-Night-Base](https://github.com/Dark-Night-Base) | Manage plugins via *git*                       | 2021-01-17 |
| [MCDR-Mirror-Server](https://github.com/GamerNoTitle/MCDR-Mirror-Server) | [GamerNoTitle](https://github.com/GamerNoTitle)       | A plugin helps you sync/turn on your mirror server, for building design and redstone debug | 2020-04-26 |
