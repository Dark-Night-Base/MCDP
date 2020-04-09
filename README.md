# MCDP
MCDP Can Download Plugins

⚠️️ MCDP does NOT support python2 and MCDaemon! Currently only supports [MCDReforged](https://github.com/Fallen-Breath/MCDReforged).

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

Click [here](https://github.com/Dark-Night-Base/MCDP/compare) to start a Pull request!

Remember: you'd better to merge into branch [dev](https://github.com/Dark-Night-Base/MCDP/tree/dev) if your plugin has not been fully tested yet.

## Plugin List

### Tool

#### In Game

| Name                                                   | Maintainer                                           | Function                                         |Updated Time|
| ------------------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------ | ---------- |
| [Here](https://github.com/TISUnion/Here)               | [Fallen_Breath](https://github.com/Fallen-Breath)    | Boardcast your position and high light yourself  | 2020-04-07 |
| [joinMOTD](https://github.com/TISUnion/joinMOTD)       | [Fallen_Breath](https://github.com/Fallen-Breath)    | Welcome message and server list on player joined | 2020-04-07 |
| [daycount](https://github.com/Dark-Night-Base/daycount)| [Dark-Night-Base](https://github.com/Dark-Night-Base)| `!!day` give you the number of day passed        | 2020-04-07 |
| [Calculator](https://github.com/TISUnion/Calculator)   | [Fallen_Breath](https://github.com/Fallen-Breath)    | In game calculator                               | 2020-04-07 |

<!-- #### Outside -->

<!-- | Name                                                        | Maintainer                                        | Function                                                                      |Updated Time| -->
<!-- | ----------------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------- | ---------- | -->
<!-- | [MCDR-bot](https://github.com/MCDReforged-Plugins/MCDR-bot) | [Fallen_Breath](https://github.com/Fallen-Breath) | Fake player support based on [pycraft](https://github.com/ammaraskar/pyCraft) | -->
<!-- | [ChatBridge](https://github.com/TISUnion/ChatBridge)        | [Fallen_Breath](https://github.com/Fallen-Breath) | Boardcast chat between mc servers or even discord server                      | -->
<!-- | [PCRC-MCDR](https://github.com/TISUnion/PCRC-MCDR)          | [Fallen_Breath](https://github.com/Fallen-Breath) | a PCRC plugin                                                                 | -->

### Server Control

| Name                                                        | Maintainer                                        | Function                                            |Updated Time|
| ----------------------------------------------------------- | ------------------------------------------------- | --------------------------------------------------- | ---------- |
| [SimpleOP](https://github.com/MCDReforged-Plugins/SimpleOP) | [Fallen_Breath](https://github.com/Fallen-Breath) | `!!op` to get op, `!!restart` to restart the server | 2020-04-07 |

<!-- ### Command Helper -->

<!-- | Name                                                                   | Maintainer                                        | Function                                                              | -->
<!-- | ---------------------------------------------------------------------- | ------------------------------------------------- | --------------------------------------------------------------------- | -->
<!-- | [CarpetFeatureHelper](https://github.com/TISUnion/CarpetFeatureHelper) | [Fallen_Breath](https://github.com/Fallen-Breath) | Give the ability of switching some of carpet options to non-op player | -->

### File Management

| Name                                                               | Maintainer                                            | Function                                       |Updated Time|
| ------------------------------------------------------------------ | ----------------------------------------------------- | ---------------------------------------------- | ---------- |
| [QuickBackupM](https://github.com/TISUnion/QuickBackupM)           | [Fallen_Breath](https://github.com/Fallen-Breath)     | Backup/Restore plugin, with muti backup slot   | 2020-04-07 |
| [RegionFileUpdater](https://github.com/TISUnion/RegionFileUpdater) | [Fallen_Breath](https://github.com/Fallen-Breath)     | Update region files for mirror server          | 2020-04-07 |
| [StatsHelper](https://github.com/TISUnion/StatsHelper)             | [Fallen_Breath](https://github.com/Fallen-Breath)     | Statistic query and scoardboard maker          | 2020-04-07 |
| [AutoBackup](https://github.com/Dark-Night-Base/AutoBackup)        | [Dark-Night-Base](https://github.com/Dark-Night-Base) | Auto backup via *rsync* (tested only on Linux) | 2020-04-07 |
| [MCDP](https://github.com/Dark-Night-Base/MCDP)                    | [Dark-Night-Base](https://github.com/Dark-Night-Base) | Manage plugins via *git*                       | 2020-04-09 |
