## `Discord`.`Commands`.`Bot` | `Project` `Heimdall`
[![Tag](https://img.shields.io/github/v/tag/SirQuacksALot/py.discord.autochannel?style=flat-square)](https://github.com/SirQuacksALot/py.discord.autochannel/releases "Latest Tag") [![License](https://img.shields.io/github/license/SirQuacksAlot/py.discord.autochannel?style=flat-square)](https://github.com/SirQuacksALot/py.discord.autochannel/blob/stable/LICENSE "The Repo's License") [![CodeFactor](https://www.codefactor.io/repository/github/sirquacksalot/py.discord.command.bot/badge?style=flat-square)](https://www.codefactor.io/repository/github/sirquacksalot/py.discord.command.bot "Code Quality") [![Release](https://img.shields.io/github/actions/workflow/status/SirQuacksALot/py.discord.autochannel/release.yaml?style=flat-square)](https://github.com/SirQuacksALot/py.discord.autochannel/actions/workflows/release.yaml)


Discord Bot to automatically create voice channels on entering a specified voice channel written in python.

> [!WARNING]
> Currently work in progess. Please ignore missing parts and just feel free take a look around 👀

## Getting started 🛫

### Dependencies

1. Bot token - *Have a discord bot setuped in the development portal and your server*
2. Python3 installed - *Only for direct running the programm*

### Docker deployment

Deploy single container with docker

```bash
docker run -e DISCORD_TOKEN=yourTokenHere ghcr.io/sirquacksalot/heimdalldbot:latest
```

Deploy with Docker compose in a stack

```bash
services:
  bot:
    image: ghcr.io/sirquacksalot/heimdalldbot:latest
    container_name: heimdall-bot
    environment: 
      - DISCORD_TOKEN=${DISCORD_TOKEN} # use the .env file
    volumes:
      - "db:/bot/app/database"
      - "commands:/bot/app/commands"

volumes:
  db:
  commands:
```

### Direct running the program

Clone the repo

```bash
git clone git@github.com:SirQuacksALot/py.discord.autochannel.git
```

Create a .env file by copying the `example.env`
```bash
cp example.env .env
```

Change the bot `TOKEN` in the newly created .env to your token.

Run the program

```bash
python3 ./main.py
```
## Documentation 📖

- [How to use the Bot](docs/guide.md)
- [Development documentation](docs/dev/the_plan.md)

## Repo Activity 👀

![Alt](https://repobeats.axiom.co/api/embed/bd873357e4eb42b1f9c5ba56f2693b438d5ae1a3.svg "Repobeats analytics image")
