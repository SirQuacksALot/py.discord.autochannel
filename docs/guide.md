# How to use the bot

[![Button](https://img.shields.io/badge/README-0e1114?style=flat-square)](/README.md)
![Spacer](https://img.shields.io/badge/%7C-0e1114?style=flat-square)
[![Button](https://img.shields.io/badge/How_to_use_the_bot-24292e?style=flat-square)](/docs/guide.md)
[![Button](https://img.shields.io/badge/Development_documentation-0e1114?style=flat-square)](/docs/dev/README.md)

## The concept

The conept of the bot is to dynacially load manager scritps which implement new commands and functionality. In the project there is a `commands` submodule to provide basic functionality and give example for own developed ones.

## Add a script

To add a new script a python file has to be provided and put into the `commands` folder of the bot instance.

In the case you are running the bot as a docker container you have to either link the `comamnds` folder to a `local folder` or, as it is in the [example](/README.md#docker-deployment), as a `volume` and add the script files into the `commands` folder of this `volume`.

If you want to develop own scritps please take a look at the basic provided scripts and the [development documentation](/docs/dev/the_plan.md).

## Remove a script

To remove a script. Just delete it from the `commands` folder.

### Commands Collection

> [!important]
> *This might change in the future depending on future changes and this repo will function as a simple collection to download openly available scritps.*

Basic or general commands  to give some simple functionality are developed in the [heimdall commands collection](https://github.com/SirQuacksALot/py.heimdall.commands.collection) repo and will be part of the default scripts.


## The default scripts

The default functionalities are `ping`, `delete message` and `auto voice channels`. The commands of these basic scripts can be accessed with `/` and are synced with the guild command tree. Depedning on the command admin privilages are required. For example the `auto voice channels` require admin privilages.

### Ping

The ping script adds a `/ping` command that returns a pong message.

### Delete message

The delete message script adds a `/delete_message` command which deletes a message by an given message id. It is used to delete old debugging or other message written by the bot.

### Auto Channel

The auto channel script adds the functionality of registering join listeners which automatically create a new voice channel and move the user into it. Also they delete the channel when it is empty.

#### Commands added by this script

- `/add_channel_listener` - adds a new listener for a given channel
- `/remove_channel_listener` - removes a listener from registered list by a given channel
